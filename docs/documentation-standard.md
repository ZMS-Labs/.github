# A consistent documentation experience

Consistency means a reader can find the same essential answers across projects. The amount of detail, terminology, and visual identity should suit the project.

## The README answers the first questions

A useful README establishes:

1. **Purpose and audience:** what the project does, the problem it addresses, and its scope.
2. **Current state:** released, experimental, a fork, a mirror, or archived; material limitations and the authority for status claims.
3. **A safe starting point:** prerequisites and a supported first task, or an orientation guide when running the project is not appropriate.
4. **How to check a change:** relevant development and verification instructions, with the limits of those checks made clear.
5. **Where to go next:** a short map to the authoritative usage, design, architecture, operation, or evidence guides.
6. **Participation and licensing:** contribution instructions, upstream relationships, and the license that actually applies.

Use a clear title, a concrete opening paragraph, and descriptive links. Add a short navigation section when the README is long. Keep extensive runbooks and historical records behind those links.

## Adapt the structure to the repository

| Repository kind | Additional guidance |
|---|---|
| Application or library | Supported use, installation or local development, an example, and verification |
| Experimental project | What exists today, what is planned, how to exercise the implemented slice, and known limits |
| Infrastructure or configuration | Authority, safe orientation, change and validation paths, and links to operational runbooks |
| Research or methods | The question, assumptions, artifacts, evidence limits, and how to reproduce or evaluate a claim |
| Skills or agent workflows | When to use the method, required context, useful output, stopping point, and host-specific limits |
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

## Respect the publication boundary

Public documentation must stand on public, intentionally disclosed information. Do not expose private project names, internal links, machine identities, inventories, network topology, credentials, personal data, or confidential operational details. Prefer generalized explanations and synthetic examples.

Private documentation can link to the operational detail its readers need, but the front page should still orient readers before presenting those details. Keep sensitive information in the appropriate controlled source rather than duplicating it.

A decision to change visibility is separate from a documentation improvement. Review contents, history, metadata, assets, automation, and access implications before proposing publication.

## Use visuals to explain

Visual communication is part of documentation correctness. Every new or changed visual heading, Mermaid graph, flowchart, sequence, chart, badge, screenshot and illustration must have a clear purpose, excellent project-appropriate presentation, source-backed meaning and an inspected rendered result.

Follow the [visual documentation review standard](visual-documentation-review.md). It requires checking the meaning of labels, arrows, ordering, grouping, color and status; distinguishing concepts, plans, implementation and observed results; and reviewing the intended rendering, text equivalents, narrow-screen readability and supported themes. Preserve authentic product demonstrations and each project's own design authority. Use generated artwork for clearly identified illustrations, not fabricated evidence or exact technical diagrams.

Record the material sources, checks and remaining limits in the existing review or design record. One bounded review and affected rechecks are sufficient; no mandatory independent-model panel is introduced. A passing Mermaid render establishes syntax/rendering, not the truth of the diagram. Existing historical visuals are not certified merely because the repository adopts this standard.

Use badges only when they point to meaningful, maintained information. Avoid decorative scores, unsupported maturity labels and claims of universal reliability. The quality bar applies to private as well as public documentation; privacy and publication boundaries remain unchanged.

## Verify and maintain

For a documentation change, check relative links and anchors, confirm external references where needed, run whitespace checks, review the diff for unintended information, and inspect rendered layouts when they change. Run relevant existing checks; a prose edit does not require inventing a test framework.

Update documentation with the behavior it describes. A short, accurate guide is more useful than a comprehensive-looking one that cannot be trusted.
