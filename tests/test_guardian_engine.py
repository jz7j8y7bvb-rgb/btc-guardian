from core.market import get_market_snapshot
from core.engine.technical_engine import TechnicalEngine
from core.engine.guardian_engine import GuardianEngine


def test_guardian_score():

    snapshot = get_market_snapshot()

    technical = TechnicalEngine(snapshot.history)

    indicators = technical.analyze()

    guardian = GuardianEngine()

    score = guardian.analyze(indicators)

    assert 0 <= score.score <= 100
    assert score.recommendation in [
        "BUY",
        "HOLD",
        "REDUCE",
        "DEFENSIVE",
    ]