# Contributing to NaijaScamCorpus

Thank you for helping improve African-context scam research. Contributions are welcome from researchers, language experts, students, community educators, developers, privacy professionals, and practitioners.

## Before contributing

1. Read the [Founding Charter](CHARTER.md), [Code of Conduct](CODE_OF_CONDUCT.md), and [Data Governance Policy](DATA_GOVERNANCE.md).
2. Check existing issues and the taxonomy before proposing a duplicate.
3. For a substantial change, open a discussion or proposal first.
4. Keep pull requests narrow and explain the purpose, evidence, risks, and limitations.

## Important: do not report a real scam here

GitHub issues, discussions, pull requests, commit messages, and repository files are public or may be copied. **Never upload victim evidence, raw messages, screenshots, phone numbers, account details, transaction references, credentials, private links, or live malicious URLs.**

At launch, contributions containing real-world incident data are not accepted. Use synthetic examples or cite a suitable public source and submit a non-identifying pattern abstraction for review.

## Contribution pathways

### Research and sourcing

- Find and cite relevant academic work, public advisories, and public reports.
- Summarise methodology and limitations; do not copy protected datasets or text.
- Identify regional coverage gaps without making unsupported claims.

### Language and cultural review

- Review language tags, transliteration, code-switching, idioms, and translations.
- State dialect/region and the limits of your expertise.
- Do not claim a translation represents every speaker of a language.

### Taxonomy and data quality

- Propose a new label only when existing categories do not fit.
- Provide a definition, positive examples (synthetic), exclusions, and confusion with nearby labels.
- Keep labels mutually understandable and avoid unnecessary granularity.

### Engineering

- Improve schema validation, tests, documentation tooling, benchmark reproducibility, and accessibility.
- Avoid adding telemetry, network calls, or external dependencies without a clear need and review.

### Community education

- Develop plain-language explanations and defensive guidance.
- Keep guidance practical, non-alarmist, accessible, and available for localisation.

## Data submission requirements

Every proposed record must:

- validate against `schemas/scam-pattern.schema.json`;
- be synthetic or grounded in a permitted public source;
- include provenance, language, country context where known, and limitations;
- carry the correct record-level licence;
- pass privacy and safety review;
- avoid operational details that enable abuse;
- use an appropriately cautious confidence value.

The initial corpus is synthetic. Do not add real-world-derived records until the Steering Council publishes an explicit change to the data-collection policy.

## Pull request process

1. Fork the repository and create a descriptive branch.
2. Make one logically scoped change.
3. Run `python scripts/validate_records.py` and `python -m unittest discover -s tests`.
4. Include tests for tooling changes.
5. Complete the pull-request template, including provenance/licence/privacy questions where relevant.
6. Sign off commits using `git commit -s` to indicate agreement with the Developer Certificate of Origin (DCO).
7. Respond to reviewer feedback. Do not merge your own sensitive data contribution.

## Review expectations

- Routine documentation changes: one maintainer.
- Taxonomy/schema changes: two reviewers, including a data standards reviewer.
- Dataset record or release changes: two independent approvals, including a privacy/safety reviewer.
- A safety objection pauses publication until resolved.

## Commit style

Use clear, imperative summaries, for example:

- `docs: clarify language annotation guidance`
- `taxonomy: add payment-redirection pattern`
- `data: add reviewed synthetic example`
- `test: cover duplicate record identifiers`

## Recognition

Contributors may opt to be credited in release notes, `CONTRIBUTORS.md`, or the relevant research output. Do not include private contact details. Contributors may use a public handle or request no attribution.
