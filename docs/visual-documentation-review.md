# Visual documentation review

This is the shared quality standard for ZMS Labs documentation: clear meaning, excellent visual craft, source-backed accuracy and an inspected rendered result. It covers READMEs, wikis, guides, diagrams, charts, flowcharts, sequence diagrams, visual headings, badges, screenshots, interactive explanations and generated artwork in public and private repositories.

The same quality bar applies across projects; product-local design authority still determines identity, typography, tokens and visual language. An established product is not a blank canvas. A simple, precise diagram can satisfy this standard better than an elaborate illustration.

## Start with what the reader should understand

Before making or revising a visual, state its purpose in one sentence. Identify its audience, the question it answers, its authoritative source, the state/date/revision represented, and where it will render. Describe the intended takeaway without relying on the caption to excuse a misleading picture.

Choose a heading that makes a concrete promise the material supports. Review the heading and image together: a modest caption cannot undo a headline, checkmark or arrow that overstates the result. Avoid empty status badges, invented metrics, decorative trend lines, pseudo-controls and ornamental process steps.

## Choose the medium for the claim

| Material | Preferred treatment | Required boundary |
|---|---|---|
| Architecture, relationships, data or control flow | Editable Mermaid, SVG or equivalent structured source | Every edge has a known meaning; grouping and direction match the source |
| Temporal interactions or protocols | Editable sequence diagram | Ordering, participants, async behavior and relevant failure/return paths are accurate |
| State transitions or decisions | Editable state/decision diagram | Branch conditions and reachable outcomes are correct; scope exclusions are visible |
| Measurements or comparisons | Reproducible plot or table derived from identified data | Values, units, denominator, period, uncertainty and transformations are traceable |
| Product appearance or interaction | Authentic capture or reproducible render with appropriate data | Prototype, isolated component, recording and live operation are distinguished |
| Conceptual introduction or editorial metaphor | Carefully directed illustration, including image generation when useful | Clearly illustrative; never passed off as a screenshot, benchmark or executable design |
| A simple relationship already clear in prose | Keep the prose or a small table | No visual is required merely to make a page look busy |

Keep exact schematics and measured charts editable and reproducible. Image generation may create conceptual artwork, but it must not invent architectural edges, code, labels, metrics, screenshots or evidence. Keep important explanatory text in Markdown/HTML or accessible vector text rather than baking it into a bitmap. Review generated details for unintended numbers, symbols and implications.

## Review semantics, not just syntax

For each material visual, inspect these concrete assertions:

- **Nodes and labels:** terminology matches the authoritative source; no stale names, nonexistent capabilities or ambiguous abbreviations.
- **Arrows:** distinguish data transfer, control, time, dependency, causation and association. Do not use a directional arrow when only association is known. Label mixed edge meanings and ambiguous direction.
- **Order and branches:** a row is not automatically a sequence. Optional paths must not look mandatory. Show conditions, loops and failure paths when their omission would change the reader's understanding; a focused diagram may omit unrelated detail if its scope is stated.
- **Grouping and scale:** containment must mean something real, such as ownership or a trust boundary. Size, line weight, position and color must not imply importance, quantity, confidence or status without support.
- **State and evidence:** distinguish concept, proposal, implementation, tested behavior and observed deployment. Do not promote a planned connection to an existing integration. Checkmarks, green status dots and success colors require the same justification as words.
- **Completeness at the stated scope:** a summary can be selective, but must not hide a condition that reverses its conclusion. Link to the deeper source when a single image cannot explain the system honestly.
- **Consistency:** headings, captions, legend, adjacent prose, alternative text, example data and the diagram say the same thing.

For a chart, also verify the data source and date, units, denominator, baseline, axes, scale, missing values, filters, aggregation and any uncertainty. No invented observations, decorative numerical precision, misleading area encoding or unsupported comparison. A stable run is not evidence of accuracy; a screenshot is not evidence of working behavior.

Record the relevant source or test result next to the explanation or in its review record. Sensitive source references stay private; the published explanation must be independently intelligible without exposing them.

## Make the visual excellent at its actual size

Use deliberate hierarchy, typography, alignment, spacing and a restrained project-appropriate palette. Route connectors clearly; avoid crossings, unexplained line styles and labels that collide with edges. Split an overcrowded diagram into linked levels rather than shrinking its text. Do not apply the same visual template to every project's distinct identity.

Inspect the actual rendered image, not only its source or a successful render command. Check the intended README/wiki/page width, desktop and narrow-screen layout. Where the destination supports both light and dark modes, inspect both. Preserve useful text at normal reading size, provide full-resolution access or a usable zoom for dense captures, and verify the selected image is the one that opens.

