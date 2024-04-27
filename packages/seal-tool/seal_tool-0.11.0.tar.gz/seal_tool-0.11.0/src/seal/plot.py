import argparse
import datetime
import random
from collections.abc import Generator
from pathlib import Path
from typing import Final, Literal

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns  # type: ignore[import-untyped] # wontfix'ed https://github.com/mwaskom/seaborn/issues/2212, partial https://github.com/mwaskom/seaborn/issues/3287
from alive_progress import alive_bar  # type: ignore[import-untyped]
from matplotlib.ticker import FixedLocator, ScalarFormatter

from seal.common import analysis_results_filename, geom_r2, get_spinner
from seal.config import Analysis, Config, Sides
from seal.exceptions import InvalidLiteralError

type Metadata = dict[str, str | list[str] | None]
type PlotData = tuple[list[matplotlib.figure.Figure], Metadata]

SVG_METADATA: Final[Metadata] = {
    'Description': (
        'Work was funded by project Influence of sample grain'
        ' and extent on coral reef fish richness, MUNI / IGA / 1076 / 2021.'
    ),
    'Contributor': ['Martin Matouš', 'Barbora Winterová'],
    'Coverage': None,
    'Keywords': None,
    'Language': 'en',
    'Publisher': 'Department of Botany and Zoology, Faculty of Science, Masaryk University',
    # 'Relation': DOI of published paper
    'Rights': 'CC BY-SA 4.0',
    'Title': None,
}

ADD_PNG_METADATA: Final[Metadata] = {
    'Copyright': 'CC BY-SA 4.0',
    'Creation Time': None,
    'Software': 'seal (https://pypi.org/project/seal-tool/)',
}


def main(args: argparse.Namespace) -> int:
    sns.set_theme(palette='colorblind', rc={'backend': 'svg'})
    cfg = Config.from_taskfile(args.taskfile)
    csv_results_dir = cfg.out_dir  # it's outdir from the perspective of analysis, not plot
    spinner = get_spinner()
    analysis_idx = {analysis.type_: 0 for analysis in cfg.analyses}
    with alive_bar(len(cfg.analyses), title='Plotting', spinner=spinner) as bar:
        for analysis in cfg.analyses:
            analysis_file = analysis_results_filename(
                csv_results_dir, args.taskfile, analysis.type_, analysis_idx[analysis.type_]
            )
            plot_analysis(analysis_file, cfg, analysis)
            analysis_idx[analysis.type_] += 1
            bar.text(f'{analysis.type_}')
            bar()
    return 0


def plot_analysis(analysis_file: Path, cfg: Config, analysis: Analysis) -> None:
    df = pd.read_csv(analysis_file)
    # seaborn ignores palette for numeric hues
    # https://github.com/mwaskom/seaborn/issues/2606
    df['level'] = df['level'].astype(str)
    random.seed(cfg.seed)
    np.random.seed(cfg.seed)
    figs, meta = plot_figures(df, cfg, analysis)
    if cfg.plot.output_format == 'png':
        meta = conv_png_metadata(meta)
    out_path = analysis_file.with_suffix(f'.{cfg.plot.output_format}')
    for i, fig in enumerate(figs):
        out_path = out_path.with_stem(f'{analysis_file.stem}-{i}')
        fig.savefig(out_path, metadata=meta)
        print(f'Graph plotted at {out_path}')
    matplotlib.pyplot.close('all')


def plot_figures(df: pd.DataFrame, cfg: Config, analysis: Analysis) -> PlotData:  # noqa: PLR0911
    match analysis.type_:
        case 'a1' | 'overview':
            return a1(df, cfg)
        case 'a2' | 'sar':
            return a2(df, cfg)
        case 'a3' | 'spdiff':
            return a3(df, cfg)
        case 'a4' | 'rrich':
            return a4(df, cfg)
        case 'a5' | 'oerich':
            return a5(df, cfg)
        case 'a6' | 'sratios':
            return a6(df, cfg)
        case 'a7' | 'jaccard':
            return a7(df, cfg)
        case 'a8' | 'abundance':
            return a8(df, cfg)
        case _:
            raise InvalidLiteralError(f'{analysis.type_=}')


