from core.models.trend import TrendAnalysis
from core.models.indicator import Signal
from core.indicators.trend import TrendIndicators
from config import trend

class TrendEngine:

    def analyze(self, history):

        indicators = TrendIndicators(history)

        evidence = []

        score = 50

        # Analyze SMA 50
        sma50 = indicators.sma50()

        if sma50.signal == Signal.BULLISH:
            score += trend.SMA50_WEIGHT
            evidence.append("Price is above the 50-day moving average.")

        elif sma50.signal == Signal.BEARISH:
            score -= trend.SMA50_WEIGHT
            evidence.append("Price is below the 50-day moving average.")

        # Analyze SMA 200
        sma200 = indicators.sma200()

        if sma200.signal == Signal.BULLISH:
            score += trend.SMA200_WEIGHT
            evidence.append("Price is above the 200-day moving average.")

        elif sma200.signal == Signal.BEARISH:
            score -= trend.SMA200_WEIGHT
            evidence.append("Price is below the 200-day moving average.")

        # Analyze RSI
        rsi = indicators.rsi()

        if rsi.signal == Signal.BULLISH:
            score += trend.RSI_WEIGHT
            evidence.append("Momentum is improving.")

        elif rsi.signal == Signal.BEARISH:
            score -= trend.RSI_WEIGHT
            evidence.append("Momentum is weakening.")

        else:
            evidence.append("Momentum is neutral.")

        # Keep score between 0 and 100
        score = max(0, min(score, 100))

        # Human-readable summary
        if score >= trend.STRONG_BULLISH:
            summary = "Strong bullish trend."

        elif score >= trend.BULLISH:
            summary = "Bullish trend."

        elif score >= trend.NEUTRAL:
            summary = "Neutral trend."

        elif score >= trend.BEARISH:
            summary = "Weak bearish trend."

        else:
            summary = "Strong bearish trend."

        confidence = 70

        return TrendAnalysis(
            score=score,
            confidence=confidence,
            summary=summary,
            evidence=evidence,
        )