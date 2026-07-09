from config import value

from core.indicators.trend import TrendIndicators
from core.models.value import ValueAnalysis


class ValueEngine:

    def analyze(self, history):

        indicators = TrendIndicators(history)

        score = 50

        evidence = []

        rsi = indicators.rsi()

        if rsi.value < 30:
            score += value.RSI_WEIGHT
            evidence.append("RSI indicates oversold conditions.")

        elif rsi.value < 45:
            score += value.RSI_WEIGHT // 2
            evidence.append("RSI suggests improving value.")

        elif rsi.value > 70:
            score -= value.RSI_WEIGHT
            evidence.append("RSI indicates overbought conditions.")

        distance = indicators.sma200_distance()
        if distance <= value.VERY_ATTRACTIVE:
            score += value.SMA200_DISTANCE_WEIGHT
            evidence.append(
                "Bitcoin trades far below its 200-day average."
            )

        elif distance <= value.ATTRACTIVE:
            score += value.SMA200_DISTANCE_WEIGHT // 2
            evidence.append(
                "Bitcoin trades below its 200-day average."
            )

        elif distance > value.FAIR:
            score -= value.SMA200_DISTANCE_WEIGHT // 2
            evidence.append(
                "Bitcoin trades above its long-term average."
            )
        
        score = max(0, min(score, 100))
        if score >= 80:
            summary = "Very attractive valuation."

        elif score >= 65:
            summary = "Attractive valuation."

        elif score >= 45:
            summary = "Fair valuation."

        else:
            summary = "Expensive relative to recent history."
        return ValueAnalysis(
            score=score,
            confidence=75,
            summary=summary,
            evidence=evidence,
        )