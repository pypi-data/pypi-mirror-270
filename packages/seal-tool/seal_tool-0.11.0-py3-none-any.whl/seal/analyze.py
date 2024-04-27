import argparse
import copy
import math
import random
import warnings
from collections.abc import Callable, Iterator, Mapping, Sequence
from dataclasses import astuple, dataclass
from pathlib import Path
from typing import Literal, cast

import numpy as np
import pandas as pd
from alive_progress import alive_bar  # type: ignore[import-untyped]
from scipy import optimize  # type: ignore[import-untyped] # https://github.com/scipy/scipy/issues/17158

import seal.config as conf
from seal.common import analysis_results_filename, enc_dtypes, geom_r2, get_spinner, qlist_dtypes
from seal.config import Analysis, Analysis2, Analysis3, Analysis4, Distance, LevelStrategy, QuadratType, Sides
from seal.exceptions import InputType, InvalidFilterError, InvalidLiteralError, InvalidQuadratsError, MissingValuesError

type Caps = dict[Literal['centroid', 'diagonal', 'max1dx', 'max1dy', 'total_area'], float]
type DistFunction = Callable[[pd.DataFrame, pd.DataFrame], 'pd.Series[float]']
type Edge = Literal['left', 'right', 'top', 'bottom']
type Encounters = pd.DataFrame
type QList = pd.DataFrame
type SppMatrix = pd.DataFrame


@dataclass
class GridInfo:
    """Contains information about spp. encounters and layout of the study grid."""

    enc: Encounters
    qlist: QList

    def __iter__(self) -> Iterator[Encounters | QList]:
        return iter(astuple(self))


@dataclass
class LevelInfo:
    """Contains level- (and strategy-) dependent information about the study grid."""

    subgrids: list[GridInfo]
    dmats: list[pd.DataFrame]
    sides: Sides

    def __iter__(self) -> Iterator[list[GridInfo] | list[pd.DataFrame] | Sides]:
        return iter(astuple(self))


def main(args: argparse.Namespace) -> int:
    """Load taskfile configuration, datasets, perform and save requested analyses.

    Create output directory if necessary.
    """
    cfg = conf.Config.from_taskfile(args.taskfile)
    enc = load_encounters(cfg.encounters)

    try:
        enc = filter_encounters(enc, cfg)
    except AttributeError as e:
        raise InvalidFilterError(e.name, InputType.ENCOUNTERS) from e

    if cfg.locality.quadrat_list:
        try:
            quadrats = load_quadrats(cfg.locality.quadrat_list, cfg.quadrat_types)
        except AttributeError as e:
            raise InvalidFilterError(e.name, InputType.QLIST) from e
    else:
        print('Quadrat list not passed separately, please ensure you understand the implications of doing this.')
        quadrats = generate_quadrat_list(enc)

    grinfo = GridInfo(enc, quadrats)
    check_grid_consistency(grinfo)
    (grinfo, sides_adj, caps) = adjust_grid(grinfo, cfg)

    n_tasks = len(set(cfg.levels)) * len(cfg.analyses)
    spinner = get_spinner()
    lvl_infos = get_lvl_infos(grinfo, sides_adj, caps, cfg)
    analysis_idx = {analysis.type_: 0 for analysis in cfg.analyses}
    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    with alive_bar(n_tasks, title='Analysis', spinner=spinner) as bar:
        for analysis in cfg.analyses:
            completed = []
            additional = []
            for level, lvl_info in lvl_infos.items():
                bar.text(f'{analysis.type_}, level {level}')
                res, additional_data = do_analysis(lvl_info, analysis, cfg.seed, caps)
                res['level'] = level
                completed.append(res)
                additional.append(additional_data)
                bar()
            a_info = (analysis.type_, analysis_idx[analysis.type_])
            save_results(args, cfg.out_dir, completed, additional, a_info)
            analysis_idx[analysis.type_] += 1
    return 0


def do_analysis(  # noqa: PLR0911
    lvl_info: LevelInfo,
    analysis: Analysis,
    seed: int | None,
    caps: Caps,
) -> tuple[pd.DataFrame, str | pd.DataFrame | None]:
    """Return results of `analysis` on passed subgrids with given config settings."""
    if seed:
        random.seed(seed)
        np.random.seed(seed)

    subgrids = lvl_info.subgrids
    spp_matrices = [get_spp_matrix(subgrid) for subgrid in subgrids]
    match analysis.type_:
        case 'a1' | 'overview':
            return a1_overview(subgrids)
        case 'a2' | 'sar':
            return a2_sar(spp_matrices, cast(Analysis2, analysis), lvl_info.sides, caps)
        case 'a3' | 'spdiff':
            return a3_species_delta(spp_matrices, lvl_info.dmats, cast(Analysis3, analysis))
        case 'a4' | 'rrich':
            return a4_avg_radius_richness(spp_matrices, lvl_info.dmats, cast(Analysis4, analysis))
        case 'a5' | 'oerich':
            return a5_observed_expected(spp_matrices)
        case 'a6' | 'sratios':
            return a6_shared_ratios(spp_matrices, lvl_info.dmats)
        case 'a7' | 'jaccard':
            return a7_jaccard_diss(spp_matrices, lvl_info.dmats)
        case 'a8' | 'abundance':
            return a8_abundance(subgrids)
        case _:
            raise InvalidLiteralError(f'{analysis.type_=}')


class TilingError(Exception):
    """Exception raised when request quadrat level doesn't fit the study grid.

    Attributes:
        level -- level being analyzed
        sides -- dimensions of the entire locality
    """

    def __init__(self, level: int, sides: Sides) -> None:
        super().__init__(f'Requested level {level} incompatible with locality dimensions: {sides.x} x {sides.y}')


def describe_full(df: pd.DataFrame) -> pd.DataFrame:
    stats = df.describe(percentiles=[0.025, 0.25, 0.5, 0.75, 0.975], include='all')
    stats.loc['median'] = df.median(numeric_only=True)
    stats.loc['sem'] = df.sem(numeric_only=True)
    stats.loc['skewness'] = df.skew(numeric_only=True)
    stats.loc['kurtosis'] = df.kurtosis(numeric_only=True)
    return stats


def a1_overview(subgrids: list[GridInfo]) -> tuple[pd.DataFrame, str]:
    """Return DataFrame containing number of unique species as well as number of individuals encountered in respective quadrats.

    Additional data contains per-level (and per-subgrid if applicable)
    descriptive statistics about encounters being processed.
    """
    res = []
    uniques = []
    res += ['====LEVEL OVERVIEW START====']
    for i, (enc, quadrats) in enumerate(subgrids):
        if len(subgrids) > 1:
            res += [f'===SUBGRID #{i} START===']
        desc = describe_full(enc)
        res += [desc.to_string()]

        by_qid = enc.groupby(['coord_x', 'coord_y'])
        unique = by_qid.species.nunique()
        # fill 0 for quadrats where nothing was encountered
        unique = unique.reindex(quadrats.index, fill_value=0).to_frame('n_species')
        if 'individuals' in enc.columns:
            unique['n_individuals'] = by_qid.individuals.sum()

        unique = unique.fillna(0)
        res += ['\n==Unique per quadrat==']
        res += [unique.to_string()]

        avg = unique / len(quadrats)
        res += [f'\n==Avg per quadrat==\n{avg.to_string()}']

        indist_mask = enc.species.str.endswith(' sp.', na=True)
        indist_enc = indist_mask.sum()
        res += ['\n==Indistinguishable encounters #==']
        res += [f'{indist_enc}']
        res += ['\n==Indistinguishable encounters %==']
        res += [f'{100 * indist_enc / (indist_enc + len(enc.index))}']

        if 'individuals' in enc.columns:
            indist_individuals = enc[indist_mask].individuals.sum()
            res += ['\n==Indistinguishable individuals #==']
            res += [f'{indist_individuals}']
            res += ['\n==Indistinguishable individuals %==']
            res += [f'{100 * indist_individuals / enc.individuals.sum()}']

        if 'direction' in enc.columns:
            res += ['\n==Direction richness difference==']
            dirdiff = direction_difference(enc).dropna()
            dirdiff['diff_abs#'] = dirdiff['diff_#'].abs()
            dirdiff = dirdiff.sort_values(by='diff_abs#', ascending=False)
            res += [describe_full(dirdiff).to_string(), '\n']
            res += [dirdiff.to_string()]

        if len(subgrids) > 1:
            res += [f'===SUBGRID #{i} END===\n']

        unique = unique.reset_index(drop=False)
        uniques.append(unique)
    res += ['====LEVEL OVERVIEW END====\n\n']
    unique_avg = pd.concat(uniques, ignore_index=True).groupby(['coord_x', 'coord_y']).mean().convert_dtypes()
    unique_avg = unique_avg.assign(
        coord_x=quadrats.index.get_level_values('coord_x'), coord_y=quadrats.index.get_level_values('coord_y')
    )
    return (unique_avg, '\n'.join(res))


