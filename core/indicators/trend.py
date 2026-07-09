import ta

from core.models.indicator import IndicatorResult, Signal


class TrendIndicators:
    def __init__(self, history):
        self.history = history

    def sma50(self):
        sma = ta.trend.sma_indicator(
            self.history["Close"],
            window=50
        ).iloc[-1]

        price = self.history["Close"].iloc[-1]

        signal = Signal.BULLISH if price > sma else Signal.BEARISH

        return IndicatorResult(
            "SMA 50",
            float(sma),
            signal,
            "Price compared with the 50-day moving average",
        )

    def sma200(self):
        sma = ta.trend.sma_indicator(
            self.history["Close"],
            window=200
        ).iloc[-1]

        price = self.history["Close"].iloc[-1]

        signal = Signal.BULLISH if price > sma else Signal.BEARISH

        return IndicatorResult(
            "SMA 200",
            float(sma),
            signal,
            "Price compared with the 200-day moving average",
        )

    def rsi(self):
        value = ta.momentum.rsi(
            self.history["Close"],
            window=14
        ).iloc[-1]

        if value < 30:
            signal = Signal.VERY_BULLISH
        elif value < 45:
            signal = Signal.BULLISH
        elif value < 55:
            signal = Signal.NEUTRAL
        elif value < 70:
            signal = Signal.BEARISH
        else:
            signal = Signal.VERY_BEARISH

        return IndicatorResult(
            "RSI",
            float(value),
            signal,
            "Relative Strength Index",
        )
    
    def sma200_distance(self):

        sma200 = ta.trend.sma_indicator(
            self.history["Close"],
            window=200,
        ).iloc[-1]

        price = self.history["Close"].iloc[-1]

        distance = ((price - sma200) / sma200) * 100
        return float(distance)