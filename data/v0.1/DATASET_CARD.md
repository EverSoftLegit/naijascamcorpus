# NaijaScamCorpus Synthetic Pattern Dataset v0.1.0

## Summary

A small, synthetic-only starter set for validating the initial scam-pattern schema and taxonomy. It is not a collection of real scam messages, reports, or verified incidents.

## Intended uses

- schema and annotation workflow testing;
- contributor onboarding;
- taxonomy discussion;
- educational demonstrations;
- prototyping research code, with clear disclosure that examples are synthetic.

## Out-of-scope uses

- estimating scam prevalence;
- attributing criminal conduct to a person or organisation;
- training or evaluating a production fraud classifier as though this were representative real-world data;
- operational blocking or enforcement decisions.

## Composition

- Records: 48 synthetic examples.
- Scam families: all twelve families in the taxonomy are represented with exactly 4 records each, a balanced set for multi-class tooling.
- Countries referenced (illustrative metadata only): NG, GH, KE, ZA, UG, TZ, ET, SN, and others across several African regions.
- Languages: English variants plus illustrative code-switch and local-language tags (for example Nigerian Pidgin, Swahili, Hausa, Yoruba, Igbo, Amharic, French, Afrikaans, Zulu); linguistic review is still required and tags are provisional.
- Channels: SMS, messaging apps, email, voice calls, social media, websites, online ads, and cross-channel ("multiple").
- Source type: synthetic for every record.
- Confidence: not applicable to synthetic examples.

## Collection and curation

All examples were authored for the project and are not copied from a victim message or an actual case. They intentionally avoid real people, phone numbers, account identifiers, active URLs, and named brands.

## Limitations

The dataset is small, fictional, and not representative of any country's scam landscape. It must not be used to train or validate claims about real-world detection performance. The included benchmark (`benchmark/`) is a reproducibility harness that measures a baseline on these synthetic records only; its scores say nothing about real-world accuracy.

The baseline's confusion matrix shows the expected overlaps for a bag-of-words model on short text: families that share vocabulary and requested actions — for example account-takeover and impersonation, or the several families that ask the target to "send money" — are the ones most often confused. This reflects genuine semantic overlap between scam families, not a labelling error, and is a reason the taxonomy records more than one dimension (family, tactic, requested action, sector) per record rather than relying on the family alone.

## Licence

CC BY 4.0 for these project-authored synthetic records. See the repository's `DATA_LICENSE.md`.

## Citation

NaijaScamCorpus Community. (2026). *NaijaScamCorpus Synthetic Pattern Dataset v0.1.0*. Project pre-release. Cite the exact release tag and dataset card.
