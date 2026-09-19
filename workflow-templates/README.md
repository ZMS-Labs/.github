# Workflow templates

GitHub offers these templates when a repository maintainer chooses **Actions → New workflow**. Selecting a template copies it into that repository; later template updates do not silently update existing copies.

| Template | What it does | Requirements |
|---|---|---|
| [Secret scan](gitleaks.yml) | Scans the checked-out Git history with Gitleaks and redacts findings in logs | GitHub-hosted Linux runner and network access to public Go modules; no third-party service credential |

The default-branch placeholder is replaced by GitHub when the template is copied. The workflow grants read access to repository contents, pins action revisions and the scanner version, and limits each run to fifteen minutes. Review the copied workflow and its repository's rules before enabling it. A passing scan does not establish that all sensitive information has been removed.

To maintain the template, update the YAML and matching `.properties.json`, validate the resulting workflow after replacing `$default-branch` with a branch name, and keep its scanner steps consistent with this repository's [secret scan](../.github/workflows/secret-scan.yml). Action and scanner upgrades need fresh review and verification.
