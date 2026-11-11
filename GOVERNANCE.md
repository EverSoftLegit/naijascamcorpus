# Governance and Decision-Making

**Status:** Founding model v0.1

## 1. Governance design

NaijaScamCorpus is an independent open-source community. The repository is a public collaboration space, not the legal owner of contributors' rights or a substitute for a legal entity. At inception, the project has no claim to represent the African Union, any national authority, regulator, bank, law-enforcement body, or the African public as a whole.

The governance model separates project direction, technical maintenance, and safety review. No single person should control all three.

## 2. Proposed governance bodies

### 2.1 Steering Council

**Size:** 5–7 members once the founding cohort is established.

**Responsibilities:** mission, priorities, budget transparency, appointments, dispute escalation, annual review, and public accountability.

**Composition goal:** geographic and disciplinary diversity. Seek representation across African regions and include research, civil society/community safety, language expertise, and technical practice. Do not claim continental representation merely because members are from several countries.

**Term:** 12 months, renewable once consecutively; stagger initial terms where practical.

### 2.2 Maintainers

Maintain repository health, triage issues, review code and documentation, operate release workflows, and enforce repository policies. Maintainers cannot waive privacy or safety requirements.

### 2.3 Data Standards and Research Group

Maintains the schema, taxonomy, annotation handbook, dataset cards, and research-quality criteria. Includes researchers, data stewards, language reviewers, and domain specialists.

### 2.4 Safety and Data Governance Reviewers

Review source rights, privacy, re-identification risk, defamation risk, harmful operational detail, vulnerable-person implications, and withdrawal requests. This function may place a publication hold. It should be independent of the submitter and dataset author.

### 2.5 Regional and Language Working Groups

Propose regional context, language labels, translation conventions, and culturally appropriate examples. Groups must document dialect and language limitations rather than asserting that one contributor speaks for an entire community.

## 3. Founding phase

Until a 5–7 person Council is appointed, the founding maintainers may administer routine repository operations. During this interim period:

- all public data additions require two independent reviews;
- at least one reviewer must be responsible for privacy/safety review;
- the submitter cannot be the sole approver;
- any unresolved safety objection blocks publication;
- decisions affecting scope, licensing, or governance must be documented in a decision record;
- the interim maintainers must publish a call for founding contributors and a governance review date.

## 4. Decision classes

| Decision | Required approval |
|---|---|
| Typo, formatting, non-substantive docs | One maintainer |
| Code change with no data-policy impact | One maintainer plus passing CI; two approvals preferred |
| Taxonomy or schema change | Two reviewers, including one Data Standards reviewer |
| Public dataset record or dataset release | Two independent approvals, including a Safety/Data Governance reviewer |
| Material licence or data-policy change | Steering Council; 14-day public review |
| Charter or governance amendment | Two-thirds of Council after 14-day public review |
| Emergency removal for privacy or safety | Any designated safety reviewer may temporarily restrict; Council reviews promptly |

No silence should be treated as approval for a sensitive data release.

## 5. Public review and decision records

Material proposals should remain open for at least 7 days; charter, licensing, and policy changes for at least 14 days. Decisions must record the proposal, alternatives, decision, rationale, conflicts disclosed, and review date. Store records under `docs/decisions/`.

## 6. Conflict of interest

Contributors and reviewers must disclose a material interest. Examples include employment by a named organisation involved in a proposed record, paid work for a vendor whose product is being evaluated, authorship of a dataset under review, or personal involvement in a reported incident. Conflicted individuals may provide factual context but must not approve the affected decision.

## 7. Appeals, corrections, and removal

Any person may request correction or removal of a public record without posting private information in an issue. The project must provide a private contact route before accepting non-synthetic data. Until that route exists, the corpus must remain synthetic/public-source only. Safety concerns can be raised through the repository security contact after it is configured.

A record may be corrected, withdrawn, or removed when its source rights are unclear, a privacy risk is identified, its claim is materially inaccurate, or publication creates disproportionate harm. Dataset release notes should record the change without repeating the harmful material.

## 8. Maintainer appointment and removal

Appointments are based on sustained contributions, sound judgement, respectful conduct, and capacity to serve. The Council appoints maintainers by majority vote. A maintainer may be suspended for urgent safety reasons pending review. Removal requires a documented process, an opportunity to respond, recusal of conflicted decision-makers, and a two-thirds Council vote.

## 9. Funding and independence

Publish material funding and in-kind support. Do not sell exclusive access to community submissions. Funders cannot dictate record acceptance, conclusions, benchmark outcomes, or takedowns. Any commercial service using the dataset must comply with the applicable licence and attribution requirements.

## 10. Governance maturity gates

Before moving from synthetic examples to a real-world corpus, the project must have: (1) named privacy/safety reviewers; (2) a documented lawful sourcing standard; (3) a private correction/removal route; (4) jurisdictional legal review for planned sources and processing; (5) record-level licence and provenance controls; and (6) a retention and incident-response procedure.
