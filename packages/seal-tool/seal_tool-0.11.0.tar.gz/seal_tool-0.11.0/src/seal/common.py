#!/usr/bin/env python3

import random
from collections.abc import Callable, Generator
from pathlib import Path
from typing import cast

import pandas as pd
from alive_progress.animations.spinners import bouncing_spinner_factory  # type: ignore[import-untyped]
from pandas._typing import Dtype


def get_spinner() -> Callable[[None], Generator]:  # type: ignore[type-arg]
    emoji = ['🐧', '🐡', '🐟', '🦑', '🦦', '🐠', '🦐', '🐙', '🪼', '🐳']
    random.shuffle(emoji)
    emoji = ''.join(emoji)
    spinner = bouncing_spinner_factory(('🌊', emoji), 6, block=(1, 1), hide=True)
    return cast(Callable[[None], Generator], spinner)  # type: ignore[type-arg]


def analysis_results_filename(out_dir: Path, taskfile: Path, analysis_type: str, analysis_idx: int) -> Path:
    if analysis_idx:
        plain_path = out_dir / f'{taskfile.stem}-{analysis_type}-{analysis_idx}.csv'
    else:
        plain_path = out_dir / f'{taskfile.stem}-{analysis_type}.csv'
    return plain_path


def enc_dtypes() -> dict[str, Dtype]:
    direction = pd.CategoricalDtype(categories=['b', 'f'])
    phase = pd.CategoricalDtype(categories=['ad', 'init', 'juv', 'sub', 'term'])
    return {
        'significant_size': 'bool',
        'direction': direction,
        'phase': phase,
        'ref': 'Int64',
    }


def qlist_dtypes() -> dict[str, Dtype]:
    q_type = pd.CategoricalDtype(['normal', 'no-reef', 'riptide', 'shallows'])
    return {
        'coord_x': 'Int64',
        'coord_y': 'Int64',
        'quadrat_type': q_type,
    }


def geom_r2(start: float, end: float) -> list[float]:
    res = []
    current = start
    while current <= end:
        res.append(current)
        current *= 2
    return res
