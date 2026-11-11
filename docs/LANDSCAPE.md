# Existing Landscape and Differentiation

**Purpose:** record why the project exists alongside existing work. This is a snapshot, not an exhaustive competitor analysis.

## Relevant initiatives and resources identified during founding research

- **Prembly FraudLens:** reported in March 2026 as an open fraud-intelligence database aimed at financial institutions, fintechs, banks, and businesses, with an ambition to expand across Africa. This means NaijaScamCorpus should not position itself as another generic fraud-intelligence bank. [TechCabal coverage](https://techcabal.com/2026/03/10/nigerias-prembly-launches-shared-open-source-database/).
- **UbuntuScamBank:** a community-powered scam reporting and intelligence platform with researcher access. This means we should not duplicate a public incident-reporting portal. [Project site](https://scambank.ubuntubridgeinitiatives.org/).
- **Africa Phishing IOCs:** a community repository describing phishing indicators and African-targeted patterns. This means a URL/IOC list is not a distinctive core product. [LANfrica catalogue record](https://lanfrica.com/en/record/github-abdul-itas-africa-phishing-iocs).
- **MOZ-Smishing:** a 2025 AfricaNLP research benchmark on mobile-money smishing in Mozambique, using Portuguese messages and local linguistic context. [ACL Anthology paper](https://aclanthology.org/2025.africanlp-1.23/).
- **Nigerian ExAIS SMS Spam dataset:** a Nigerian SMS corpus collected from volunteers with African-English context. Its repository documentation notes that the original collection contains sensitive metadata fields, illustrating why privacy and field minimisation must be central. [Repository](https://github.com/AbayomiAlli/SMS-Spam-Dataset).
- **Africa-smishing dataset:** a public dataset listed on Hugging Face with country, language, scam type, and other annotations. Its provenance, permissions, and suitability should be independently assessed before reuse; the project should not assume that a public dataset can be copied or redistributed. [Dataset page](https://huggingface.co/datasets/electricsheepafrica/africa-smishing).
- **Sheng-English Phishing Corpus:** a Kenya-focused corpus for low-resource, code-mixed language phishing research. [LANfrica catalogue record](https://lanfrica.com/en/record/a-sheng-phishing-corpus-for-low-resource-cybersecurity-nlp).
- **PhishTank:** a well-established phishing-verification community service operated by Cisco Talos. We should not recreate generic phishing URL reporting and verification. [FAQ](https://phishtank.org/faq.php).

## Strategic gap to test

The opportunity is not “no one has collected African scam messages.” Existing datasets and platforms demonstrate otherwise.

The hypothesis worth testing is that contributors need a **neutral, independently governed, cross-country research commons** with:

1. a versioned taxonomy that can describe scam patterns across channels and languages;
2. record-level provenance and confidence, separating a report from a verified fact;
3. explicit rights, privacy, re-identification, and safety review;
4. synthetic-first examples and safe abstraction rather than publishing raw victim material;
5. regional and language review pathways;
6. reproducible dataset cards, benchmark definitions, and correction history;
7. an open contribution model that welcomes non-code expertise.

This is a positioning hypothesis, not a proven market gap. The first public design review should ask existing researchers and maintainers what is missing and what should be interoperable rather than duplicated.

## Positioning statement

NaijaScamCorpus is a community-governed research and benchmarking commons for responsibly describing scam patterns in African digital contexts. It complements reporting portals, commercial fraud platforms, IOC feeds, and individual academic corpora; it does not replace them.

## Landscape review obligations

Before each major release:

- search for new African datasets and initiatives;
- check dataset licences and source conditions;
- document overlap and interoperability opportunities;
- update this page with dated findings;
- avoid claims such as “the first,” “the only,” or “the largest” unless independently substantiated.
