from core.models.analysis import AnalysisSection


class TrendEngine:

    def analyze(self, history):

        return AnalysisSection(
            name="Trend",
            score=50,
            confidence=50,
            summary="Trend engine not implemented yet.",
            evidence=[],
        )