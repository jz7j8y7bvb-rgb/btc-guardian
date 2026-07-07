from core.market import get_market_snapshot
from core.engine.technical_engine import TechnicalEngine


def test_technical_engine():
    snapshot = get_market_snapshot()

    engine = TechnicalEngine(snapshot.history)

    results = engine.analyze()

    assert len(results) >= 3

    for result in results:
        assert result.name != ""