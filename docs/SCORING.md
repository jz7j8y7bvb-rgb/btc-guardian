# Bitcoin Guardian Scoring

Current Version

The Guardian Engine starts from a neutral score of 50.

Every indicator contributes evidence.

Bullish indicators increase the score.

Bearish indicators decrease the score.

Current weights are configurable in config/scoring.py.

Future versions will normalize the score based on:

- indicator weight
- indicator confidence
- total available evidence

This will make the score comparable even after adding more indicators.