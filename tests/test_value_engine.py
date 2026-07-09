from core.market import get_market_snapshot
from core.engine.value_engine import ValueEngine

snapshot = get_market_snapshot()

result = ValueEngine().analyze(snapshot.history)

print(result)