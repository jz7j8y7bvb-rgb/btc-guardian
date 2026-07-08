from dashboard.terminal import show_dashboard
from core.market import get_market_snapshot
from core.engine.technical_engine import TechnicalEngine
from core.engine.guardian_engine import GuardianEngine


def test_dashboard():

    snapshot = get_market_snapshot()

    indicators = TechnicalEngine(snapshot.history).analyze()

    analysis = GuardianEngine().analyze(indicators)

    show_dashboard(snapshot, indicators, analysis)