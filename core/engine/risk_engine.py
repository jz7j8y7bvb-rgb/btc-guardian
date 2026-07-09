from core.models.analysis import AnalysisSection


class RiskEngine:

    def analyze(self):

        return AnalysisSection(
            name="Risk",
            score=50,
            confidence=50,
            summary="Risk engine not implemented yet.",
            evidence=[],
        )