def a2_sar(
    spp_matrices: list[pd.DataFrame], analysis: Analysis2, sides_adj: Sides, caps: Caps
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return DataFrame containing quadrat richness accumulations.

    The accumulations are performed in random order and
    separate columns are added for slowest and fastest growing series
    and total accumulated area.
    """
    accumulated = []
    for spp_matrix in spp_matrices:
        for _ in range(analysis.permutations):
            shuff = acc_richness_shuffled(spp_matrix)
            accumulated.append(shuff)
    sar = pd.DataFrame(accumulated).transpose()
    sar_add = agg_results(sar, 'n_species', 'area')

    min_acc = sar[0].to_list()
    max_acc = sar[0].to_list()
    for colname in sar:
        col = sar[colname].to_list()
        if col < min_acc:
            min_acc = col
        if col > max_acc:
            max_acc = col
    sar['min_acc'] = min_acc
    sar['max_acc'] = max_acc

    surface_area = sides_adj.x * sides_adj.y
    sar['area'] = np.minimum((sar.index + 1) * surface_area, caps['total_area'])
    sar_add['area'] = sar['area']
    return sar, sar_add


def a3_species_delta(
    spp_matrices: list[SppMatrix], dmats: list[pd.DataFrame], analysis: Analysis3
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return DataFrame containing distance-dependent species difference.

    Absolute difference between species lists is calculated
    for each pair of quadrats of given distance. This is done with all possible
    pairs of quadrats of given level.

    For relative comparison see `a7_jaccard_diss`.
    """
    deltas_list = []
    for richness, dmat in zip(spp_matrices, dmats, strict=True):
        sub_deltas = species_delta(richness, dmat)
        deltas_list.append(sub_deltas)
    deltas = pd.concat(deltas_list)
    deltas = deltas[deltas.distance > 0]

    deltas_stats = deltas.reset_index(drop=True)
    interval = analysis.interval
    if interval and not deltas.empty:
        bins = pd.interval_range(0, deltas.distance.max() + interval, freq=interval, closed='left')  # type: ignore[call-overload] # should accept numeric, but rejects float; pandas 2.2.0 bug?
        deltas['distance_bin'] = pd.cut(deltas.distance, bins)
        deltas_stats['distance'] = pd.cut(deltas_stats.distance, bins)
    deltas_stats = deltas_stats.groupby('distance', observed=False).agg(AGG_STATS)
    deltas_stats = flatten_multicolumns(deltas_stats).reset_index()
    return (deltas, deltas_stats)


def a4_avg_radius_richness(
    spp_matrices: list[pd.DataFrame], dmats: list[pd.DataFrame], analysis: Analysis4
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return DataFrame containing the sum of richness of quadrats orbiting a select as a point of origin.

    This is done for every quadrat in a grid for every distance bin.
    Additional data is returned as an aggregation of various statistics
    for said DataFrame.
    """
    radius_richness_lst = []
    step = analysis.radius_step
    for spp_matrix, dmat_exact in zip(spp_matrices, dmats, strict=True):
        radius_bins = pd.interval_range(0, dmat_exact.distance.max() + step, freq=step, closed='left')  # type: ignore[call-overload] # freq should accept float, pd or mypy err
        dmat = dmat_exact.assign(distance=pd.cut(dmat_exact.distance, radius_bins)).dropna()
        dmat_groups = dmat.groupby(['coord_x', 'coord_y', 'distance'], observed=False)

        def rpd(df: pd.DataFrame) -> int:
            return total_radius_richness(df, spp_matrix)  # noqa: B023    # spp_matrix changing value is desirable

        radius_richness = dmat_groups.agg(rpd)
        radius_richness_lst.append(radius_richness)
    radius_richness = (
        pd.concat(radius_richness_lst).reset_index().rename({0: 'radius_richness'}, errors='raise', axis='columns')
    )
    stats = (
        radius_richness.drop(['coord_x', 'coord_y'], axis='columns', errors='raise')
        .groupby(by='distance', observed=False)
        .agg(AGG_STATS)
    )
    stats = flatten_multicolumns(stats).reset_index()
    return (radius_richness, stats)


def a5_observed_expected(spp_matrices: list[SppMatrix]) -> tuple[pd.DataFrame, None]:
    """Return DataFrame containing observed and expected species occurrences in a given list of subgrids."""
    oe_ratios = []
    for spp_matrix in spp_matrices:
        species_in_n_quadrats = spp_matrix.sum(axis='index')
        n_quadrats = len(spp_matrix)
        observed_ratio = species_in_n_quadrats / n_quadrats
        expected_var = (observed_ratio * (1 - observed_ratio)).sum()
        q_richnesses = spp_matrix.sum(axis='columns')
        oe_ratio = q_richnesses / expected_var
        oe_ratios.append(pd.DataFrame({'oe_ratio': oe_ratio}))
    oe_ratios = pd.concat(oe_ratios, axis='columns')
    oe_ratios = pd.DataFrame(
        {'oe_ratio_mean': oe_ratios.mean(axis='columns'), 'oe_ratio_med': oe_ratios.median(axis='columns')}
    )
    return oe_ratios, None


def a6_shared_ratios(spp_matrices: list[SppMatrix], dmats: list[pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return DataFrame containing various ratios of quadrat spp. intersection with regards to distance.

    Specifically spp. intersection vs
    species total, vs. union of species and between total richness of quadrats in the entire subgrid.

    Additional data is returned as an aggregation of various statistics
    for said DataFrame.
    """
    res: dict[str, list['pd.Series[float]']] = {
        'common_diff': [],
        'common_total': [],
        'common_union': [],
        'distance': [],
    }
    for spp_matrix, dmat in zip(spp_matrices, dmats, strict=True):
        spp_grid_total = len(spp_matrix.columns)
        for idx, row in spp_matrix.iterrows():
            n_intersect = (spp_matrix & row).sum(axis='columns')
            n_xor = (spp_matrix ^ row).sum(axis='columns')
            n_union = (spp_matrix | row).sum(axis='columns')

            res['common_diff'].append(n_intersect / n_xor)
            res['common_total'].append(n_intersect / spp_grid_total)
            res['common_union'].append(n_intersect / n_union)
            res['distance'].append(dmat.loc[idx, 'distance'])  # type: ignore[arg-type, index]   # is truly pd.Series, can be indexed by MultiIndex tuple just fine
    res = {k: pd.concat(v) for k, v in res.items()}
    ratios = pd.DataFrame(res)
    ratios = ratios[ratios.distance > 0]
    with np.errstate(invalid='ignore'):  # inf-inf may occur since values above may be inf
        ratios_stats = ratios.groupby('distance').agg(AGG_STATS)
    ratios_stats = flatten_multicolumns(ratios_stats).reset_index()
    return ratios, ratios_stats


def a7_jaccard_diss(spp_matrices: list[pd.DataFrame], dmats: list[pd.DataFrame]) -> tuple[pd.DataFrame, None]:
    """Return DataFrame containing Jaccard dissimilarity analysis for quadrats in respective distances."""
    jaccards_list = []
    for spp_matrix, dmat in zip(spp_matrices, dmats, strict=True):
        jaccards_list.append(jaccard_dissimilatity(spp_matrix, dmat))
    list_of_jaccard_lists = pd.concat(jaccards_list)
    return list_of_jaccard_lists, None


def a8_abundance(subgrids: list[GridInfo]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return DataFrame containing equitability of abundance and species abundance distribution data.

    Theoretical species richness as per Preston, F. W. (1948). "The Commonness, and Rarity, of Species",
    doi:10.2307/1930989, p. 257 is returned as additional data.
    """
    enc = subgrids[0].enc  # disregard subgrids as they are most likely to be removed
    spp_totals = enc[['individuals', 'species']].groupby('species', as_index=False).sum()

    # formulas and curves explained in the paper in docs or at
    # https://en.wikipedia.org/wiki/Relative_species_abundance#Calculating_theoretical_species_richness
    bins_scalars = geom_r2(1, spp_totals.individuals.max())
    spp_totals['individuals_bin'] = pd.cut(spp_totals.individuals, bins_scalars, right=False)
    ns = spp_totals[['individuals_bin', 'species']].groupby('individuals_bin', observed=False).count()
    ns['bin_position'] = range(len(ns))
    n0_bin = ns['species'].idxmax()  # the modal bin
    n0_position = ns.at[n0_bin, 'bin_position']
    n0 = ns.at[n0_bin, 'species']  # number of spp in the modal bin
    Rs = (ns['bin_position'] - n0_position).abs()  # noqa: N806 # consistency with literature, distances to modal bin

    def gauss_curve(R: 'pd.Series[int]', a: int) -> 'pd.Series[float]':  # noqa: N803 # same as above
        return cast('pd.Series[float]', n0 * np.exp(-((a * R) ** 2)))

    try:
        a = optimize.curve_fit(gauss_curve, Rs, ns['species'], nan_policy='raise')[0][0]
    except RuntimeError:
        a = math.nan
    spp_theoretical = n0 * math.sqrt(math.pi) / a  # N in formulas above
    spp_sampled = len(spp_totals)
    add = pd.DataFrame(
        {
            'theoretical_richness': [spp_theoretical],
            'sampled_richness': [spp_sampled],
            'hidden_species': [spp_theoretical - spp_sampled],
            'sampled_%': [100 * spp_sampled / spp_theoretical],
        }
    )

    # prevent pandas.errors.IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer during pd.concat()
    # pandas bug as of 2.2.1?
    spp_totals['individuals_bin'] = spp_totals['individuals_bin'].astype(str)
    return spp_totals, add


def jaccard_dissimilatity(spp_matrix: pd.DataFrame, dmat: pd.DataFrame) -> pd.DataFrame:
    """Return Jaccard dissimilarity for respective distances in a DataFrame.

    >>> spp_idx = pd.MultiIndex.from_arrays([[0, 0, 1], [0, 1, 0]], names=('coord_x', 'coord_y'))
    >>> spp_matrix = pd.DataFrame(
    ...     index=spp_idx,
    ...     data={
    ...         'A': [True, True, False],
    ...         'B': [True, False, False],
    ...         'C': [True, False, False],
    ...         'D': [False, True, False],
    ...     },
    ... )
    >>> idx = pd.MultiIndex.from_tuples(
    ...     [
    ...         (0, 0, 0, 0),
    ...         (0, 0, 0, 1),
    ...         (0, 0, 1, 0),
    ...         (0, 1, 0, 0),
    ...         (0, 1, 0, 1),
    ...         (0, 1, 1, 0),
    ...         (1, 0, 0, 0),
    ...         (1, 0, 0, 1),
    ...         (1, 0, 1, 0),
    ...     ],
    ...     names=['coord_x', 'coord_y', 'coord_x_other', 'coord_y_other'],
    ... )
    >>> dmat = pd.DataFrame(index=idx, data={'distance': [0, 1, 1, 1, 0, 2, 1, 2, 0]})
    >>> jaccard_dissimilatity(spp_matrix, dmat)
       jaccard_dissimilarity  log_jaccard_dissimilarity  distance
    1                   0.75                  -0.124939         1
    2                   1.00                   0.000000         1
    3                   0.75                  -0.124939         1
    5                   1.00                   0.000000         2
    6                   1.00                   0.000000         1
    7                   1.00                   0.000000         2
    """
    jacc_diss = []
    dists = []
    for idx, row in spp_matrix.iterrows():
        n_intersect = (spp_matrix & row).sum(axis='columns')
        n_unique_a = (spp_matrix & ~row).sum(axis='columns')
        n_unique_b = (~spp_matrix & row).sum(axis='columns')

        divisor = n_intersect + n_unique_a + n_unique_b
        jd = 1 - (n_intersect / divisor)

        jacc_diss.append(jd)
        dists.append(dmat.loc[idx, 'distance'])  # type: ignore[index]   # can be indexed by MultiIndex tuple just fine
    jd_series = pd.concat(jacc_diss, ignore_index=True)  #
    with np.errstate(divide='ignore'):  # J.d. may be 0 for 2 quadrats with same species, results in NaN
        log_jd = np.log10(jd_series)
    res = pd.DataFrame(
        {
            'jaccard_dissimilarity': jd_series,
            'log_jaccard_dissimilarity': log_jd,
            'distance': pd.concat(dists, ignore_index=True),
        }
    )
    res = res[res.distance > 0]
    return res


def adjust_grid(gri: GridInfo, cfg: conf.Config) -> tuple[GridInfo, Sides, Caps]:
    sides = cfg.locality.sides
    caps = compute_caps(gri.qlist, sides)
    gri.qlist = add_quadrat_centroids(gri.qlist, sides)
    gri_adj, sides_adj = discard_axes(
        gri, sides, discard_transect=cfg.discard_transect_info, discard_zone=cfg.discard_zone_info
    )
    sides_adj = Sides(sides_adj.x, sides_adj.y)
    return (gri_adj, sides_adj, caps)


def adjust_for_lvl(
    gri: GridInfo, lvl: int, max_lvl: int, lvl_strat: LevelStrategy, sides: Sides
) -> tuple[list[GridInfo], Sides]:
    """Transform study grid according to current level and level strategy.

    Returns `list[GridInfo]` because 'overlaid-subgrids' level strategy averages multiple subgrids.
    """
    enc, quadrats = gri
    if lvl_strat == 'transect-additive':
        res = adjust_transect_additive(enc, quadrats, sides, lvl)
    elif lvl_strat == 'zone-additive':
        res = adjust_zone_additive(enc, quadrats, sides, lvl)
    elif lvl_strat == 'overlaid-subgrids':
        enc_subgrids, q_subgrids, sides_adj = adjust_overlaid_subgrids(enc, quadrats, sides, lvl)
        subgrids = [GridInfo(e, q) for e, q in zip(enc_subgrids, q_subgrids, strict=True)]
    elif lvl_strat == 'transect-merging':
        res = adjust_transect_merging(enc, quadrats, sides, lvl)
    elif lvl_strat == 'zone-merging':
        res = adjust_zone_merging(enc, quadrats, sides, lvl)
    elif lvl_strat == 'repeated-transect-merging':
        res = adjust_repeated_transect_merging(enc, quadrats, sides, lvl)
    elif lvl_strat == 'striped-transect-merging':
        res = adjust_striped_transect_merging(enc, quadrats, sides, lvl, max_lvl)
    elif lvl_strat == 'nested-quadrats':
        res = adjust_nested_quadrats(enc, quadrats, sides, lvl, max_lvl)
    else:
        raise conf.InvalidTaskError(lvl_strat)

    if lvl_strat != 'overlaid-subgrids':
        subgrids = [GridInfo(res[0], res[1])]  # type: ignore[possibly-undefined] # is defined for any other option
        sides_adj = res[2]

    for grid in subgrids:  # type: ignore[possibly-undefined] # guaranteed to be defined by two ifs above
        check_grid_consistency(grid)

    return (subgrids, sides_adj)  # type: ignore[possibly-undefined] # guaranteed to be defined by two ifs above


def check_grid_consistency(grinfo: GridInfo, *, post_adj: bool = False) -> None:
    enc, quadrats = grinfo
    enc.set_flags(allows_duplicate_labels=False)
    quadrats.set_flags(allows_duplicate_labels=False)
    qids_enc = set(zip(enc.coord_x, enc.coord_y, strict=False))
    qids_qlist = set(
        zip(quadrats.index.get_level_values('coord_x'), quadrats.index.get_level_values('coord_y'), strict=False)
    )
    qids_diff = qids_enc - qids_qlist
    if len(qids_diff) > 0:
        raise InvalidQuadratsError(qids_diff, post_adj=post_adj)
    if quadrats.isna().any().any():
        raise MissingValuesError(quadrats[quadrats.isna().any(axis='columns')], post_adj=post_adj)
    enc_subset = enc[['species', 'coord_x', 'coord_y']]
    if enc_subset.isna().any().any():
        raise MissingValuesError(enc_subset[enc_subset.isna().any(axis='columns')], post_adj=post_adj)


def adjust_transect_additive(
    enc: Encounters, qlist: QList, sides: Sides, level: int
) -> tuple[Encounters, QList, Sides]:
    """Adjust passed encounters, quadrat list and sides for transect-additive strategy at given `level`.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 3],
    ...         'coord_y': [0, 0, 1, 0, 3],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 2, 3], [0, 1, 0, 1, 0, 3]], names=('coord_x', 'coord_y')),
    ...     data={'centroid_x': [2, 2, 6, 6, 10, 14], 'centroid_y': [2, 6, 2, 6, 2, 14]},
    ... )
    >>> sides = Sides(4, 4)
    >>> res = adjust_transect_additive(enc, qlist, sides, level=2)
    >>> res[0]
       coord_x  coord_y species
    0        0        0       B
    1        1        0       A
    2        1        1       A
    3        1        0       C
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0                 2           2
            1                 2           6
    1       0                 6           2
            1                 6           6
    >>> res[2]
    Sides(x=4.0, y=4.0)
    """
    enc = enc[enc.coord_x < level]
    idx = pd.IndexSlice
    qlist = qlist.loc[idx[0 : level - 1, :], :]
    return enc, qlist, sides


def adjust_zone_additive(enc: Encounters, qlist: QList, sides: Sides, level: int) -> tuple[Encounters, QList, Sides]:
    """Adjust passed encounters, quadrat list and sides for zone-additive strategy at given `level`.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 3],
    ...         'coord_y': [0, 0, 1, 0, 3],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 2, 3], [0, 1, 0, 1, 0, 3]], names=('coord_x', 'coord_y')),
    ...     data={'centroid_x': [2, 2, 6, 6, 10, 14], 'centroid_y': [2, 6, 2, 6, 2, 14]},
    ... )
    >>> sides = Sides(4, 4)
    >>> res = adjust_zone_additive(enc, qlist, sides, level=1)
    >>> res[0]
       coord_x  coord_y species
    0        0        0       B
    1        1        0       A
    3        1        0       C
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0                 2           2
    1       0                 6           2
    2       0                10           2
    >>> res[2]
    Sides(x=4.0, y=4.0)
    """
    enc = enc[enc.coord_y < level]
    idx = pd.IndexSlice
    qlist = qlist.loc[idx[:, 0 : level - 1], :]
    return enc, qlist, sides


def adjust_transect_merging(enc: Encounters, qlist: QList, sides: Sides, level: int) -> tuple[Encounters, QList, Sides]:
    """Adjust passed encounters, quadrat list and sides for transect-merging strategy at given `level`.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 3],
    ...         'coord_y': [0, 0, 1, 2, 3],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 1, 3], [0, 1, 0, 1, 2, 3]], names=('coord_x', 'coord_y')),
    ...     data={'centroid_x': [2, 2, 6, 6, 10, 14], 'centroid_y': [2, 6, 2, 6, 10, 14]},
    ... )
    >>> sides = Sides(4, 4)
    >>> res = adjust_transect_merging(enc, qlist, sides, level=3)
    >>> res[0]
       coord_x  coord_y species
    0        0        0       B
    1        0        0       A
    2        0        1       A
    3        0        2       C
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0                 6           2
            1                 6           6
            2                 6          10
    >>> res[2]
    Sides(x=12.0, y=4.0)
    """
    enc = enc[enc.coord_x < level]
    enc.loc[:, 'coord_x'] = 0

    idx = pd.IndexSlice
    qlist = qlist.loc[idx[0 : level - 1, :], :]
    new_idx = pd.MultiIndex.from_arrays(
        [[0] * len(qlist), qlist.index.get_level_values('coord_y')], names=['coord_x', 'coord_y']
    )
    qlist = qlist.set_index(new_idx)
    qlist = qlist[~qlist.index.duplicated()]
    qlist.loc[:, 'centroid_x'] = (sides.x * level) / 2
    qlist = qlist.drop_duplicates()

    return enc, qlist, Sides(sides.x * level, sides.y)


def adjust_zone_merging(enc: Encounters, qlist: QList, sides: Sides, level: int) -> tuple[Encounters, QList, Sides]:
    """Adjust passed encounters, quadrat list and sides for zone-merging strategy at given `level`.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 3],
    ...         'coord_y': [0, 0, 1, 2, 3],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 1, 3], [0, 1, 0, 1, 2, 3]], names=('coord_x', 'coord_y')),
    ...     data={'centroid_x': [2, 2, 6, 6, 10, 14], 'centroid_y': [2, 6, 2, 6, 10, 14]},
    ... )
    >>> sides = Sides(4, 4)
    >>> res = adjust_zone_merging(enc, qlist, sides, level=3)
    >>> res[0]
       coord_x  coord_y species
    0        0        0       B
    1        1        0       A
    2        1        0       A
    3        1        0       C
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0                 2           6
    1       0                 6           6
    >>> res[2]
    Sides(x=4.0, y=12.0)
    """
    enc = enc[enc.coord_y < level]
    enc.loc[:, 'coord_y'] = 0

    idx = pd.IndexSlice
    qlist = qlist.loc[idx[:, 0 : level - 1], :]
    new_idx = pd.MultiIndex.from_arrays(
        [qlist.index.get_level_values('coord_x'), [0] * len(qlist)], names=['coord_x', 'coord_y']
    )
    qlist = qlist.set_index(new_idx)
    qlist = qlist[~qlist.index.duplicated()]
    qlist.loc[:, 'centroid_y'] = (sides.y * level) / 2

    return enc, qlist, Sides(sides.x, sides.y * level)


def adjust_overlaid_subgrids(
    enc: Encounters, qlist: QList, sides: Sides, level: int
) -> tuple[list[Encounters], list[QList], Sides]:
    """Adjust passed encounters, quadrat list and sides for overlaid-subgrids strategy at given `level`.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 3],
    ...         'coord_y': [0, 0, 1, 2, 3],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 1, 3], [0, 1, 0, 1, 2, 3]], names=('coord_x', 'coord_y')),
    ...     data={'centroid_x': [2, 2, 6, 6, 10, 14], 'centroid_y': [2, 6, 2, 6, 10, 14]},
    ... )
    >>> sides = Sides(4, 4)
    >>> res = adjust_overlaid_subgrids(enc, qlist, sides, level=1)
    >>> res[0]
    [   coord_x  coord_y species
    0        0        0       B
    1        1        0       A
    2        1        1       A
    3        1        2       C
    4        3        3       B]
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
    [                 centroid_x  centroid_y
    coord_x coord_y
    0       0                 2           2
            1                 2           6
    1       0                 6           2
            1                 6           6
            2                10          10
    3       3                14          14]
    >>> res[2]
    Sides(x=4.0, y=4.0)
    >>> res = adjust_overlaid_subgrids(enc, qlist, sides, level=2)
    >>> res[0]
    [   coord_x  coord_y species
    0        0        0       B
    1        0        0       A
    2        0        0       A
    3        0        1       C
    4        1        1       B]
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
    [                 centroid_x  centroid_y
    coord_x coord_y
    0       0                 4           4
            1                 4           8
    1       1                 8           8]
    >>> res[2]
    Sides(x=8.0, y=8.0)
    """
    qlist['coord_x'] = qlist.index.get_level_values('coord_x')
    qlist['coord_y'] = qlist.index.get_level_values('coord_y')
    cutoffs = cutting_bounds(qlist, level)
    q_subgrids = create_subgrids(qlist, cutoffs)
    shift_tuples = get_shift_tuples(q_subgrids)
    q_subgrids = shift_coords(q_subgrids, shift_tuples, level)

    enc_subgrids = create_subgrids(enc, cutoffs)
    enc_subgrids = shift_coords(enc_subgrids, shift_tuples, level)

    for q_subgrid in q_subgrids:
        q_subgrid.loc[:, 'centroid_x'] = qlist['centroid_x'] + ((sides.x / 2) * (level - 1))
        q_subgrid.loc[:, 'centroid_y'] = qlist['centroid_y'] + ((sides.y / 2) * (level - 1))
        q_subgrid.drop(columns=['coord_x', 'coord_y'], inplace=True)  # noqa: PD002

    return enc_subgrids, q_subgrids, Sides(sides.x * level, sides.y * level)


def adjust_repeated_transect_merging(
    enc: Encounters, qlist: QList, sides: Sides, level: int
) -> tuple[Encounters, QList, Sides]:
    """Adjust passed encounters, quadrat list and sides for striped-transect-merging strategy at given `level`.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 3],
    ...         'coord_y': [0, 0, 1, 2, 3],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 1, 3], [0, 1, 0, 1, 2, 3]], names=('coord_x', 'coord_y')),
    ...     data={'centroid_x': [2, 2, 6, 6, 10, 14], 'centroid_y': [2, 6, 2, 6, 10, 14]},
    ... )
    >>> sides = Sides(4, 4)
    >>> res = adjust_repeated_transect_merging(enc, qlist, sides, level=2)
    >>> res[0]
       coord_x  coord_y species
    0        0        0       B
    1        0        0       A
    2        0        1       A
    3        0        2       C
    4        1        3       B
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0               6.0           2
            1               6.0           6
            2              14.0          10
    1       3              18.0          14
    >>> res[2]
    Sides(x=8.0, y=4.0)
    """
    new_xs = enc.coord_x.floordiv(level)
    enc.loc[:, 'coord_x'] = new_xs

    new_xs = qlist.index.get_level_values('coord_x').to_series().floordiv(level)
    new_idx = pd.MultiIndex.from_arrays([new_xs, qlist.index.get_level_values('coord_y')], names=('coord_x', 'coord_y'))
    qlist = qlist.set_index(new_idx)
    qlist = qlist[~qlist.index.duplicated()]
    qlist['centroid_x'] = qlist['centroid_x'] + ((sides.x / 2) * level)

    return enc, qlist, Sides(sides.x * level, sides.y)


def adjust_striped_transect_merging(
    enc: Encounters, qlist: QList, sides: Sides, level: int, max_level: int
) -> tuple[Encounters, QList, Sides]:
    """Adjust passed grid info list and sides for striped-transect-merging strategy at given `level` and `max_level`.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 3],
    ...         'coord_y': [0, 0, 1, 2, 3],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 1, 3], [0, 1, 0, 1, 2, 3]], names=('coord_x', 'coord_y')),
    ...     data={'centroid_x': [2, 2, 6, 6, 10, 14], 'centroid_y': [2, 6, 2, 6, 10, 14]},
    ... )
    >>> sides = Sides(4, 4)
    >>> res = adjust_striped_transect_merging(enc, qlist, sides, level=1, max_level=2)
    >>> res[0]
       coord_x  coord_y species
    0        0        0       B
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0               4.0           2
            1               4.0           6
    >>> res[2]
    Sides(x=4.0, y=4.0)
    """
    enc = enc[(enc.coord_x % max_level) < level]
    new_xs = enc.coord_x.floordiv(max_level)
    enc.loc[:, 'coord_x'] = new_xs

    q_xs = qlist.index.get_level_values('coord_x')
    qlist = qlist[(q_xs % max_level) < level]
    q_xs = qlist.index.get_level_values('coord_x')
    new_xs = q_xs.to_series().floordiv(max_level)
    new_idx = pd.MultiIndex.from_arrays([new_xs, qlist.index.get_level_values('coord_y')], names=('coord_x', 'coord_y'))
    qlist = qlist.set_index(new_idx)

    qlist = qlist[~qlist.index.duplicated()]

    qlist['centroid_x'] = qlist['centroid_x'] + ((sides.x / 2) * level)

    return enc, qlist, Sides(sides.x * level, sides.y)


def adjust_nested_quadrats(
    enc: Encounters, qlist: QList, sides: Sides, level: int, max_level: int
) -> tuple[Encounters, QList, Sides]:
    """Adjust passed grid information for striped-transect-merging strategy at given `level` and `max_level`.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 3],
    ...         'coord_y': [0, 0, 1, 2, 3],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 1, 3], [0, 1, 0, 1, 2, 3]], names=('coord_x', 'coord_y')),
    ...     data={'centroid_x': [2, 2, 6, 6, 10, 14], 'centroid_y': [2, 6, 2, 6, 10, 14]},
    ... )
    >>> sides = Sides(4, 4)
    >>> res = adjust_nested_quadrats(enc, qlist, sides, level=1, max_level=2)
    >>> res[0]
       coord_x  coord_y species
    0        0        0       B
    >>> res[1]  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0               4.0         4.0
    >>> res[2]
    Sides(x=4.0, y=4.0)
    """
    merge_n_quadrats = 2 ** (level - 1)
    retain_every_nth = 2 ** (max_level - level)

    new_xs = enc.coord_x.floordiv(merge_n_quadrats)
    new_ys = enc.coord_y.floordiv(merge_n_quadrats)
    enc = enc.assign(coord_x=new_xs, coord_y=new_ys)
    keep_x = (enc.coord_x % retain_every_nth) == 0
    keep_y = (enc.coord_y % retain_every_nth) == 0
    enc = enc[keep_x & keep_y]

    qlist['coord_x'] = qlist.index.get_level_values('coord_x')
    qlist['coord_y'] = qlist.index.get_level_values('coord_y')

    new_xs = qlist.coord_x.floordiv(merge_n_quadrats)
    new_ys = qlist.coord_y.floordiv(merge_n_quadrats)
    qlist = qlist.assign(coord_x=new_xs, coord_y=new_ys)
    qlist = qlist.drop_duplicates(subset=['coord_x', 'coord_y'])

    keep_x = (qlist.coord_x % retain_every_nth) == 0
    keep_y = (qlist.coord_y % retain_every_nth) == 0
    qlist = qlist[keep_x & keep_y]

    qlist = qlist.set_index(['coord_x', 'coord_y'], drop=True, verify_integrity=True)

    qlist['centroid_x'] = qlist['centroid_x'] + ((sides.x / 2) * merge_n_quadrats)
    qlist['centroid_y'] = qlist['centroid_y'] + ((sides.y / 2) * merge_n_quadrats)

    return enc, qlist, Sides(sides.x * merge_n_quadrats, sides.y * merge_n_quadrats)


def add_quadrat_centroids(quadrats: pd.DataFrame, sides: Sides) -> pd.DataFrame:
    """Add centroid_x and centroid_y columns to *quadrats* with coordinates of quadrats' centroids.

    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 2], [0, 1, 0, 1, 0]], names=('coord_x', 'coord_y'))
    ... )
    >>> add_quadrat_centroids(qlist, Sides(1, 2))  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0               0.5         1.0
            1               0.5         3.0
    1       0               1.5         1.0
            1               1.5         3.0
    2       0               2.5         1.0
    """
    quadrats['centroid_x'] = (quadrats.index.get_level_values('coord_x') * sides.x) + (sides.x / 2)
    quadrats['centroid_y'] = (quadrats.index.get_level_values('coord_y') * sides.y) + (sides.y / 2)
    return quadrats


def compute_caps(quadrats: QList, sides: Sides) -> Caps:
    """Compute and return maximum possible area or distance in a study grid.

    This is necessary because some grid transformations, e.g. involving
    quadrat merging, could result in the grid seeming larger for a
    given level.
    Does not take grid irregularities, like nonsampled shallows, into account.

    >>> qlist = pd.DataFrame(
    ...     index=pd.MultiIndex.from_arrays([[0, 0, 1, 1, 2], [0, 1, 0, 1, 0]], names=('coord_x', 'coord_y'))
    ... )
    >>> compute_caps(qlist, Sides(1, 2))
    {'total_area': 12.0, 'max1dx': 3.0, 'max1dy': 4.0, 'diagonal': 5.0, 'centroid': 2.8284271247461903}
    """
    x_max = quadrats.index.get_level_values('coord_x').max()
    y_max = quadrats.index.get_level_values('coord_y').max()
    max1dx = (1 + x_max) * sides.x
    max1dy = (1 + y_max) * sides.y
    total_area = max1dx * max1dy
    diagonal = math.sqrt(max1dx**2 + max1dy**2)
    centroid_diff = {'x': max1dx - sides.x, 'y': max1dy - sides.y}
    centroid = math.sqrt(centroid_diff['x'] ** 2 + centroid_diff['y'] ** 2)
    return {'total_area': total_area, 'max1dx': max1dx, 'max1dy': max1dy, 'diagonal': diagonal, 'centroid': centroid}


def get_lvl_infos(grinfo: GridInfo, sides_adj: Sides, caps: Caps, cfg: conf.Config) -> dict[int, LevelInfo]:
    infos = {}
    for level in sorted(set(cfg.levels)):
        subgrids, sides_adj_lvl = adjust_for_lvl(
            grinfo,
            level,
            max(cfg.levels),
            cfg.level_strategy,
            sides_adj,
        )
        capped_dist_fn = get_distance_function(cfg.distance_type, sides_adj_lvl, caps)
        dmats = [distance_matrix(gri.qlist, capped_dist_fn) for gri in subgrids]
        infos[level] = copy.deepcopy(LevelInfo(subgrids, dmats, sides_adj_lvl))
    return infos


def save_results(
    args: argparse.Namespace,
    out_dir: Path,
    completed: list[pd.DataFrame],
    additional: list[str | pd.DataFrame | None],
    analysis_info: tuple[str, int],
) -> None:
    """Save analysis results in `completed` and additional data in `additional` to `out_dir`.

    `out_dir` must be created beforehand.
    """
    a_type, a_idx = analysis_info
    out_file = analysis_results_filename(out_dir, args.taskfile, a_type, a_idx)
    pd.concat(completed).to_csv(out_file, index=False)
    print(f'Result written to {out_file}')

    additional = list(filter(lambda x: x is not None, additional))
    if not additional:
        return
    out_file = out_file.with_stem(f'{out_file.stem}-add')
    if isinstance(additional[0], pd.DataFrame):
        out_file = out_file.with_suffix('.csv')
        for lvl, adf in enumerate(additional):
            adf['level'] = lvl + 1  # type: ignore[index]
        with warnings.catch_warnings():
            warnings.simplefilter(action='ignore', category=FutureWarning)
            pd.concat(additional, ignore_index=True).to_csv(out_file, index=False)  # type: ignore[arg-type]
    else:
        out_file = out_file.with_suffix('.txt')
        out_file.write_text('\n'.join(additional))  # type: ignore[arg-type] # guaranteed list[str]
    print(f'Additional data written to {out_file}')


def total_radius_richness(dist_group: pd.DataFrame, spp_matrix: pd.DataFrame) -> int:
    """Return total richness in a given distance group.

    Assumes that distance group (radius) from a certain quadrat
    has already been created by previous grouping.

    >>> idx = pd.MultiIndex.from_arrays(
    ...     [[0, 0, 0, 0], [0, 0, 0, 0], [10, 10, 10, 10], [0, 0, 0, 0], [0, 1, 2, 3]],
    ...     names=('coord_x', 'coord_y', 'distance', 'coord_x_other', 'coord_y_other'),
    ... )
    >>> dist_group = pd.DataFrame(index=idx, data={})
    >>> spp_idx = pd.MultiIndex.from_arrays([[0, 0, 0, 0], [0, 1, 2, 3]], names=('coord_x', 'coord_y'))
    >>> spp_matrix = pd.DataFrame(
    ...     index=spp_idx,
    ...     data={
    ...         'A': [True, True, False, False],
    ...         'B': [True, False, False, False],
    ...         'C': [True, True, False, False],
    ...         'D': [False, False, False, False],
    ...         'E': [False, False, True, False],
    ...     },
    ... )
    >>> total_radius_richness(dist_group, spp_matrix)
    4
    """
    peri_idx = pd.MultiIndex.from_arrays(
        [dist_group.index.get_level_values('coord_x_other'), dist_group.index.get_level_values('coord_y_other')]
    )
    perimeter = spp_matrix.loc[peri_idx]
    perimeter_richness = cast(int, perimeter.cumsum().astype(bool).iloc[-1].sum())
    return perimeter_richness


def flatten_multicolumns(df: pd.DataFrame) -> pd.DataFrame:
    """Flatten and rename multicolumns in a DataFrame.

    >>> cols = pd.MultiIndex.from_tuples([('top', 'btm1'), ('top', 'btm2')])
    >>> multi = pd.DataFrame(data=[[0, 1], [2, 3]], columns=cols)
    >>> flatten_multicolumns(multi)
       top_btm1  top_btm2
    0         0         1
    1         2         3
    """
    df.columns = df.columns.to_flat_index()  # type: ignore[no-untyped-call] # is typed, mypy 1.9.0 bug?
    name_map = {col: f'{col[0]}_{col[1]}' for col in df.columns}
    df = df.rename(name_map, axis='columns', errors='raise')
    return df


def get_distance_function(dist_type: Distance, sides_adj: Sides, caps: Caps) -> DistFunction:
    """Return function to use for computing values in distance matrix.

    >>> sides = Sides(1, 1)
    >>> get_distance_function('diagonal', sides, None)  # doctest: +ELLIPSIS
    <function get_distance_function.<locals>.<lambda> at ...>
    >>> get_distance_function(':)', sides, None)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    seal.exceptions.InvalidLiteralError: argument dist_type=':)' is not a valid choice
    """
    if dist_type == 'centroid':
        return lambda ps, qs: q_distance_centroid(ps, qs, caps)
    if dist_type == 'max1d':
        return lambda ps, qs: q_distance_collapsed(ps, qs, sides_adj, caps)
    if dist_type == 'diagonal':
        return lambda ps, qs: q_distance_diagonal(ps, qs, sides_adj, caps)
    raise InvalidLiteralError(f'{dist_type=}')


def filter_encounters(enc: pd.DataFrame, cfg: conf.Config) -> pd.DataFrame:
    """Return encounters filtered according to criteria specified in `cfg`.

    Supported criteria are documented in 0-example-task.toml.
    """
    if cfg.locality.name:
        enc = enc[enc.locality == cfg.locality.name]
    if cfg.locality.from_:
        enc = enc[enc.date >= cfg.locality.from_]
    if cfg.locality.to:
        enc = enc[enc.date <= cfg.locality.to]

    if cfg.direction == 'richer':
        dirdiff = direction_difference(enc)
        enc = enc.join(dirdiff, on=['coord_x', 'coord_y'], validate='m:1')
        # drop if (forward_has_more_species) and (direction_is_b)
        enc = enc[~((enc['diff_#'] >= 0) & (enc.direction == 'b'))]
        enc = enc[~((enc['diff_#'] < 0) & (enc.direction == 'f'))]
        enc = enc.drop(['f_species', 'b_species', 'diff_%', 'diff_#'], axis='columns', errors='raise')
    elif cfg.direction[0] in {'backward', 'forward'}:
        enc = enc[enc.direction == cfg.direction[0]]

    if cfg.include_families:
        enc = enc[enc.family.isin(cfg.include_families)]
    elif cfg.exclude_families:
        enc = enc[~enc.family.isin(cfg.exclude_families)]
    if cfg.exclude_phases:
        enc = enc[~enc.phase.isin(cfg.exclude_phases)]
    if not cfg.include_tiny:
        enc = enc[enc.significant_size]

    if cfg.use_morph:
        # backup for analyses where orig values are needed for indistinguishables
        # currently only a1
        enc['species_orig'] = enc['species']
        enc['species'] = enc['morph']
    if cfg.discard_indistinguishable:
        indist_mask = enc.species.str.endswith(' sp.', na=True)
        enc = enc[~indist_mask]
    enc = enc.reset_index(drop=True)
    return enc


def discard_axes(gri: GridInfo, sides: Sides, *, discard_transect: bool, discard_zone: bool) -> tuple[GridInfo, Sides]:
    """Transform coordinates in DataFrames to reflect discarding transect and/or zone information if requested.

    >>> enc = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 1, 1, 1, 1],
    ...         'coord_y': [0, 0, 1, 0, 1],
    ...         'species': ['B', 'A', 'A', 'C', 'B'],
    ...     }
    ... )
    >>> idx = pd.MultiIndex.from_arrays([[0, 0, 1, 1, 2], [0, 1, 0, 1, 0]], names=('coord_x', 'coord_y'))
    >>> quadrats = pd.DataFrame(
    ...     index=idx,
    ...     data={
    ...         'centroid_x': [0.5, 0.5, 1.5, 1.5, 2.5],
    ...         'centroid_y': [0.5, 1.5, 0.5, 1.5, 0.5],
    ...     },
    ... )
    >>> gri = GridInfo(enc, quadrats)
    >>> sides = Sides(1, 1)
    >>> res = discard_axes(gri, sides, discard_transect=True, discard_zone=False)
    >>> res[0].enc
       coord_x  coord_y species
    0        0        0       B
    1        0        0       A
    2        0        1       A
    3        0        0       C
    4        0        1       B
    >>> res[0].qlist  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0               0.5         0.5
            1               0.5         1.5
    >>> res[1]
    Sides(x=3.0, y=1.0)

    >>> res = discard_axes(gri, sides, discard_transect=False, discard_zone=True)
    >>> res[0].enc
       coord_x  coord_y species
    0        0        0       B
    1        1        0       A
    2        1        0       A
    3        1        0       C
    4        1        0       B
    >>> res[0].qlist  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0               0.5         0.5
    1       0               1.5         0.5
    2       0               2.5         0.5
    >>> res[1]
    Sides(x=1.0, y=2.0)


    >>> res = discard_axes(gri, sides, discard_transect=True, discard_zone=True)
    >>> res[0].enc
       coord_x  coord_y species
    0        0        0       B
    1        0        0       A
    2        0        0       A
    3        0        0       C
    4        0        0       B
    >>> res[0].qlist  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0               0.5         0.5
    >>> res[1]
    Sides(x=3.0, y=2.0)


    >>> res = discard_axes(gri, sides, discard_transect=False, discard_zone=False)
    >>> res[0].enc
       coord_x  coord_y species
    0        0        0       B
    1        1        0       A
    2        1        1       A
    3        1        0       C
    4        1        1       B
    >>> res[0].qlist  # doctest: +NORMALIZE_WHITESPACE
                     centroid_x  centroid_y
    coord_x coord_y
    0       0               0.5         0.5
            1               0.5         1.5
    1       0               1.5         0.5
            1               1.5         1.5
    2       0               2.5         0.5
    >>> res[1]
    Sides(x=1.0, y=1.0)
    """
    enc, qlist = gri
    new_x = sides.x
    new_y = sides.y
    if discard_transect:
        enc['coord_x'] = 0
        x_coords = qlist.index.get_level_values('coord_x')
        new_x = sides.x * (x_coords.max() + 1)
        qlist['centroid_x'] = sides.x / 2
    if discard_zone:
        enc['coord_y'] = 0
        y_coords = qlist.index.get_level_values('coord_y')
        new_y = sides.y * (y_coords.max() + 1)
        qlist['centroid_y'] = sides.y / 2
    qlist = qlist.drop_duplicates()  # automatically adjusts index
    return GridInfo(enc, qlist), Sides(new_x, new_y)


def direction_difference(enc: Encounters) -> pd.DataFrame:
    """Return dataframe with absolute and relative differences in encountered species between sampling directions.

    Resulting DataFrame has (coord_x, coord_y) as index and columns 'f_species' and 'b_species'
    describing how many species were sampled in a given direction, including absolute and
    relative differences between the two.

    >>> df = pd.DataFrame(
    ...     {
    ...         'coord_x': ['0', '0', '0', '1', '1'],
    ...         'coord_y': ['0', '0', '0', '1', '1'],
    ...         'direction': ['f', 'f', 'b', 'f', 'b'],
    ...         'species': ['A', 'B', 'A', 'B', 'B'],
    ...     }
    ... )
    >>> direction_difference(df)  # doctest: +NORMALIZE_WHITESPACE
                     f_species  b_species  diff_%  diff_#
    coord_x coord_y
    0       0                2          1     0.5       1
    1       1                1          1     0.0       0
    """
    forward = enc[enc.direction == 'f'][['coord_x', 'coord_y', 'species']]
    backward = enc[enc.direction == 'b'][['coord_x', 'coord_y', 'species']]
    f_lens = (
        forward.groupby(['coord_x', 'coord_y'])
        .nunique()
        .rename({'species': 'f_species'}, axis='columns', errors='raise')
    )
    b_lens = (
        backward.groupby(['coord_x', 'coord_y'])
        .nunique()
        .rename({'species': 'b_species'}, axis='columns', errors='raise')
    )
    stats = f_lens.join(b_lens, how='outer')
    stats['diff_%'] = (stats['f_species'] - stats['b_species']) / stats['f_species']
    stats['diff_#'] = stats['f_species'] - stats['b_species']
    return stats


def load_quadrats(qlist: Path, quadrat_types: Sequence[QuadratType] | None) -> QList:
    """Load CSV dataset listing all quadrats in a grid from `qlist` filtered by `quadrat_types`."""
    qs = pd.read_csv(qlist, dtype=qlist_dtypes(), index_col=['coord_x', 'coord_y']).convert_dtypes()
    if quadrat_types:
        qs = qs[qs.quadrat_type.isin(quadrat_types)]
    qs = qs.drop(columns='quadrat_type', errors='ignore')
    qs = qs.sort_index()
    return qs


def generate_quadrat_list(enc: Encounters) -> QList:
    idx = pd.MultiIndex.from_frame(enc[['coord_x', 'coord_y']].drop_duplicates())
    return pd.DataFrame(index=idx)


def load_encounters(dataset: Path) -> Encounters:
    """Load CSV dataset with encounters from `dataset`."""
    dtype_dict = enc_dtypes()
    enc = pd.read_csv(dataset, dtype=dtype_dict).convert_dtypes()
    if 'date' in enc.columns:
        enc['date'] = pd.to_datetime(enc.date, format='ISO8601')
    enc.set_flags(allows_duplicate_labels=False)
    return enc


def get_spp_matrix(grinfo: GridInfo) -> SppMatrix:
    """Return DataFrame with species matrix for passed *grinfo*.

    The species matrix has MultiIndex coord_x, coord_y labels with quadrat coordinates
    and species as column names with bool values denoting whether species COL was encountered in quadrat LABEL.

    >>> enc = pd.DataFrame(
    ...     {'coord_x': [0, 1, 1, 1, 1], 'coord_y': [0, 0, 1, 0, 1], 'species': ['B', 'A', 'A', 'C', 'B']}
    ... )
    >>> idx = pd.MultiIndex.from_arrays([[0, 0, 1, 1, 2], [0, 1, 0, 1, 0]], names=('coord_x', 'coord_y'))
    >>> quadrats = pd.DataFrame(index=idx)
    >>> get_spp_matrix(GridInfo(enc, quadrats))  # doctest: +NORMALIZE_WHITESPACE
    species              A      B      C
    coord_x coord_y
    0       0        False   True  False
            1        False  False  False
    1       0         True  False   True
            1         True   True  False
    2       0        False  False  False
    """
    enc, quadrats = grinfo
    enccoords = [enc.coord_x, enc.coord_y]
    spp_matrix = pd.crosstab(enccoords, columns=enc.species, dropna=False)
    spp_matrix = spp_matrix.reindex(quadrats.index).fillna(0).astype(bool)
    spp_matrix = spp_matrix.sort_index()
    return spp_matrix


def p025(x: 'pd.Series[float]') -> float:
    """Return 0.25 quantile (25th percentile) of pandas Series."""
    return x.quantile(0.025)


def p975(x: 'pd.Series[float]') -> float:
    """Return 0.975 quantile (97.5th percentile) of pandas Series."""
    return x.quantile(0.975)


AGG_STATS: list[str | Callable[['pd.Series[float]'], float]] = [
    'mean',
    'median',
    'sem',
    'std',
    'count',
    'min',
    'max',
    'skew',
    p025,
    p975,
]
"""List with aggregation to be called at once for convenience."""


def acc_richness_shuffled(spp_matrix: pd.DataFrame) -> 'pd.Series[int]':
    """Return Series containing accumulated richness.

    Quadrats are accumulated in random order.

    >>> np.random.seed(0)
    >>> spp_matrix = pd.DataFrame(
    ...     {
    ...         'A': [True, False, True, False],
    ...         'B': [True, False, False, False],
    ...         'C': [True, True, False, False],
    ...         'D': [False, False, False, False],
    ...         'E': [False, False, True, False],
    ...     }
    ... )
    >>> acc_richness_shuffled(spp_matrix)
    0    2
    1    2
    2    3
    3    4
    dtype: int64
    """
    return (
        spp_matrix.sample(frac=1, ignore_index=True)  # reshuffle dataset
        .cumsum()
        .astype(bool)
        .sum(axis='columns')  # sum total species
    )


def agg_results(df: pd.DataFrame, col_prefix: str, index_name: str) -> pd.DataFrame:
    """Aggregate data from DataFrame in a wide format.

    >>> pd.set_option('display.width', None)
    >>> df = pd.DataFrame({'col1': [1, 0], 'col2': [2, 1], 'col3': [2, 2], 'col4': [1, 3]})
    >>> agg_results(df, 'col', 'idx')  # doctest: +NORMALIZE_WHITESPACE
         col_mean  col_med   col_sem   col_std  col_count  col_p025  col_p975  col_min  col_max  col_skew  col_kurtosis
    idx
    0         1.5      1.5  0.288675  0.577350          4     1.000     2.000        1        2       0.0          -6.0
    1         1.5      1.5  0.645497  1.290994          4     0.075     2.925        0        3       0.0          -1.2
    """
    res = pd.DataFrame(index=df.index)
    res.index.name = index_name
    res[f'{col_prefix}_mean'] = df.mean(axis='columns')
    res[f'{col_prefix}_med'] = df.median(axis='columns')
    res[f'{col_prefix}_sem'] = df.sem(axis='columns')
    res[f'{col_prefix}_std'] = df.std(axis='columns')
    res[f'{col_prefix}_count'] = df.count(axis='columns')
    res[f'{col_prefix}_p025'] = df.quantile(0.025, axis='columns')
    res[f'{col_prefix}_p975'] = df.quantile(0.975, axis='columns')
    res[f'{col_prefix}_min'] = df.min(axis='columns')
    res[f'{col_prefix}_max'] = df.max(axis='columns')
    res[f'{col_prefix}_skew'] = df.skew(axis='columns')
    res[f'{col_prefix}_kurtosis'] = df.kurtosis(axis='columns')
    return res


def species_delta(species: pd.DataFrame, dmat: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame containing absolute in quadrats richness.

    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> vals = [
    ...     [True, True, True, False, False],
    ...     [True, False, True, False, False],
    ...     [False, False, False, False, True],
    ... ]
    >>> idx_spp = pd.MultiIndex.from_tuples([(0, 0), (0, 1), (1, 0)])
    >>> spp_matrix = pd.DataFrame(index=idx_spp, data=vals, columns=cols)
    >>> idx = pd.MultiIndex.from_tuples(
    ...     [
    ...         (0, 0, 0, 0),
    ...         (0, 0, 0, 1),
    ...         (0, 0, 1, 0),
    ...         (0, 1, 0, 0),
    ...         (0, 1, 0, 1),
    ...         (0, 1, 1, 0),
    ...         (1, 0, 0, 0),
    ...         (1, 0, 0, 1),
    ...         (1, 0, 1, 0),
    ...     ],
    ...     names=['coord_x', 'coord_y', 'coord_x_other', 'coord_y_other'],
    ... )
    >>> dmat = pd.DataFrame(index=idx, data={'distance': [0, 1, 1, 1, 0, 2, 1, 2, 0]})
    >>> species_delta(spp_matrix, dmat)
         distance  abs_diff
    0 0         0         0
      1         1         0
    1 0         1         1
    0 0         1         1
      1         0         0
    1 0         2         1
    0 0         1         3
      1         2         2
    1 0         0         0

    >>> vals = [
    ...     [False, False, False, False, False],
    ...     [True, False, True, False, False],
    ...     [False, False, False, False, False],
    ... ]
    >>> spp_matrix = pd.DataFrame(index=idx_spp, data=vals, columns=cols)
    >>> species_delta(spp_matrix, dmat)
         distance  abs_diff
    0 0         0         0
      1         1         2
    1 0         1         0
    0 0         1         0
      1         0         0
    1 0         2         0
    0 0         1         0
      1         2         2
    1 0         0         0
    """
    spp_diff: dict[str, list['pd.Series[float]']] = {'distance': [], 'abs_diff': []}
    for idx, row in species.iterrows():
        abs_diffs = (species & ~row).sum(axis='columns')
        spp_diff['abs_diff'].append(abs_diffs)
        dists = dmat.loc[idx, 'distance']  # type: ignore[index]   # can be indexed by MultiIndex tuple just fine
        spp_diff['distance'].append(dists)  # type: ignore[arg-type]   # is Series, not DF, verified by assert
    res = pd.DataFrame(
        {
            'distance': pd.concat(spp_diff['distance']),
            'abs_diff': pd.concat(spp_diff['abs_diff']),
        }
    )
    return res