def level_aspect(sides: Sides, level: int, lvl_strat: str) -> float:
    if lvl_strat in {'transect-merging', 'repeated-transect-merging', 'striped-transect-merging'}:
        return sides.y / (sides.x * level)
    if lvl_strat == 'zone-merging':
        return sides.y * level / sides.x
    if lvl_strat in {'overlaid-subgrids', 'transect-additive', 'zone-additive', 'nested-quadrats'}:
        return sides.y / sides.x
    raise InvalidLiteralError(f'{lvl_strat=}')


def a1(df: pd.DataFrame, cfg: Config) -> PlotData:
    locname = cfg.locality.name
    meta = fill_metadata(locname, 'a1')
    bplot_cfg = [{'y': 'n_species', 'ylabel': 'species'}]
    df = df.astype(int)

    figs = []
    level_dfs = list(df_levels(df))
    for ldf, level in level_dfs:
        fig, ax = plt.subplots(figsize=(12, 12))
        fig.suptitle(f'{locname} species')

        val_matrix = ldf.pivot_table(index='coord_y', columns='coord_x', values='n_species')
        val_matrix = val_matrix.sort_index(ascending=False)

        aspect = level_aspect(cfg.locality.sides, level, cfg.level_strategy)
        sns.heatmap(val_matrix, annot=True, fmt='g', cmap='magma_r', linewidths=0.3, cbar_kws={'shrink': 0.5}, ax=ax)
        ax.grid(visible=False)
        ax.set(xlabel='Transect', ylabel='Zone', aspect=aspect, title=f'Level {level}')
        fig.text(x=0.7, y=0.05, s=f'Level strategy: {cfg.level_strategy}')
        figs.append(fig)

    if 'n_individuals' in df.columns:
        bplot_cfg.append({'y': 'n_individuals', 'ylabel': 'individuals'})

        for ldf, level in level_dfs:
            fig, ax = plt.subplots(figsize=(12, 12))
            fig.suptitle(f'{locname} individuals')
            val_matrix = ldf.pivot_table(index='coord_y', columns='coord_x', values='n_individuals')
            val_matrix = val_matrix.sort_index(ascending=False)
            sns.heatmap(
                val_matrix, annot=True, fmt='g', cmap='magma_r', linewidths=0.3, cbar_kws={'shrink': 0.5}, ax=ax
            )
            ax.grid(visible=False)
            aspect = level_aspect(cfg.locality.sides, level, cfg.level_strategy)
            ax.set(xlabel='Transect', ylabel='Zone', aspect=aspect, title=f'Level {level}')
            fig.text(x=0.7, y=0.05, s=f'Level strategy: {cfg.level_strategy}')
            figs.append(fig)

    for bar_cfg in bplot_cfg:
        fig, ax = plt.subplots(figsize=(48, 12))
        fig.suptitle(f'{bar_cfg['ylabel'].title()} in quadrats')
        ldf_s = ldf.sort_values(bar_cfg['y'], ascending=False)
        sns.barplot(
            x=map(str, zip(ldf_s.coord_x, ldf_s.coord_y, strict=False)),
            y=ldf_s[bar_cfg['y']],
            gap=0.2,
            errorbar=cfg.plot.error_type,
        )
        ax.bar_label(ax.containers[0], fontsize=10)
        ax.set(xlabel='Quadrat', ylabel=f'# of {bar_cfg['ylabel']}', title=f'{locname}, level {level}')
        figs.append(fig)

    return figs, meta


