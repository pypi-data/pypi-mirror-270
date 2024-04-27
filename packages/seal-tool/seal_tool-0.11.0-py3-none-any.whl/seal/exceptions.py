from collections.abc import Iterable
from enum import StrEnum

from pandas import DataFrame

type Coord = tuple[int, int]


class InputType(StrEnum):
    ENCOUNTERS = 'dataset'
    QLIST = 'quadrat list'


class InvalidQuadratsError(Exception):
    """Raised when sp. encountered in quadrat not found in quadrat list."""

    def __init__(self, coords: Iterable[Coord], *, post_adj: bool = False) -> None:
        msg = (
            'Filtered dataset contains encounters in quadrats not found in quadrat list.'
            "Possible causes may be using quadrat list for unintended locality, incorrectly set-up filters, e.g. *from* and *to* dates in taskfile's locality section or simply mistakes/typos in provided quadrat list or dataset."
            'Extraneous coordinates:\n'
            f'{sorted(coords)}'
        )
        if post_adj:
            msg += 'As this happened post-coordinate adjustment, the most likely reason is bug in the program.'
        super().__init__(msg)


class MissingValuesError(Exception):
    """Raised when attribute considered mandatory is NA."""

    def __init__(self, rows: DataFrame, *, post_adj: bool = False) -> None:
        msg = (
            'Processed data contains missing values. This should not happen for properly preprocessed data.'
            'Rows with missing values:\n'
            f'{rows}'
        )
        if post_adj:
            msg += 'As this happened post-coordinate adjustment, the most likely reason is bug in the program.'
        super().__init__(msg)


class InvalidLiteralError(ValueError):
    """Raised when string argument is passed with invalid choice."""

    def __init__(self, selfdoc: str) -> None:
        msg = f'argument {selfdoc} is not a valid choice'
        super().__init__(msg)


class InvalidFilterError(ValueError):
    """Raised when filtering using missing columns is requested."""

    def __init__(self, field: str, input_type: InputType) -> None:
        self.field = field
        self.input_type = input_type
        msg = f'requested filtering on attribute "{self.field}", but input {self.input_type} contains no such column'
        super().__init__(msg)
