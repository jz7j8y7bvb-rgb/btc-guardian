from core.market import get_market_snapshot
from core.indicators.trend import TrendIndicators
from dashboard.terminal import show_dashboard

snapshot = get_market_snapshot()

trend = TrendIndicators(snapshot.history)

print(trend.sma50())
print(trend.sma200())
print(trend.rsi())

show_dashboard(snapshot)