def a2(df: pd.DataFrame, cfg: Config) -> PlotData:
    locname = cfg.locality.name
    meta = fill_metadata(locname, 'a2')
    err_style = cfg.plot.error_style

    init_df = df.copy()
    df = df.drop(['min_acc', 'max_acc'], axis='columns', errors='raise')
    df['id'] = range(len(df))
    df = pd.wide_to_long(df, stubnames='', i=['id'], j='subid').rename({'': 'species'}, axis='columns', errors='raise')

    fig1, ax1 = plt.subplots()

    sns.lineplot(
        x='area',
        y='species',
        hue='level',
        seed=cfg.seed,
        estimator='mean',
        err_style=err_style,
        ax=ax1,
        data=df,
        errorbar=cfg.plot.error_type,
    )
    ax1.set(xlabel='Surface area ($m^2$)', ylabel='# of species', title='Species-area relationship')

    fig2, ax2 = plt.subplots()
    sns.lineplot(
        x='area',
        y='min_acc',
        hue='level',
        seed=cfg.seed,
        estimator='mean',
        err_style=None,
        data=init_df,
        ax=ax2,
        legend=False,
    )
    sns.lineplot(
        x='area', y='max_acc', hue='level', seed=cfg.seed, estimator='mean', err_style=None, data=init_df, ax=ax2
    )
    ax2.set(xlabel='Surface area ($m^2$)', ylabel='# of species', title='Species-area relationship extremes')

    if cfg.plot.logscale_x:
        for ax in [ax1, ax2]:
            ax.set_xscale('log')
            min_area = init_df.area.min()
            max_area = init_df.area.max()
            ticks = geom_r2(min_area, max_area)
            ax.xaxis.set_major_locator(FixedLocator(ticks))
            ax.xaxis.set_major_formatter(ScalarFormatter())

    return [fig1, fig2], meta


def a3(df: pd.DataFrame, cfg: Config) -> PlotData:
    locname = cfg.locality.name
    meta = fill_metadata(locname, 'a3')
    figs = []
    axs = []

    fig1, ax1 = plt.subplots()
    fig1.suptitle('Pair-wise species difference')
    sns.lineplot(
        x='distance',
        y='abs_diff',
        hue='level',
        seed=cfg.seed,
        estimator='mean',
        err_style=cfg.plot.error_style,
        errorbar=cfg.plot.error_type,
        ax=ax1,
        data=df,
    )
    figs.append(fig1)
    axs.append(ax1)

    if 'distance_bin' in df.columns:
        fig2, ax2 = plt.subplots(figsize=(20, 20))
        fig2.suptitle('Pair-wise species difference')
        sns.boxplot(x='distance_bin', y='abs_diff', hue='level', ax=ax2, data=df)
        plt.setp(ax2.collections, alpha=0.3)
        sns.rugplot(y='abs_diff', hue='level', ax=ax2, data=df)
        ax2.tick_params(axis='x', labelrotation=45)
        figs.append(fig2)
        axs.append(ax2)

    for ax in axs:
        ax.set(xlabel='Distance ($m$)', ylabel='Difference', title=locname)

    return figs, meta


def a4(df: pd.DataFrame, cfg: Config) -> PlotData:
    locname = cfg.locality.name
    meta = fill_metadata(locname, 'a4')

    # intervals are simply strings to seaborn, can't be sorted automatically
    df['distance'] = df['distance'].apply(to_interval)  # type: ignore[arg-type] # valid AggFuncTypeBase (basically Callable[Any]), mypy 1.9.0 bug?
    df = df.sort_values('distance')
    df['distance'] = df.distance.apply(str)

    fig1, ax1 = plt.subplots(figsize=(20, 20))
    fig1.suptitle('Richness of quadrats within distance')
    sns.boxplot(x='distance', y='radius_richness', hue='level', ax=ax1, data=df)

    fig2, ax2 = plt.subplots(figsize=(20, 20))
    fig2.suptitle('Richness of quadrats within distance')
    sns.lineplot(
        x='distance',
        y='radius_richness',
        seed=cfg.seed,
        estimator='median',
        err_style=cfg.plot.error_style,
        errorbar=cfg.plot.error_type,
        hue='level',
        ax=ax2,
        data=df,
    )

    for ax in [ax1, ax2]:
        ax.set(title=locname, xlabel=r'Radius ($m$)', ylabel='# of species')
        ax.tick_params(axis='x', labelrotation=45)

    return [fig1, fig2], meta


