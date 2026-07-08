from datetime import datetime

from sqlalchemy import (
    create_engine,
    String,
    Column,
    Integer,
    Float,
    DateTime,
)

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import DATABASE_FILE

Base = declarative_base()

engine = create_engine(f"sqlite:///{DATABASE_FILE}")

Session = sessionmaker(bind=engine)


class MarketHistory(Base):

    __tablename__ = "market_history"

    id = Column(Integer, primary_key=True)

    timestamp = Column(DateTime, default=datetime.utcnow)

    btc_usd = Column(Float)

    btc_eur = Column(Float)

    guardian_score = Column(Integer)

    recommendation = Column(String)

    confidence = Column(Integer)

def initialize_database():

    Base.metadata.create_all(engine)


def save_snapshot(snapshot, analysis):

    session = Session()

    row = MarketHistory(
        btc_usd=snapshot.btc_usd,
        btc_eur=snapshot.btc_eur,
        guardian_score=analysis.score,
        recommendation=analysis.recommendation,
        confidence=analysis.confidence,
    )

    session.add(row)

    session.commit()

    session.close()