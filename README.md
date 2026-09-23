# ZMS Labs public profile and shared guidance

<!-- ZMS-ESTATE:BEGIN -->

Status: Maintained.

<!-- ZMS-ESTATE:END -->

This repository contains the [ZMS Labs organization profile](profile/README.md) and public contribution guidance. The profile appears on the organization's GitHub Overview page.

| Start here | Purpose |
|---|---|
| [Organization profile](profile/README.md) | Introduction and selected public work |
| [Documentation standard](docs/documentation-standard.md) | A consistent reading experience across different kinds of projects |
| [Visual documentation review](docs/visual-documentation-review.md) | What a diagram, chart or screenshot has to get right before it is published |
| [Contributing](CONTRIBUTING.md) | Shared contribution guidance where a project supplies no override |
| [Support](SUPPORT.md) | Where to ask a question, and how to report a vulnerability privately |
| [Workflow templates](workflow-templates/README.md) | A starter secret-scan workflow offered through GitHub |
| [Profile artwork](profile/assets/README.md) | Source, licensing, and reproducible assets |

Project-specific documentation and contribution policies take precedence. A repository's license applies to that repository; this repository does not supply a default license for other projects.

## Maintaining this repository

Edit the profile in `profile/README.md` and shared guidance in the files linked above. Use only public, verified information and links. Keep private project details, personal information, operational inventories, and internal addresses out of the public tree and its history.

Check changed links and images, run `git diff --check`, and inspect desktop and mobile rendering before publishing. The Gitleaks workflow scans the complete Git history with redacted output. A passing secret scan does not replace a contextual privacy review.
