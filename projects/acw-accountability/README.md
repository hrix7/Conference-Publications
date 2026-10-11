# Autonomous Cyber Systems Accountability Lab

**v0.1.0 · exploratory prototype · 11 October 2026**

Maintained by Hritika Adhikary. A computational starting point for human-control and civilian digital-harm research. This release contains independently implemented code and synthetic examples, not the manuscript or unpublished case ratings.

## Run

Python 3.10+; no third-party dependencies.

```bash
cd projects/acw-accountability
python mhc.py
python mhc.py --threshold 0.94 --output assessment.json
python -m unittest discover -s tests -v
```

The limited-control synthetic scenario scores **0.245**; the reviewed-defence scenario scores **0.915**. The incomplete scenario returns `insufficient_evidence`. These examples are constructed, not observed operations.

## Implemented

- Five-dimensional weighted control score, with validated inputs and weights.
- Explicit design-threshold comparison and JSON export.
- Override-weight sweep from 0.15 to 0.45 with proportional rescaling.
- Exact score range over all admissible weight vectors.
- Missing evidence retained as null rather than zero.
- Eight tests including mathematical properties and counterexamples.

| Dimension | Working interpretation | Illustrative weight |
|---|---|---:|
| Understand | Operators understand capabilities and limits | 0.25 |
| Predict | Behaviour is predictable in the assessed context | 0.25 |
| Override | Intervention can halt or correct actions | 0.30 |
| Time | Intervention can occur before harm | 0.10 |
| Audit | Decisions can be reconstructed | 0.10 |

These interpretations require observable scoring anchors before real cases are rated. This index is **not a probability of harm or legal compliance finding**. The configurable 0.87 threshold is illustrative and unvalidated. A defensive label alone confers no approval.

See [methodology](docs/METHODOLOGY.md), [roadmap](docs/ROADMAP.md), [conference notes](docs/CONFERENCE_NOTES.md), and [progress](docs/PROGRESS.md).

Next: source-backed case records containing operational mode, autonomy evidence, attribution evidence, harm category/severity/scope, control ratings, confidence, provenance and reviewer disagreement. No real-case ratings are included. Repository rights and release policies apply.
