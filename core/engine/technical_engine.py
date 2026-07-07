from core.indicators.trend import TrendIndicators


class TechnicalEngine:

    def __init__(self, history):
        self.history = history

    def analyze(self):
        trend = TrendIndicators(self.history)

        return [
            trend.sma50(),
            trend.sma200(),
            trend.rsi(),
        ]