def distance_matrix(quadrats: pd.DataFrame, distance: DistFunction) -> pd.DataFrame:
    """Convert quadrat's grid coordinates to quadrat's centroid coordinates on a meters-based plane.

    >>> df = pd.DataFrame(
    ...     {
    ...         'coord_x': [0, 0, 1, 1],
    ...         'coord_y': [0, 1, 0, 1],
    ...         'centroid_x': [0.5, 0.5, 1.5, 1.5],
    ...         'centroid_y': [0.5, 1.5, 0.5, 1.5],
    ...     }
    ... )
    >>> distance_matrix(
    ...     df, lambda a, b: q_distance_diagonal(a, b, Sides(1, 1), {'diagonal': 10})
    ... )  # doctest: +NORMALIZE_WHITESPACE
                                                 distance
    coord_x coord_y coord_x_other coord_y_other
    0       0       0             0              0.000000
                                  1              2.236068
                    1             0              2.236068
                                  1              2.828427
            1       0             0              2.236068
                                  1              0.000000
                    1             0              2.828427
                                  1              2.236068
    1       0       0             0              2.236068
                                  1              2.828427
                    1             0              0.000000
                                  1              2.236068
            1       0             0              2.828427
                                  1              2.236068
                    1             0              2.236068
                                  1              0.000000
    """
    quadrats = quadrats.reset_index(drop=False)
    dmat = quadrats.join(quadrats, how='cross', rsuffix='_other')  # type: ignore[arg-type]     # pandas bug as of 2.0.3
    ps = dmat[['centroid_x', 'centroid_y']]
    qs = dmat[['centroid_x_other', 'centroid_y_other']]
    qs = qs.rename(columns={'centroid_x_other': 'centroid_x', 'centroid_y_other': 'centroid_y'}, errors='raise')
    dmat = dmat[['coord_x', 'coord_y', 'coord_x_other', 'coord_y_other']]
    dmat['distance'] = distance(ps, qs)
    dmat = dmat.set_index(['coord_x', 'coord_y', 'coord_x_other', 'coord_y_other'])
    dmat = dmat.sort_index()
    return dmat


