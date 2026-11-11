# Security Policy

## Scope

This policy covers security vulnerabilities in the repository's code, CI workflows, package/release process, and project-controlled infrastructure. It is not a channel for reporting scams or submitting victim evidence.

## Reporting a vulnerability

Do not open a public issue for an undisclosed vulnerability. Use GitHub Security Advisories / private vulnerability reporting after that feature is enabled for the repository. Until then, the project must configure a monitored private security contact before accepting code that processes external submissions.

Do not attach victim records, credentials, or unrelated personal data to a vulnerability report.

## Response goals

- Acknowledge a credible report within 7 calendar days.
- Triage severity and scope within 14 calendar days.
- Coordinate remediation and disclosure with the reporter.
- Credit the reporter where they consent.

These are target service levels, not a guarantee until maintainers and contact channels are formally appointed.

## Safe handling

- Keep secrets out of source control and CI logs.
- Pin and review dependencies.
- Use least-privilege GitHub tokens and workflow permissions.
- Do not add telemetry or upload dataset contents by default.
- Treat all contributed data as untrusted input.
