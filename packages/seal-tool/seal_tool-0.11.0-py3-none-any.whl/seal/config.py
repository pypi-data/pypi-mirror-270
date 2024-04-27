import tomllib
from datetime import datetime
from keyword import iskeyword, issoftkeyword
from pathlib import Path
from typing import Any, Literal, Self

from pydantic import Field, PositiveFloat, PositiveInt, model_validator
from pydantic.dataclasses import dataclass
from pydantic_core import ArgsKwargs

type Distance = Literal['centroid', 'diagonal', 'max1d']
type ErrorStyle = Literal['band', 'bars']
type ErrorType = Literal['ci', 'pi', 'se', 'sd']
type Format = Literal['png', 'svg']
type LevelStrategy = Literal[
    'nested-quadrats',
    'overlaid-subgrids',
    'repeated-transect-merging',
    'striped-transect-merging',
    'transect-additive',
    'transect-merging',
    'zone-additive',
    'zone-merging',
]
type SamplingDirection = Literal['any', 'backward', 'forward', 'richer']
type QuadratType = Literal['normal', 'no-reef', 'riptide', 'shallows']
type AnalysisNameShort = Literal['a1', 'a5', 'a6', 'a7', 'a8']
type AnalysisNameLong = Literal['overview', 'oerich', 'sratios', 'jaccard', 'abundance']


def normalize_param_names(params: dict[str, Any] | ArgsKwargs) -> dict[str, Any]:
    if isinstance(params, ArgsKwargs):
        if not params.kwargs:
            return {}
        d = params.kwargs
    elif isinstance(params, dict):
        d = params
    else:
        raise TypeError(params)
    normalized = {}
    for k, v in d.items():
        norm_k = k.replace('-', '_')
        norm_k = f'{norm_k}_' if iskw(norm_k) else norm_k
        normalized[norm_k] = v
    return normalized


def iskw(s: str) -> bool:
    return iskeyword(s) or issoftkeyword(s)


@dataclass(frozen=True, config={'extra': 'forbid', 'validate_default': True})
class Analysis0:
    type_: AnalysisNameShort | AnalysisNameLong

    @model_validator(mode='before')
    @classmethod
    def pre_validate(cls, params: dict[str, Any]) -> dict[str, Any]:
        return normalize_param_names(params)


@dataclass(frozen=True, config={'extra': 'forbid', 'validate_default': True})
class Analysis2(Analysis0):
    type_: Literal['a2', 'sar']  # type: ignore[assignment]
    permutations: PositiveInt = 200


@dataclass(frozen=True, config={'extra': 'forbid', 'validate_default': True})
class Analysis3(Analysis0):
    type_: Literal['a3', 'spdiff']  # type: ignore[assignment]
    interval: PositiveFloat | None = None


@dataclass(frozen=True, config={'extra': 'forbid', 'validate_default': True})
class Analysis4(Analysis0):
    type_: Literal['a4', 'rrich']  # type: ignore[assignment]
    radius_step: PositiveFloat


type Analysis = Analysis0 | Analysis2 | Analysis3 | Analysis4


@dataclass(frozen=True, config={'extra': 'forbid', 'validate_default': True})
class Sides:
    """Represents side lengths of quadrats."""

    x: PositiveFloat
    y: PositiveFloat


@dataclass(frozen=True, config={'extra': 'forbid', 'validate_default': True})
class Locality:
    sides: Sides
    quadrat_list: Path | None = None
    name: str | None = None
    from_: datetime | None = None
    to: datetime | None = None

    @model_validator(mode='before')
    @classmethod
    def pre_validate(cls, ks: dict[str, Any]) -> dict[str, Any]:
        return {k.replace('-', '_').replace('from', 'from_'): v for k, v in ks.items()}


@dataclass(frozen=True, config={'extra': 'forbid', 'validate_default': True})
class Plot:
    error_type: ErrorType = 'pi'
    error_style: ErrorStyle = 'band'
    logscale_x: bool = True
    output_format: Format = 'svg'

    @model_validator(mode='before')
    @classmethod
    def pre_validate(cls, params: ArgsKwargs | dict[str, Any]) -> dict[str, Any]:
        return normalize_param_names(params)


@dataclass(frozen=True, config={'extra': 'forbid', 'validate_default': True})
class Config:
    """Configuration read from taskfile."""

    locality: Locality
    encounters: Path

    out_dir: Path = Path('./results')
    levels: list[PositiveInt] = Field(default=[1, 2, 3])
    level_strategy: LevelStrategy = 'nested-quadrats'
    direction: SamplingDirection = 'any'
    include_tiny: bool = True
    quadrat_types: list[QuadratType] | None = None
    distance_type: Distance = 'diagonal'
    discard_zone_info: bool = False
    discard_transect_info: bool = False
    discard_indistinguishable: bool = True
    exclude_families: list[str] = Field(default_factory=list)
    include_families: list[str] = Field(default_factory=list)
    exclude_phases: list[str] = Field(default_factory=list)
    seed: int | None = None
    use_morph: bool = False

    analyses: list[Analysis] = Field(default_factory=list)
    plot: Plot = Plot()

    @classmethod
    def from_taskfile(cls, taskfile: Path) -> Self:
        with taskfile.open('rb') as task:
            task_dict = tomllib.load(task)
        return cls(**task_dict)

    @model_validator(mode='before')
    @classmethod
    def pre_validate(cls, akwa: ArgsKwargs) -> dict[str, Any]:
        return normalize_param_names(akwa)