def q_distance_centroid(q1: pd.DataFrame, q2: pd.DataFrame, caps: Caps) -> 'pd.Series[float]':
    """Return series of euclidean distance between centroids of quadrats at `q1` and `q2`.

    Distance is capped by `centroid` value from `caps`.

    Grid coords should be paired-up, e.g. using cross-join, beforehand.

    >>> q1 = pd.DataFrame(
    ...     {
    ...         'centroid_x': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    ...         'centroid_y': [0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5],
    ...     }
    ... )
    >>> q2 = pd.DataFrame(
    ...     {
    ...         'centroid_x': [0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5],
    ...         'centroid_y': [0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5],
    ...     }
    ... )
    >>> q_distance_centroid(q1, q2, {'centroid': 10})
    0     0.000000
    1     1.000000
    2     1.000000
    3     1.414214
    4     1.000000
    5     0.000000
    6     1.414214
    7     1.000000
    8     1.000000
    9     1.414214
    10    0.000000
    11    1.000000
    12    1.414214
    13    1.000000
    14    1.000000
    15    0.000000
    dtype: float64
    """
    dists = pd.Series(np.sqrt((q1.centroid_x - q2.centroid_x) ** 2 + (q1.centroid_y - q2.centroid_y) ** 2))
    dists = dists.where(dists <= caps['centroid'], caps['centroid'])
    return cast('pd.Series[float]', dists)


