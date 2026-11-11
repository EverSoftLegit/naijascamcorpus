# Annotation and Research Methodology (v0.1 draft)

## Unit of analysis

The unit is a **scam pattern**, not a victim, suspect, message sender, phone number, account, domain, or incident case. A pattern describes a recurring social-engineering or fraud mechanism at a level that supports research without exposing individuals.

## Annotation workflow

1. **Intake:** accept only synthetic examples and suitable public-source references under the current policy.
2. **Source review:** confirm that the source is suitable for citation and does not require copying protected or personal data.
3. **Abstraction:** describe the pattern without preserving unique narrative details or operational indicators.
4. **Annotation:** assign controlled taxonomy labels and language/country context only when supported.
5. **Independent review:** a second reviewer checks labels, source interpretation, uncertainty, and potential bias.
6. **Safety review:** check privacy, re-identification, defamation, and misuse risk.
7. **Publication:** assign version, licence, dataset card entry, and release history.

## Confidence levels

- `not_applicable_synthetic`: fictional example created for education/testing.
- `low`: limited source support; hypothesis or weakly described pattern.
- `medium`: credible source support but incomplete or non-independent corroboration.
- `high`: multiple credible, independent public sources or an authoritative public advisory support the pattern. This does not mean a named person is guilty or that every occurrence matches the pattern.

Confidence is about support for the pattern description, not certainty about an individual case.

## Language representation

Use BCP 47 language tags where practical. Record code-switching and transliteration separately from the main language label. Do not automatically infer language from country. A country may contain many languages, and a language may be used across multiple countries.

## Bias and limitations

Publicly documented scams are not a representative sample of all scams. Reporting rates, platform access, language resources, media coverage, and institutional transparency differ across countries. Dataset users must not interpret record counts as prevalence estimates unless a separate sampling methodology supports that claim.

## Model evaluation

Any benchmark must publish its sampling strategy, splits, class balance, label definitions, annotator process, language coverage, limitations, and known leakage risks. Keep near-duplicate examples across splits from inflating reported performance. Report per-language and per-region metrics where sample sizes support meaningful interpretation. Evaluate false positives as well as false negatives.
