# Visual documentation review

This checklist covers every picture in a ZMS Labs README, wiki or guide that carries meaning: diagrams, charts, screenshots, badges, headings drawn as images, interactive explanations and generated artwork, in public and private repositories. It is written for people and for AI tools that add or change one.

The same bar applies to every project, and each product keeps its own type, colors and visual language. A simple, precise diagram can meet this standard better than an elaborate illustration.

Some rules apply to every visual, public or private: it has to be accurate, it can't expose private information, and a screenshot or recording has to be genuine. Presentation polish, contrast measurement and the depth of the review notes get the full treatment on public pages and a lighter one in private working notes. Where a later section spells one of these out, that is the bar for public pages.

## Start with what the reader should understand

Before making or revising a visual, state its purpose in one sentence. Identify its audience, the question it answers, its authoritative source, the state, date or revision it shows, and where it will render. Describe the intended takeaway without relying on the caption to excuse a misleading picture.

Choose a heading that makes a concrete promise the material supports. Review the heading and image together: a modest caption cannot undo a headline, checkmark or arrow that overstates the result. Avoid empty status badges, invented metrics, decorative trend lines, fake controls and ornamental process steps.

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

Keep exact schematics and measured charts editable and reproducible. Image generation may create conceptual artwork, but it must not invent architectural edges, code, labels, metrics, screenshots or evidence. Keep important explanatory text in Markdown, HTML or accessible vector text rather than baking it into a bitmap. Review generated details for unintended numbers, symbols and implications.

## Review semantics, not just syntax

A visual is material when a mistake in it could change what a reader concludes or decides. For each material visual, check these points:

- Nodes and labels: terminology matches the authoritative source; no stale names, nonexistent capabilities or ambiguous abbreviations.
- Arrows: say what each arrow means. Data moving, one step triggering the next, time passing, and one thing depending on or causing another are different relationships. If you only know that two things are related, don't draw a one-way arrow, and label the arrows when one diagram mixes meanings or the direction is ambiguous.
- Order and branches: a row is not automatically a sequence. Optional paths must not look mandatory. Show conditions, loops and failure paths when their omission would change the reader's understanding; a focused diagram may omit unrelated detail if its scope is stated.
- Grouping and scale: a box drawn around things should mean something real, such as who owns them or a security boundary between them. Size, line weight, position and color must not imply importance, quantity, confidence or status without support.
- State and evidence: distinguish concept, proposal, implementation, tested behavior and observed deployment. Do not promote a planned connection to an existing integration. Checkmarks, green status dots and success colors require the same justification as words.
- Completeness at the stated scope: a summary can be selective, but must not hide a condition that reverses its conclusion. Link to the deeper source when a single image cannot explain the system honestly.
- Consistency: headings, captions, legend, adjacent prose, alternative text, example data and the diagram say the same thing.

For a chart, also check where the data came from and when, its units and scale, what each number is out of, where the axes start, what was filtered out or is missing, how values were combined, and how certain they are. Don't invent data points, show more precision than the data has, let the size of a shape exaggerate a difference, or make a comparison the data can't support.

Record the relevant source or test result next to the explanation or in its review record. Sensitive source references stay private; the published explanation must be independently intelligible without exposing them.

## Check the visual at its actual size

Use deliberate hierarchy, typography, alignment, spacing and a restrained project-appropriate palette. Route connectors clearly; avoid crossings, unexplained line styles and labels that collide with edges. Split an overcrowded diagram into linked levels rather than shrinking its text. Do not apply the same visual template to every project's distinct identity.

Inspect the actual rendered image, not only its source or a successful render command. Check the intended README, wiki or page width, and both desktop and narrow-screen layouts. Where the destination supports both light and dark modes, inspect both. Preserve useful text at normal reading size, provide full-resolution access or a usable zoom for dense captures, and verify the selected image is the one that opens.

Complex visuals need a short identifying text alternative and a nearby textual explanation of their essential relationships or results. A chart may need a data table. Meaning must not rely only on color or hover. Keyboard access and visible focus apply to interactive figures; reduced-motion preferences apply to animation. See [W3C guidance on complex images](https://www.w3.org/WAI/tutorials/images/complex/).

Text should meet the W3C contrast minimums, 4.5:1 or 3:1 for large text, and shapes or controls that carry meaning need 3:1 against the colors next to them where the criterion applies. Measure the real colors and check the relevant exceptions; don't eyeball the ratio. Passing these checks doesn't by itself make a page conform to the accessibility guidelines. See [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Mermaid and other rendered diagrams

Keep the source in the repository or authoritative documentation system. Use supported syntax, concise node text, a clear reading direction, useful subgraphs and explicit labels where necessary. A legend is useful only when it explains a real visual encoding. Provide a prose equivalent; do not assume a renderer's accessibility output covers every reader or destination.

Test on the intended destination. GitHub's Mermaid version can differ from a local renderer, so check the render on GitHub itself, and use its documented version mechanism when syntax support is in doubt. If destination inspection is unavailable, record that exact remaining check instead of reporting a pass. See [GitHub's diagram guidance](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).

An SVG or HTML figure should resize with the screen, load nothing unsafe and keep its text readable by screen readers. Do not add remote scripts, fonts, trackers or runtime dependencies solely to make a static document more decorative. Use a fallback when the destination cannot render the preferred format.

## Keep captures genuine and private details out

Keep genuine product and project captures. Improve their framing, annotation, captions, scale or access before considering a replacement. Do not generate over a product screenshot to imply that invented controls or results exist. Renders with made-up content must use sample data written for the purpose, never renamed private records.

Inspect pixels, metadata, filenames, links and surrounding source for personal data, confidential documents, private endpoints, operational topology, credentials and unapproved identities. Keep publication rights, licenses and attribution with the asset. Visibility changes and external publication remain separate authorized actions.

Keep the chosen design and any seriously considered alternative, with the reasons. Keep the editable source somewhere permanent, along with where the data came from, the prompt and tool behind any generated image, the source version, the image size, its hash and the render that was inspected. Use the project's existing design archive. A private archive may hold sensitive provenance; publish only the approved image and safe attribution.

## A finite completion check

Whoever reviews the change is responsible for both what the visual means and how it looks. Seek specialist help only when a material claim goes beyond the available evidence or expertise.

1. Identify the exact changed visual and the source that supports its claims.
2. Read it as a new reader: what does the heading, shape, arrow or status imply?
3. Compare those implications with the source; fix or explicitly bound unsupported claims.
4. Inspect its rendered destination, sizing, supported themes and accessible equivalent; try any changed interactions.
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

One record may cover a coherent set of closely related figures if it identifies them and their checks. Do not add a new ledger or framework for a trivial caption correction. Automated checks can confirm syntax, links, file integrity or that a policy was adopted; they can't tell whether a picture is clear or true.

The target is no known material error within the reviewed scope. A claim or implementation change reopens the affected review.

## Where this applies

Apply this to new and changed visuals in active repositories, public and private. A repository can add stricter rules of its own but keeps the ones on this page. Keep this page as the single copy, and point contributor and AI agent instructions here.

In a fork, apply it to ZMS Labs' own guidance and changes, and leave files the upstream project owns alone. Don't rewrite historical evidence or unarchive a repository just to update how it looks. Review an older visual before reusing it as a current claim, and apply this checklist to an archived project's new work if it is revived.

Adopting this checklist doesn't review anything by itself. Older visuals count as unreviewed until someone has checked what they claim and how they render, and a new edit date or a fresh export doesn't change that. Any report on review coverage should say which visuals were actually checked.
