# Annotation Guide (synthetic pattern records)

How to author one synthetic record. Read this with `CONTRIBUTING.md`,
`DATA_GOVERNANCE.md`, and the taxonomy files. Every record in the initial
release is **synthetic** — authored to illustrate a pattern, never copied from a
real message or incident.

## The one rule that matters most

A record describes a *pattern* at an abstract level. It must never contain:

- a real or invented brand, company, agency, person, or campaign name;
- a real or made-up URL, domain, phone number, account number, or address;
- a copy-ready message a reader could send to actually run a scam;
- any real victim content, screenshot text, or private conversation.

If an example reads like something you could paste and send, it is too concrete.
Describe what the pattern *does* ("asks the recipient to share a one-time code"),
not a working script.

## Field by field

Start from `templates/record.template.json`.

- **record_id** — `NSC-SYN-NNNN`, unique. Use the next free number.
- **record_version** — `1.0.0` for a new record; bump on later corrections.
- **record_type** — always `synthetic_pattern` in this release.
- **countries** — ISO 3166-1 alpha-2 codes for the *context* the pattern reflects. This is illustrative metadata, not a prevalence claim and not a victim location. Confirm with a regional reviewer.
- **languages** — language/locale tags (for example `en-NG`, `sw-KE`, `pcm-NG`). Tags are provisional until a language reviewer confirms them; see `taxonomy/languages.md`.
- **channel** — one value from `taxonomy/channels.json`.
- **scam_family** — one value from `taxonomy/scam-families.json`. If nothing fits, use `other` and explain in `limitations`.
- **impersonated_sector** — one value from `taxonomy/sectors.json`; `none` if no one is impersonated.
- **persuasion_tactics** — one or more from `taxonomy/tactics.json`. Pick what the pattern actually relies on; do not list every tactic.
- **requested_actions** — one or more from `taxonomy/requested-actions.json`: what the target is asked to do.
- **pattern_summary** — 20–1200 characters, plain description of the pattern.
- **synthetic_example** — 20–1200 characters, and it **must start with** `SYNTHETIC EXAMPLE:`. Keep it abstract (see the rule above).
- **source** — `source_kind` is `synthetic`; `reference` and `published_date` are `null`; `methodology` (20–1000 chars) says you authored it to illustrate the pattern and did not copy it.
- **confidence / review_status / privacy_review** — fixed values for synthetic records (`not_applicable_synthetic`, `approved_synthetic`, `passed`). A privacy reviewer confirms `passed`.
- **limitations** — at least one honest caveat (it is fictional; tags need regional confirmation; etc.).
- **record_license** — `CC-BY-4.0`.

## Before you open a pull request

Run the checks locally:

```bash
python scripts/validate_all.py      # consistency, schema, duplicates, manifest
python -m unittest discover -s tests
```

If you added or changed a record, regenerate the manifest and include it:

```bash
python scripts/make_manifest.py
```

A data pull request also needs an independent reviewer and a safety/privacy
review before it can merge (see `docs/GITHUB_LAUNCH.md`).