Complex visuals need a short identifying text alternative and a nearby textual explanation of their essential relationships or results. A chart may need a data table. Meaning must not rely only on color or hover. Keyboard access and visible focus apply to interactive figures; reduced-motion preferences apply to animation. See [W3C guidance on complex images](https://www.w3.org/WAI/tutorials/images/complex/).

For meaningful text, target at least 4.5:1 contrast, or 3:1 for qualifying large text; relevant graphical objects and control indicators require 3:1 against adjacent colors where the criterion applies. Check the actual colors and relevant exceptions, not an eyeballed ratio. These checks alone do not establish full accessibility conformance. See [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Mermaid and other rendered diagrams

Keep the source in the repository or authoritative documentation system. Use supported syntax, concise node text, a clear reading direction, useful subgraphs and explicit labels where necessary. A legend is useful only when it explains a real visual encoding. Provide a prose equivalent; do not assume a renderer's accessibility output covers every reader or destination.

Test on the intended destination. GitHub's Mermaid version can differ from a local renderer; check supported syntax using its documented version mechanism when needed. A local SVG render is local evidence, not proof that the GitHub README or wiki renders correctly. If destination inspection is unavailable, record that exact remaining check instead of reporting a pass. See [GitHub's diagram guidance](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).

For SVG/HTML, preserve a responsive view box, safe dependencies and accessible text. Do not add remote scripts, fonts, trackers or runtime dependencies solely to make a static document more decorative. Use a fallback when the destination cannot render the preferred format.

## Preserve authenticity and privacy

Retain authentic product/project demonstrations. Improve framing, annotation, captions, scale or access before considering replacement. Do not generate over a product screenshot to imply that invented controls or results exist. Synthetic renders must use deliberately authored fixtures, not renamed private records.

Inspect pixels, metadata, filenames, links and surrounding source for personal data, confidential documents, private endpoints, operational topology, credentials and unapproved identities. Keep publication rights, licenses and attribution with the asset. Visibility changes and external publication remain separate authorized actions.

Preserve selected and materially rejected directions with their rationale. Keep editable source, input/data provenance, generation prompts and tool identity where relevant, source revision, asset dimensions, hashes and the inspected render outside a transient cache. Use the project's existing design archive. A private archive may hold sensitive provenance; publish only the approved artifact and safe attribution.

## A finite completion check

The task-owning reviewer is responsible for both meaning and presentation. A separate model or standing review panel is not required. Seek specialist help only when a material claim exceeds the available evidence or expertise.

1. Identify the exact changed visual and the source that supports its claims.
2. Read it as a new reader: what does the heading, shape, arrow or status imply?
3. Compare those implications with the source; fix or explicitly bound unsupported claims.
4. Inspect its rendered destination, sizing, supported themes and accessible equivalent; exercise changed interactions.
5. Record the actual checks and remaining limitations, retain the exact asset/source, and stop when the identified issues are resolved. Repeat only checks affected by a new change or unresolved finding.

A concise review record can live in the existing PR, design note or asset manifest:

```text
Visual and purpose:
Source revision/data and represented state:
Semantic checks performed and corrections:
Rendered destination, widths/themes and interaction checks:
Text equivalent, privacy/rights and provenance:
Result: reviewed for the stated scope | needs correction | not yet reviewed
Remaining limitations and conditions requiring re-review:
```

One record may cover a coherent set of closely related figures if it identifies them and their checks. Do not add a new ledger or framework for a trivial caption correction. Automated checks may establish syntax, links, file integrity or policy adoption; they do not establish beauty or semantic truth.

The target is no known material error within the reviewed scope. Do not certify universal or permanent perfection. A claim or implementation change reopens the affected review; an edit date, fresh export, generated hash or inherited standard does not prove that old content was rechecked.

## Applying the standard across the estate

Apply this to all new and changed documentation visuals in active repositories, including private operational guides and public case studies. Repository-specific requirements can strengthen or specialize it while preserving these accuracy, accessibility, authenticity and privacy obligations.

Keep one authoritative standard and point contributor/agent instructions to it. Preserve product-local design authority. In forks, apply it to ZMS-authored guidance and local changes without rewriting upstream-owned files. Do not rewrite immutable historical evidence or unarchive a repository to modernize its appearance. Review a historical visual before reusing it as a current claim; apply the standard to an archived project's new work if it is revived.

Adoption and retrospective compliance are separate states. Existing visuals remain unreviewed until their own claims and renderings have been examined. An estate coverage report must distinguish local prepared adoption, published guidance, and actually reviewed visual content; it must never report every repository's historical documentation as perfect from the existence of this policy.
