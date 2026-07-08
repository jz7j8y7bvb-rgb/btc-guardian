from dataclasses import dataclass


@dataclass(slots=True)
class GuardianScore:
    score: int
    recommendation: str
    confidence: int
    explanation: list[str]