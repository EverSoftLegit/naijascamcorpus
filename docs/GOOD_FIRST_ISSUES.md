# Good first issues

Concrete starter tasks for new contributors. You do not need to know Git,
Python, or machine learning to help — several of these are review and writing
tasks. Pick one, read `CONTRIBUTING.md`, and open a draft pull request or a
discussion. Each task notes the skills it suits and the review it needs.

Issues are for project work only. Never submit a real scam report, victim
evidence, personal data, or an accusation about an identifiable person or
organisation.

## No code required

1. **Review a scam-family definition.** Read `taxonomy/scam-families.json` and
   suggest a clearer definition or a missing distinction for one family. *(Cybersecurity, fraud, civil-society reviewers.)*
2. **Review language tags for one region.** Check the `languages` tags on records
   for a region you know (for example `sw-KE`, `pcm-NG`, `am-ET`) and flag anything
   that looks wrong or too coarse. *(Linguists, native speakers.)*
3. **Propose a new persuasion tactic or requested action.** If a real-world pattern
   you know is not expressible with the current `taxonomy/tactics.json` or
   `taxonomy/requested-actions.json`, open a taxonomy proposal with a rationale. *(Researchers, practitioners.)*
4. **Improve the annotation guide.** Suggest a clearer explanation or a worked
   example for a field in `docs/ANNOTATION_GUIDE.md`. *(Documentation, education.)*
5. **Add a research reference.** Contribute a citation to `docs/LANDSCAPE.md` for an
   African-context scam study, with a one-line note on what it covers. *(Students, researchers.)*
6. **Review the public-education wording.** Suggest plain-language improvements to the
   README so a non-technical reader understands what the project is and is not. *(Civil-society, communications.)*

## Small code or data tasks

7. **Author one synthetic record.** Follow `docs/ANNOTATION_GUIDE.md`, copy
   `templates/record.template.json`, and add one abstract, clearly fictional record
   for a family or region that is thin. Run `python scripts/validate_all.py` and
   regenerate the manifest. *(Needs independent + safety/privacy review.)*
8. **Add a coverage dimension.** Extend `scripts/coverage_report.py` to also report,
   for example, the count of records per country. *(Beginner Python.)*
9. **Add a baseline feature.** Try character n-grams in `benchmark/baseline.py` and
   report whether the leave-one-out score changes. Keep it deterministic and
   dependency-free. *(Beginner ML / Python.)*
10. **Tighten a test.** Add a unit test for an edge case you think is uncovered in
    `tests/`. *(Beginner Python.)*

## Review gates (so you know what to expect)

- A documentation or tooling change needs a maintainer review and passing CI.
- A data change (a new or edited record) also needs an independent reviewer and a
  safety/privacy review before it can merge. Any safety objection pauses the pull request.
