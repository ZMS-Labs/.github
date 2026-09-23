# ZMS Labs documentation standard

Whichever ZMS Labs repository you open, its README should answer the same basic questions. How much detail it gives, the terms it uses and how it looks should fit the project.

## The README answers the first questions

A useful README answers:

1. Purpose and audience: what the project does, the problem it addresses, and its scope.
2. Current state: released, experimental, a fork, a mirror or archived, plus the main limitations and where the status information comes from.
3. A safe starting point: prerequisites and a supported first task, or an orientation guide when running the project is not appropriate.
4. How to check a change: relevant development and verification instructions, with the limits of those checks made clear.
5. Where to go next: a short map to the authoritative usage, design, architecture, operation, or evidence guides.
6. Participation and licensing: contribution instructions, upstream relationships, and the license that actually applies.

Use a clear title, a concrete opening paragraph, and descriptive links. Add a short navigation section when the README is long. Keep extensive runbooks and historical records behind those links.

## Adapt the structure to the repository

| Repository kind | Additional guidance |
|---|---|
| Application or library | Supported use, installation or local development, an example, and verification |
| Experimental project | What exists today, what is planned, how to exercise the implemented slice, and known limits |
| Infrastructure or configuration | What this repository is the source of truth for, how to look around without changing anything, how to make and check a change, and links to the step-by-step operating guides |
| Research or methods | The question, assumptions, artifacts, evidence limits, and how to reproduce or evaluate a claim |
| Skills or agent workflows | When to use the method, what context it needs, what useful output looks like, when to stop, and limits that depend on which AI tool runs it |
| Fork | Upstream attribution, the local purpose and difference, and where issues or contributions belong |
| Mirror or archive | What is preserved, the source or successor, and whether changes are accepted |
| Documentation or showcase | Reading paths and how to maintain the material; no invented install or runtime instructions |

An empty or archived repository may have a recorded documentation exception instead of an artificial guide. Do not unarchive or publish a repository merely to satisfy a template.

## Keep information accurate

- Verify commands and paths against current source. Do not copy a command because it works in another project.
- Separate implemented behavior from goals, and source checks from live-system observations.
- Preserve historical evidence as historical. Link to current guidance without rewriting a past result as a current claim.
- Keep one authoritative explanation and link to it. Avoid copies that will drift.
- When an answer is unknown, say what is known and where verification belongs.
- A recent edit date is not evidence that every statement was revalidated.

## Written voice

Identity-bearing surfaces are the organization profile, the openings of featured repository READMEs, the showcase About text and featured-project leads. AI tools may draft them. Zach Stern reviews every change to them before it merges and rewrites or approves each first-person sentence, since those sentences speak for him. Process and governance pages, such as Support, Contributing and this standard, use a neutral voice and don't need his phrasing. The one first-person line on them is his contact line at the end of Support.

- Each identity-bearing surface carries at least one sentence only this project could produce: a concrete memory, number, decision, or failure. A sentence that could be pasted onto any other project gets rewritten.
- Don't repeat a qualification in the same words. Keep a material limit next to each claim it bounds, and let the page's status or evidence section carry the general limit once.
- Vary headline forms. A plain single-line title is fine.
- Give a coinage, a term a project made up, a one-line gloss at first use on the entry surface that introduces it.

## Respect the publication boundary

Public documentation must stand on public, intentionally disclosed information. Do not expose the names of private projects that have not been deliberately made public, internal links, machine identities, inventories, network topology, credentials, personal data, or confidential operational details. Prefer generalized explanations and made-up examples.

Private documentation can link to the operational detail its readers need, but the front page should still orient readers before presenting those details. Keep sensitive information in the appropriate controlled source rather than duplicating it.

A decision to change visibility is separate from a documentation improvement. Review contents, history, metadata, assets, automation, and access implications before proposing publication.

## Use visuals to explain

For new or changed diagrams, screenshots, charts, badges and illustrations, follow the [visual documentation review](visual-documentation-review.md). Check the rendering at the widths and in the themes the page supports, and use generated artwork only for labeled illustrations, never as evidence or as an exact technical diagram.

## Verify and maintain

For a documentation change, check relative links and anchors, confirm external references where needed, run whitespace checks, review the diff for unintended information, and inspect rendered layouts when they change. Run relevant existing checks; a prose edit does not require inventing a test framework.

Update documentation with the behavior it describes. A short, accurate guide is more useful than a comprehensive-looking one that cannot be trusted.

## Review cadence

Public-facing pull requests get one round of automated review. Each finding gets a reply in its thread, either fixed or declined with a reason. A finding that arrives after a merge still gets a reply, and any fix goes in a follow-up pull request. Never resolve a finding without a reply.

The plan is to have the public pages critically reviewed about once a quarter. The first review ran in September 2026.
