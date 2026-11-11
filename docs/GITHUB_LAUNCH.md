# GitHub Launch Architecture and Repository Operations

## 1. Recommended repository identity

**Working repository name:** `naijascamcorpus`  
**Suggested description:** `An independent, Africa-wide, multilingual scam-pattern research and benchmarking commons.`

Because the intended scope is continental, review the public-facing name before announcement. Do not change the name silently after contributors begin using it; record the decision and provide redirects/aliases where possible.

## 2. Repository architecture

```text
naijascamcorpus/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── taxonomy_proposal.yml
│   │   ├── documentation.yml
│   │   └── config.yml
│   ├── workflows/
│   │   └── validate-data.yml
│   ├── CODEOWNERS
│   └── PULL_REQUEST_TEMPLATE.md
├── data/
│   └── v0.1/
│       ├── DATASET_CARD.md
│       ├── MANIFEST.sha256
│       └── synthetic/
│           └── records.jsonl
├── docs/
│   ├── decisions/
│   ├── ANNOTATION_GUIDE.md
│   ├── GITHUB_LAUNCH.md
│   ├── LANDSCAPE.md
│   ├── METHODOLOGY.md
│   └── RELEASE_CHECKLIST.md
├── benchmark/
│   ├── README.md
│   ├── baseline.py
│   ├── run_benchmark.py
│   └── results/
│       └── baseline-metrics.json
├── schemas/
│   └── scam-pattern.schema.json
├── scripts/
│   ├── check_duplicates.py
│   ├── check_taxonomy_consistency.py
│   ├── coverage_report.py
│   ├── lint_language_tags.py
│   ├── make_manifest.py
│   ├── validate_all.py
│   └── validate_records.py
├── taxonomy/
│   ├── channels.json
│   ├── countries.json
│   ├── languages.md
│   ├── requested-actions.json
│   ├── scam-families.json
│   ├── sectors.json
│   └── tactics.json
├── templates/
│   └── record.template.json
├── tests/
│   ├── test_benchmark.py
│   └── test_dataset.py
├── CHARTER.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DATA_GOVERNANCE.md
├── DATA_LICENSE.md
├── GOVERNANCE.md
├── LICENSE
├── README.md
├── ROADMAP.md
├── SECURITY.md
└── requirements-dev.txt
```

## 3. GitHub repository settings

Before public launch:

- Set repository visibility to public only after removing all secrets and non-public material.
- Add a clear description, website or community contact only when staffed, and Africa-wide topics.
- Enable Discussions for project design, research, language, and contributor questions.
- Disable blank issues; use structured issue forms for project work only.
- Enable private vulnerability reporting / GitHub Security Advisories.
- Protect `main`: require pull requests, passing CI, at least two approvals for data changes, dismiss stale approvals, require CODEOWNERS review, and restrict force pushes/deletions.
- Ensure administrators do not routinely bypass protections; document emergency exceptions.
- Enable Dependabot alerts and security updates where applicable.
- Keep workflow permissions read-only by default; do not expose secrets to untrusted pull requests.
- Add a monitored private contact for privacy/takedown requests before admitting non-synthetic records.
- Add country/language labels without assuming a contributor represents a whole country or language.

## 4. Suggested GitHub Discussions categories

- Announcements
- General and community
- Taxonomy and annotation
- Language and regional working groups
- Research and benchmark methods
- Governance proposals
- Help wanted / good first issue

Never use Discussions to collect incident reports or evidence.

## 5. Labels

Suggested labels: `good first issue`, `help wanted`, `documentation`, `taxonomy`, `schema`, `data-quality`, `language-review`, `regional-review`, `research`, `benchmark`, `privacy-review`, `safety-review`, `governance`, `needs-decision`, `blocked`.

## 6. Branch and release model

- `main`: reviewed and releasable content.
- Feature branches: short-lived, one purpose per pull request.
- Tags: `v0.1.0`, `v0.2.0`, etc. for tooling/schema releases.
- Dataset releases: `dataset-v0.1.0` or a separately documented dataset version, with a versioned dataset card and checksum manifest.
- Never silently rewrite a published dataset. Publish a corrected version and a change log; remove unsafe content promptly when required and explain the removal without reprinting it.

## 7. Review gates

A code PR may be merged after tests and required code-owner approval. A data PR also needs source-rights, provenance, licence, safety, and privacy review. Any safety objection pauses the PR. Dataset release must follow `docs/RELEASE_CHECKLIST.md`.

## 8. Contributor onboarding path

1. Read README and Charter.
2. Choose a non-code or technical contribution pathway.
3. Pick a `good first issue` or join a regional/language discussion.
4. Submit a small contribution with source and limitations.
5. Complete review and receive attribution if desired.
6. After sustained contribution, be considered for reviewer or maintainer roles.

## 9. First public announcement should wait for

- name/brand decision;
- at least three to five committed founding maintainers across different disciplines and at least three African regions;
- a monitored governance and privacy contact;
- repository protections and CI;
- approved Charter, Code of Conduct, and Data Governance Policy;
- a synthetic-only initial dataset card;
- no claim that the corpus contains real verified scam reports.