def a5(df: pd.DataFrame, cfg: Config) -> PlotData:
    ratios = []
    medians = []
    for ldf, lvl in df_levels(df):
        ratios.append(pd.DataFrame({'oe_ratio': ldf['oe_ratio_mean'], 'level': lvl}))
        m = ldf['oe_ratio_mean'].median()
        medians.append({'value': m, 'vertical_offset': m * 0.05})
    df = pd.concat(ratios, ignore_index=True)

    locname = cfg.locality.name
    meta = fill_metadata(locname, 'a5')

    fig1, ax1 = plt.subplots()
    fig1.suptitle('Observed/expected ratio per level')
    sns.violinplot(x='level', y='oe_ratio', ax=ax1, data=df)
    plt.setp(ax1.collections, alpha=0.3)
    sns.rugplot(y='oe_ratio', ax=ax1, data=df)
    ax1.set(title=locname, xlabel='Level', ylabel='Observed/Expected')

    fig2, ax2 = plt.subplots()
    fig1.suptitle('Observed/expected ratio per level')
    sns.boxplot(x='level', y='oe_ratio', ax=ax2, data=df)
    sns.stripplot(x='level', y='oe_ratio', linewidth=0.7, ax=ax2, data=df)
    ax2.set(title=locname, xlabel='Level', ylabel='Observed/Expected')
    for xtick, median in zip(ax2.get_xticks(), medians, strict=True):
        ax2.text(
            xtick,
            median['value'] + median['vertical_offset'],
            f'{median['value']:.2f}',
            horizontalalignment='center',
            size='x-small',
            color='w',
            weight='semibold',
        )

    return [fig1, fig2], meta


def a6(df: pd.DataFrame, cfg: Config) -> PlotData:
    locname = cfg.locality.name
    meta = fill_metadata(locname, 'a6')

    line_cfgs = [
        {'ycol': 'common_total', 'title': f'{locname}, common / total species ratio', 'ylabel': 'common / total'},
        {
            'ycol': 'common_diff',
            'title': f'{locname}, common / differing species ratio',
            'ylabel': 'common / differing',
        },
        {'ycol': 'common_union', 'title': f'{locname}, common / present species ratio', 'ylabel': 'common / present'},
    ]

    err_style = cfg.plot.error_style
    figs = []
    for line_cfg in line_cfgs:
        fig, ax = plt.subplots()
        sns.lineplot(
            x='distance',
            y=line_cfg['ycol'],
            seed=cfg.seed,
            estimator='mean',
            err_style=err_style,
            errorbar=cfg.plot.error_type,
            hue='level',
            data=df,
            ax=ax,
        )
        ax.set(title=line_cfg['title'], xlabel=r'Quadrat distance ($m$)', ylabel=line_cfg['ylabel'])
        figs.append(fig)

    return figs, meta


def a7(df: pd.DataFrame, cfg: Config) -> PlotData:
    locname = cfg.locality.name
    meta = fill_metadata(locname, 'a7')

    err_style = cfg.plot.error_style
    fig, ax = plt.subplots()
    sns.lineplot(
        x='distance',
        y='jaccard_dissimilarity',
        seed=cfg.seed,
        estimator='mean',
        err_style=err_style,
        errorbar=cfg.plot.error_type,
        hue='level',
        data=df,
        ax=ax,
    )
    fig.suptitle('Jaccard dissimilarity / distance')
    ax.set(title=locname, xlabel=r'Quadrat distance ($m$)', ylabel='Jaccard dissimilarity')

    return [fig], meta


