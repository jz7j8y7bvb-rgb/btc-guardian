from dataclasses import dataclass, field


@dataclass(slots=True)
class TrendAnalysis:
    score: int
    confidence: int
    summary: str
    evidence: list[str] = field(default_factory=list)