def q_distance_collapsed(q1: pd.DataFrame, q2: pd.DataFrame, sides: Sides, caps: Caps) -> 'pd.Series[float]':
    """Return series of farthest single direction side-to-side distances between dataframes of points at `q1` and `q2`.

    Extent as per P&W paper, longest distance on 1 axis, taking larger of x or y differences.
    Distance is capped by `max1dx` value from `caps` in case x distance is taken and `max1dy` in case of y.

    Correction is applied to result to make distance of quadrat to itself 0.

    Grid coords should be paired-up, e.g. using cross-join, beforehand.

    >>> q1 = pd.DataFrame(
    ...     {
    ...         'centroid_x': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    ...         'centroid_y': [0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5],
    ...     }
    ... )
    >>> q2 = pd.DataFrame(
    ...     {
    ...         'centroid_x': [0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5],
    ...         'centroid_y': [0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5],
    ...     }
    ... )
    >>> q_distance_collapsed(q1, q2, Sides(1, 1), {'max1dx': 10, 'max1dy': 10})
    0     0.0
    1     2.0
    2     2.0
    3     2.0
    4     2.0
    5     0.0
    6     2.0
    7     2.0
    8     2.0
    9     2.0
    10    0.0
    11    2.0
    12    2.0
    13    2.0
    14    2.0
    15    0.0
    Name: centroid_x, dtype: float64
    """
    x_diff = (q1.centroid_x - q2.centroid_x).abs()
    y_diff = (q1.centroid_y - q2.centroid_y).abs()
    x_diff[x_diff > 0] += sides.x
    y_diff[y_diff > 0] += sides.y
    x_diff = x_diff.where(x_diff <= caps['max1dx'], caps['max1dx'])
    y_diff = y_diff.where(y_diff <= caps['max1dy'], caps['max1dy'])
    dist = x_diff.where(x_diff > y_diff, y_diff)
    return cast('pd.Series[float]', dist)


