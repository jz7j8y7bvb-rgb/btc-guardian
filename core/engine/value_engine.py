from core.models.analysis import AnalysisSection


class ValueEngine:

    def analyze(self, history):

        return AnalysisSection(
            name="Value",
            score=50,
            confidence=50,
            summary="Value engine not implemented yet.",
            evidence=[],
        )