from core.models.indicator import Signal
from core.models.score import GuardianScore
from config import scoring

class GuardianEngine:

    def analyze(self, indicators):
        
        # Start from a neutral market score.
        # Bullish indicators add points.
        # Bearish indicators subtract points.
        # In a future version this will become a normalized weighted score.
        score = 50

        explanation = []

        for indicator in indicators:

            if indicator.signal == Signal.VERY_BULLISH:
                score += scoring.VERY_BULLISH
                explanation.append(f"{indicator.name}: Very Bullish")

            elif indicator.signal == Signal.BULLISH:
                score += scoring.BULLISH
                explanation.append(f"{indicator.name}: Bullish")

            elif indicator.signal == Signal.NEUTRAL:
                score += scoring.NEUTRAL
                explanation.append(f"{indicator.name}: Neutral")

            elif indicator.signal == Signal.BEARISH:
                score -= scoring.BEARISH
                explanation.append(f"{indicator.name}: Bearish")

            elif indicator.signal == Signal.VERY_BEARISH:
                score -= scoring.VERY_BEARISH
                explanation.append(f"{indicator.name}: Very Bearish")

        score = max(0, min(score, 100))

        if score >= scoring.BUY:
            recommendation = "BUY"

        elif score >= scoring.HOLD:
            recommendation = "HOLD"

        elif score >= scoring.REDUCE:
            recommendation = "REDUCE"

        else:
            recommendation = "DEFENSIVE"

        confidence = min(100, 50 + abs(score - 50) * 2)

        return GuardianScore(
            score=score,
            recommendation=recommendation,
            confidence=confidence,
            explanation=explanation,
        )
        