def a8(df: pd.DataFrame, cfg: Config) -> PlotData:
    locname = cfg.locality.name
    meta = fill_metadata(locname, 'a8')
    figs = []

    fig, ax = plt.subplots(figsize=(12, 12))
    df['individuals_bin'] = pd.cut(df.individuals, geom_r2(1, df.individuals.max()), right=False)
    ab_dist_df = df.groupby(['level', 'individuals_bin'], as_index=False, observed=False).count()
    sns.barplot(x='individuals_bin', y='species', hue='level', data=ab_dist_df, ax=ax, errorbar=cfg.plot.error_type)
    fig.suptitle('Species abundance distribution')
    ax.tick_params(axis='x', labelrotation=45)
    ax.set(title=locname, xlabel='Abundance', ylabel='# of species')
    figs.append(fig)

    for ldf, lvl in df_levels(df):
        fig, ax = plt.subplots(figsize=(20, 20))
        ldf_sorted = ldf.sort_values('individuals', ascending=False)
        sns.barplot(x='species', y='individuals', data=ldf_sorted, ax=ax)
        ax.bar_label(ax.containers[0], fontsize=5)
        fig.suptitle('Equitability of abundance')
        ax.set(title=f'{locname}, level {lvl}', xlabel='Species', ylabel='Abundance')
        ax.tick_params(axis='x', labelrotation=90)
        figs.append(fig)

    return figs, meta


def df_levels(df: pd.DataFrame) -> Generator[tuple[pd.DataFrame, int], None, None]:
    levels = df['level'].unique()
    for level in sorted(levels):
        ldf = df[df.level == level]
        yield (ldf, int(level))


def to_interval(intr: str) -> 'pd.Interval[float]':
    closed = (intr[0] == '[', intr[-1] == ']')
    cl_type: Literal['left', 'right', 'both', 'neither']
    match closed:
        case (True, False):
            cl_type = 'left'
        case (False, True):
            cl_type = 'right'
        case (True, True):
            cl_type = 'both'
        case (False, False):
            cl_type = 'neither'
    left, right = map(float, intr[1:-1].split(','))
    return pd.Interval(left, right, cl_type)


def fill_metadata(locname: str | None, analysis: str) -> Metadata:
    metadata = SVG_METADATA.copy()
    per_analysis_kw: dict[str, list[str]] = {
        'a1': ['overview', 'species', 'quadrat', 'transect', 'species richness'],
        'a2': ['species area relationship', 'species', 'area'],
        'a3': ['pairwise difference', 'distance', 'distance decay'],
        'a4': ['species', 'sum', 'radius'],
        'a5': ['expected species richness', 'observed/expected'],
        'a6': ['species', 'shared species', 'different specied', 'distance decay', 'common/total', 'common/differing'],
        'a7': ['jaccard dissimilarity', 'jaccard', 'distance decay'],
        'a8': [],
    }
    kws = ['marine', 'ecology'] + per_analysis_kw[analysis]
    if locname:
        metadata['Title'] = metadata['Coverage'] = locname
        kws.append(locname)
    else:
        metadata['Title'] = metadata['Coverage'] = analysis
    metadata['Keywords'] = sorted(kws)
    return metadata


def conv_png_metadata(metadata: Metadata) -> Metadata:
    for key, val in ADD_PNG_METADATA.items():
        metadata[key] = val
    # vals must be latin1-encodable, convert lists to strs
    metadata['Keywords'] = ', '.join(metadata['Keywords'])  # type: ignore[arg-type]
    metadata['Contributor'] = ', '.join(metadata['Contributor'])  # type: ignore[arg-type]
    metadata['Creation Time'] = datetime.datetime.now().astimezone().isoformat()
    del metadata['Rights']  # PNG has "Copyright"
    return metadata
