# NaijaScamCorpus

**Understand scams. Share intelligence. Protect communities.**

NaijaScamCorpus is an independent, Africa-wide, multilingual research and benchmarking commons for understanding scam patterns and social engineering across African digital communities.

> **Important:** This repository is not a victim-reporting service, law-enforcement portal, fraud verification service, or live threat-intelligence feed. Do not submit real victim evidence, personal data, active malicious URLs, credentials, account details, or accusations about identifiable people or organisations.

## Why this project exists

Scam patterns are shaped by local payment rails, languages, institutions, social norms, and communication channels. Research and defensive tools need datasets that represent those contexts without exposing victims or turning unverified allegations into public claims.

We aim to publish carefully governed, traceable, privacy-preserving pattern annotations, controlled taxonomies, synthetic examples, and reproducible evaluation benchmarks. The initial release contains synthetic examples only.

## What makes this project different

We are not trying to become another scam-reporting portal or generic phishing URL list. Our focus is:

- **African-context taxonomy:** comparable scam-family, channel, persuasion, and requested-action labels.
- **Multilingual coverage:** local languages, dialects, transliteration, and code-switching represented transparently.
- **Provenance:** every public record has a traceable source basis and clear confidence status.
- **Safety by design:** no raw victim submissions or personal data in public GitHub workflows.
- **Research utility:** versioned schemas, dataset cards, evaluation guidance, and reproducible benchmarks.
- **Community governance:** transparent review, corrections, licensing, and contributor credit.

## Current status

**Stage:** Foundation / pre-release. **Dataset:** synthetic examples only. **No real-world case corpus is being claimed.**

The name *NaijaScamCorpus* is a working name. The intended scope is Africa-wide; a public-brand review is required before the launch announcement because “Naija” may be read as Nigeria-only.

## Start here

- [Founding Charter](CHARTER.md)
- [Governance](GOVERNANCE.md)
- [Data Governance & Safety](DATA_GOVERNANCE.md)
- [Contribution Guide](CONTRIBUTING.md)
- [Annotation Guide](docs/ANNOTATION_GUIDE.md)
- [Dataset and Content Licensing](DATA_LICENSE.md)
- [Project Roadmap](ROADMAP.md)
- [Existing Landscape & Differentiation](docs/LANDSCAPE.md)
- [GitHub Launch Checklist](docs/GITHUB_LAUNCH.md)
- [Data Schema](schemas/scam-pattern.schema.json)
- [Reproducible Benchmark](benchmark/README.md)

## Ways to contribute

You do not need to write code to help. We welcome:

1. Taxonomy and methodology review.
2. African-language and code-switching expertise.
3. Research references and literature reviews.
4. Documentation and community education.
5. Data-quality tooling and benchmark engineering.
6. Privacy, safeguarding, and legal-policy review.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, and see [good first issues](docs/GOOD_FIRST_ISSUES.md) for concrete starter tasks. GitHub issues are for project improvements only, **not scam reports**.

## Non-goals

NaijaScamCorpus will not:

- collect or publish raw victim messages, screenshots, emails, transaction receipts, phone numbers, account numbers, identity documents, or private conversations;
- publish unverified lists of people, phone numbers, accounts, domains, or businesses as alleged scammers;
- provide live malware, phishing, or operational infrastructure feeds in the initial project;
- make automated claims that a person, business, payment, or website is fraudulent;
- replace banks, regulators, data-protection authorities, law-enforcement agencies, or official reporting channels;
- train or release a model that makes consequential fraud accusations without robust evaluation and human review.

## Project principles

People before data. Minimise collection. Preserve uncertainty. Verify before publication. Make correction possible. Credit contributors. Protect vulnerable people. Share only what is safe and lawful to share.

## Licence

- Source code and tooling: [MIT](LICENSE).
- Original project documentation, taxonomies, and explicitly marked project-authored dataset records: [CC BY 4.0](DATA_LICENSE.md), unless a file states otherwise.
- Third-party material remains under its original licence and must not be copied into this repository without permission.

See [DATA_LICENSE.md](DATA_LICENSE.md) before reusing any dataset release.

## Contact and safety

For project governance or dataset questions, open a project-discussion issue without including real incident details. For a security vulnerability in repository tooling, follow [SECURITY.md](SECURITY.md). **Do not send victim evidence through GitHub.**
