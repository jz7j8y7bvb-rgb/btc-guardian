from dataclasses import dataclass
import pandas as pd
import yfinance as yf


@dataclass
class MarketSnapshot:
    btc_usd: float
    btc_eur: float
    history: pd.DataFrame


def get_market_snapshot() -> MarketSnapshot:
    btc_usd = yf.Ticker("BTC-USD")
    btc_eur = yf.Ticker("BTC-EUR")

    history = btc_usd.history(period="1y")

    usd_price = float(history["Close"].iloc[-1])

    eur_price = float(
        btc_eur.history(period="1d")["Close"].iloc[-1]
    )

    return MarketSnapshot(
        btc_usd=usd_price,
        btc_eur=eur_price,
        history=history,
    )