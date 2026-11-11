# Data Governance, Privacy, and Safety Policy

**Default rule: when in doubt, do not submit or publish the material.**

## 1. Purpose and boundary

This policy governs any information proposed for the public NaijaScamCorpus repository. It is designed for an open GitHub environment where content may be copied, indexed, cached, forked, and difficult to fully retract.

The repository is not a victim-reporting channel. Do not open an issue or pull request containing real incident evidence.

## 2. Accepted content at launch

Permitted at launch:

- clearly labelled synthetic examples;
- taxonomies and annotation guidance;
- summaries of academic publications or public advisories with citations;
- aggregate, non-identifying statistics where licence and re-identification risks are assessed;
- reproducible evaluation methods and code.

Future real-world pattern abstractions may be considered only after the maturity gates in [GOVERNANCE.md](GOVERNANCE.md) are met.

## 3. Prohibited content

Never submit:

- victim names, usernames, phone numbers, email addresses, physical addresses, dates of birth, identity numbers, bank or wallet account numbers, card numbers, payment references, or biometric data;
- passwords, OTPs, API keys, authentication tokens, recovery codes, or session data;
- private messages, chat exports, call recordings, screenshots, emails, receipts, identity documents, or case files;
- raw user-submitted phishing messages unless a separately approved data-collection protocol explicitly authorises a safe, rights-cleared and privacy-reviewed derivative; this is not enabled at launch;
- clickable malicious URLs, active malware, exploit payloads, or instructions that enable abuse;
- unverified allegations identifying a person or organisation as criminal or fraudulent;
- data obtained through unauthorised access, deception, breach of confidentiality, or violation of platform terms or applicable law.

Do not assume that removing a name makes a record anonymous. Text, dates, amounts, locations, narrative details, and rare combinations can re-identify a person.

## 4. Data minimisation

Every field must have a defined research purpose. Do not collect victim-level demographics, exact financial losses, exact incident timestamps, transaction IDs, device identifiers, or precise locations in the public corpus. If a research question appears to require sensitive fields, propose an aggregate or synthetic alternative and obtain independent review before collection.

## 5. Provenance and confidence

Each public record must identify:

- whether it is synthetic or derived from a cited public source;
- source type and a stable public citation where available;
- source publication date, when known;
- the transformation or abstraction method;
- confidence and known limitations;
- review state and privacy-review status;
- the licence applying to the record.

A public report is evidence that a report was published; it is not automatically proof that every assertion in that report is true. Do not convert unverified reports into verified facts.

## 6. Safe publication levels

| Level | Description | Public repository? |
|---|---|---|
| S0 | Synthetic or public taxonomy material, no real person data | Yes, after review |
| S1 | Abstract pattern from a suitable public source, no operational indicators or identifiers | Potentially, after source-rights and privacy review |
| S2 | Raw or lightly redacted victim/incident material, live indicators, or potentially identifying details | No |
| S3 | Credentials, financial identifiers, identity documents, private communications, malware, or high-risk operational detail | Never |

S2 and S3 must not be uploaded to GitHub, even to a private repository, issue, discussion, gist, or pull request. Deletion from Git history does not guarantee erasure from forks or caches.

## 7. Redaction and synthetic examples

Synthetic examples must be invented from general patterns, not copied from an identifiable real victim's message. Use reserved example domains such as `example.com` and placeholder values. Do not include real phone numbers, account identifiers, or working links. Label every synthetic record explicitly.

## 8. Third-party material and rights

A source being publicly accessible does not mean it may be republished. Prefer citation and abstract description over copying source text. Review copyright, database rights, terms of use, privacy obligations, and licence compatibility before inclusion. Do not scrape private groups or closed platforms.

## 9. Re-identification and harm review

Reviewers should ask whether a motivated reader could identify a victim, a private individual, a small business, or a specific incident from the record or by combining it with other sources. Consider vulnerable groups, small communities, rare languages, exact dates, and unusual transaction narratives. Remove or generalise details when risk is not clearly low.

## 10. Corrections, takedowns, and incidents

The project will create a private correction/takedown contact before admitting non-synthetic records. When a credible privacy or safety concern is raised, suspend the affected record or release while reviewing. Preserve only the minimum administrative record necessary to track the action. Do not reproduce the harmful material in the takedown discussion.

If sensitive data is accidentally committed, notify maintainers immediately through the configured private channel. Maintainers should restrict access where possible, remove the material from the current branch and history where feasible, assess forks/caches, rotate exposed secrets where relevant, and document the incident without repeating the data. Git history rewriting alone is not a complete deletion guarantee.

## 11. Cross-border context

The project is Africa-wide, but data-protection obligations are jurisdiction-specific and may apply based on the source, people affected, contributors, hosting, or processing activities. This policy is a project safeguard, not legal advice or a substitute for local legal review. The African Union Data Policy Framework provides a useful continental policy reference, but it does not replace national law. See [Landscape & References](docs/LANDSCAPE.md).

## 12. No automated accusation

Dataset labels describe a content pattern or reported tactic. They must not be interpreted as a legal finding that a named person or organisation committed fraud. Models trained on the corpus must be evaluated for false positives, language bias, and harm before deployment.
