from dataclasses import dataclass, field
from enum import Enum


class Signal(Enum):
    VERY_BULLISH = 2
    BULLISH = 1
    NEUTRAL = 0
    BEARISH = -1
    VERY_BEARISH = -2


@dataclass(slots=True)
class IndicatorResult:
    name: str
    value: float
    signal: Signal
    description: str

    # Relative importance of the indicator.
    # Used by the Guardian Engine in future versions.
    weight: float = 1.0