# ADR-0001: Project Positioning and Initial Data Boundary

- **Status:** Accepted for foundation stage
- **Date:** 2026-11-10
- **Decision owners:** Founding maintainers (interim)

## Context

Existing services and datasets already address fraud intelligence, scam reporting, phishing indicators, and African-language smishing research. A generic reporting portal or URL list would duplicate existing efforts and create avoidable operational and privacy risks.

## Decision

Position NaijaScamCorpus as an independent, Africa-wide, multilingual scam-pattern research and benchmarking commons. The unit of analysis is a pattern, not a victim or suspect. The initial public release is synthetic-only, supplemented by taxonomy, schemas, methodology, and citations to suitable public sources.

No real-world incident submissions will be accepted through GitHub. Any future admission of non-synthetic records requires governance maturity gates, source-rights review, privacy/safety review, and a private correction/takedown route.

## Consequences

- Slower initial dataset growth, but a safer and more defensible foundation.
- More opportunities for non-code contributors.
- The project's value depends on annotation quality, provenance, regional/language participation, and external reuse—not raw record volume.
- The working name requires a brand review because the intended scope is Africa-wide.
