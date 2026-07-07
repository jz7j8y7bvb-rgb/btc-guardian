from dataclasses import dataclass
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