def q_distance_diagonal(q1: pd.DataFrame, q2: pd.DataFrame, sides: Sides, caps: Caps) -> 'pd.Series[float]':
    """Return series of farthest corner-to-corner distances between quadrats in list `q1` and `q2`, row-wise.

    Distance is capped by `diagonal` value from `caps` to prevent
    overspilling from grid in case of merged quadrats.

    Quadrats should be paired-up beforehand, e.g. using cross join.

    >>> q1 = pd.DataFrame(
    ...     {
    ...         'centroid_x': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    ...         'centroid_y': [0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5],
    ...     }
    ... )
    >>> q2 = pd.DataFrame(
    ...     {
    ...         'centroid_x': [0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5],
    ...         'centroid_y': [0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5],
    ...     }
    ... )
    >>> q_distance_diagonal(q1, q2, Sides(1, 1), {'diagonal': 10})
    0     0.000000
    1     2.236068
    2     2.236068
    3     2.828427
    4     2.236068
    5     0.000000
    6     2.828427
    7     2.236068
    8     2.236068
    9     2.828427
    10    0.000000
    11    2.236068
    12    2.828427
    13    2.236068
    14    2.236068
    15    0.000000
    dtype: float64
    >>> q_distance_diagonal(q1, q2, Sides(1, 1), {'diagonal': 2.5})
    0     0.000000
    1     2.236068
    2     2.236068
    3     2.500000
    4     2.236068
    5     0.000000
    6     2.500000
    7     2.236068
    8     2.236068
    9     2.500000
    10    0.000000
    11    2.236068
    12    2.500000
    13    2.236068
    14    2.236068
    15    0.000000
    dtype: float64
    """
    # "push" centroids into opposite corners
    x_dist = (q1.centroid_x - q2.centroid_x).abs() + sides.x
    y_dist = (q1.centroid_y - q2.centroid_y).abs() + sides.y
    dists_pre_sqrt = cast('pd.Series[float]', pd.Series(x_dist**2 + y_dist**2))
    quadrat_diagonal_2 = sides.x**2 + sides.y**2
    dists_pre_sqrt[dists_pre_sqrt == quadrat_diagonal_2] = 0
    dists = cast('pd.Series[float]', np.sqrt(dists_pre_sqrt))
    dists = dists.where(dists <= caps['diagonal'], caps['diagonal'])
    return dists


