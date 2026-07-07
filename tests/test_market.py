from core.market import get_market_snapshot


def test_market_snapshot():
    snapshot = get_market_snapshot()

    assert snapshot.btc_usd > 1000
    assert snapshot.btc_eur > 1000
    assert len(snapshot.history) >= 250