from core.market import get_market_snapshot
from core.engine.technical_engine import TechnicalEngine
from core.engine.guardian_engine import GuardianEngine
from dashboard.terminal import show_dashboard
from core.database import initialize_database, save_snapshot

def main():
    initialize_database()

    snapshot = get_market_snapshot()

    technical = TechnicalEngine(snapshot.history)
    results = technical.analyze()

    guardian = GuardianEngine()
    analysis = guardian.analyze(results)

    save_snapshot(snapshot, analysis)

    show_dashboard(snapshot, results, analysis)


if __name__ == "__main__":
    main()