def cutting_bounds(quadrats: pd.DataFrame, level: int) -> dict[Edge, int]:
    """Return minimum and maximum coordinates to be retained when tiling subgrid with level x level tiles.

    >>> idx = pd.MultiIndex.from_tuples(
    ...     [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)],
    ...     names=['coord_x', 'coord_y'],
    ... )
    >>> qs = pd.DataFrame(index=idx)
    >>> cutting_bounds(qs, 1)
    {'left': 0, 'bottom': 0, 'right': 3, 'top': 2}
    >>> cutting_bounds(qs, 2)
    {'left': 0, 'bottom': 1, 'right': 3, 'top': 1}
    >>> cutting_bounds(qs, 3)
    {'left': 1, 'bottom': 0, 'right': 2, 'top': 2}
    >>> cutting_bounds(qs, 4)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    TilingError: Requested level 4 incompatible with locality dimensions: 3 x 2
    """
    xmax = quadrats.index.get_level_values('coord_x').max()
    ymax = quadrats.index.get_level_values('coord_y').max()
    if (level > xmax + 1) or (level > ymax + 1):
        raise TilingError(level, Sides(xmax, ymax))
    xmin_cutoff = (xmax + 1) % level
    ymin_cutoff = (ymax + 1) % level
    xmax_cutoff = xmax - xmin_cutoff
    ymax_cutoff = ymax - ymin_cutoff
    return {'left': xmin_cutoff, 'bottom': ymin_cutoff, 'right': xmax_cutoff, 'top': ymax_cutoff}


def get_shift_tuples(qlist_subgrid: list[QList]) -> list[tuple[int, int]]:
    """Get a list containing offsets for adjusting grid coordinates so that they start at (0, 0).

    In other words, tuples with minimal coordinates on each axis.

    >>> df0 = pd.DataFrame(index=pd.MultiIndex.from_arrays([[0, 0, 1, 1], [0, 1, 0, 1]], names=('coord_x', 'coord_y')))
    >>> df1 = pd.DataFrame(index=pd.MultiIndex.from_arrays([[1, 1, 2, 2], [2, 3, 2, 3]], names=('coord_x', 'coord_y')))
    >>> get_shift_tuples([df0, df1])
    [(0, 0), (1, 2)]
    """
    shifts = []
    for subgrid in qlist_subgrid:
        shift_x = subgrid.index.get_level_values('coord_x').min()
        shift_y = subgrid.index.get_level_values('coord_y').min()
        shifts.append((shift_x, shift_y))
    return shifts


def shift_coords(df_subgrids: list[pd.DataFrame], shifts: list[tuple[int, int]], level: int) -> list[pd.DataFrame]:
    """Shift (x, y) coordinates in cropped grids from `df_subgrids` to create proper subgrids of corresponding `level`.

    The subgrids will start at (0, 0). Adjacent quadrats will be merged to create larger `level`x`level` quadrats.

    If quadrat list is passed (has coords as indices), duplicates will be dropped.

    >>> df0 = pd.DataFrame({'coord_x': [0, 0, 1, 1], 'coord_y': [0, 1, 0, 1]})
    >>> res = shift_coords([df0], [(0, 0)], 1)
    >>> len(res)
    1
    >>> res[0]
       coord_x  coord_y
    0        0        0
    1        0        1
    2        1        0
    3        1        1
    >>> df1 = pd.DataFrame(data={'coord_x': [0, 0, 1, 1], 'coord_y': [1, 2, 1, 2]})
    >>> res = shift_coords([df0, df1], [(0, 0), (0, 1)], 2)
    >>> len(res)
    2
    >>> res[0]
       coord_x  coord_y
    0        0        0
    1        0        0
    2        0        0
    3        0        0
    >>> res[1]
       coord_x  coord_y
    0        0        0
    1        0        0
    2        0        0
    3        0        0
    >>> coords_idx = pd.MultiIndex.from_arrays([[0, 0, 1, 1], [1, 2, 1, 2]], names=('coord_x', 'coord_y'))
    >>> df2 = df1.copy().set_index(coords_idx, verify_integrity=True)
    >>> res = shift_coords([df2], [(0, 1)], 2)
    >>> res[0]  # doctest: +NORMALIZE_WHITESPACE
                    coord_x  coord_y
    coord_x coord_y
    0       0             0        0
    """
    res = []
    for subgrid, shift in zip(df_subgrids, shifts, strict=True):
        new_xs = subgrid.coord_x.sub(shift[0]).floordiv(level)
        new_ys = subgrid.coord_y.sub(shift[1]).floordiv(level)
        shifted = subgrid.assign(coord_x=new_xs, coord_y=new_ys)
        if 'coord_x' in shifted.index.names:  # is qlist
            shifted = shifted.drop_duplicates(subset=['coord_x', 'coord_y'])
            # fix up out-of-sync coords after drop
            shifted = shifted.set_index(['coord_x', 'coord_y'], drop=False, verify_integrity=True)
        res.append(shifted)
    return res


def create_subgrids(df: pd.DataFrame, cutoffs: Mapping[Edge, int]) -> list[pd.DataFrame]:
    """Create up to 4 subgrids by cutting off transects/zones beyond cutoff from either side.

    >>> idx = pd.MultiIndex.from_tuples(
    ...     [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)],
    ...     names=['coord_x', 'coord_y'],
    ... )
    >>> df = pd.DataFrame(index=idx)
    >>> res = create_subgrids(df, {'left': 0, 'bottom': 0, 'right': 3, 'top': 2})
    >>> len(res)
    1
    >>> res[0]
    Empty DataFrame
    Columns: []
    Index: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
    """
    if not {'coord_x', 'coord_y'}.issubset(df.columns):
        coord_x = df.index.get_level_values('coord_x')
        coord_y = df.index.get_level_values('coord_y')
    else:
        coord_x = df['coord_x']  # type: ignore[assignment]  # behaves the same for our purposes
        coord_y = df['coord_y']  # type: ignore[assignment]  # behaves the same for our purposes
    left_part = coord_x <= cutoffs['right']
    bottom_part = coord_y <= cutoffs['top']
    right_part = coord_x >= cutoffs['left']
    top_part = coord_y >= cutoffs['bottom']

    df0 = df[bottom_part & left_part]
    df1 = df[bottom_part & right_part]
    df2 = df[top_part & left_part]
    df3 = df[top_part & right_part]

    res: list[pd.DataFrame] = []
    for maybe_dup in [df0, df1, df2, df3]:
        df_added = any(maybe_dup.equals(res_df) for res_df in res)
        if not df_added:
            res.append(maybe_dup)
    return res
