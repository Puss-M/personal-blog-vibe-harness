# Visual Style Discovery

Use this reference when the user is creating a new blog, migrating into a new design, or asking for a visual redesign.

## Core Rule

Do not treat "personal blog" as one default aesthetic. Learn the user's taste before designing.

The goal is not to make the user speak like a designer. The goal is to translate their words, references, and reactions into concrete visual constraints.

## Conversation Pattern

Start broad, then narrow:

1. Ask what the site should feel like to a first-time visitor.
2. Offer 2 to 3 contrasting direction cards if the answer is vague.
3. Ask what should be avoided.
4. Ask for references only if the user likely has them.
5. Summarize a style brief and ask for confirmation.

Ask one focused question at a time unless the user asks for a checklist.

## Useful First Question

Ask:

```text
When someone opens your blog, should it feel more like a quiet notebook, a professional homepage, a magazine, a research archive, or a visual portfolio?
```

If the user answers vaguely, offer direction cards instead of demanding precision.

## Direction Cards

Use these as starting points. Adapt labels to the user's domain.

### Quiet Notebook

- Mood: calm, intimate, low-noise.
- Layout: narrow readable column, simple archive, minimal navigation.
- Typography: serif or humanist sans, generous line height.
- Color: warm paper, dark ink, one muted accent.
- Imagery: optional, small, editorial.
- Best for: essays, notes, diaries, reflective writing.

### Professional Homepage

- Mood: credible, clear, current.
- Layout: profile intro, selected writing, projects, contact.
- Typography: clean sans, structured hierarchy.
- Color: neutral base, restrained accent.
- Imagery: portrait, workspace, project thumbnails.
- Best for: consultants, researchers, engineers, creators.

### Magazine / Column

- Mood: editorial, confident, opinionated.
- Layout: strong article cards, issue-like sections, featured post.
- Typography: expressive headings, readable body.
- Color: strong contrast, controlled accent palette.
- Imagery: covers, article art, photography.
- Best for: commentary, culture, product thinking, public essays.

### Research Archive

- Mood: rigorous, organized, durable.
- Layout: profile, publications, notes, tags, search.
- Typography: compact but readable.
- Color: quiet academic palette, strong metadata treatment.
- Imagery: sparse, diagrams or paper figures when useful.
- Best for: students, academics, labs, technical learning logs.

### Visual Portfolio

- Mood: distinctive, polished, image-led.
- Layout: full-bleed work previews, project pages, short writing.
- Typography: strong display headings.
- Color: brand-driven palette.
- Imagery: essential; use real work, screenshots, or generated visuals.
- Best for: designers, artists, photographers, makers.

## Style Brief Format

Write this before implementing visual design:

```markdown
## Style Brief

- Direction:
- Mood:
- Audience impression:
- Layout:
- Typography:
- Color:
- Imagery:
- Content density:
- Interactions:
- Must avoid:
- Reference cues:
- Open questions:
```

Ask:

```text
Does this style brief feel right? Tell me what to keep, remove, or push further before I build the first visual version.
```

## Translation Rules

- If the user says "高级", ask whether that means luxury, editorial restraint, technical polish, or personal taste.
- If the user says "简洁", ask whether they mean sparse, easy to read, or low maintenance.
- If the user says "有设计感", ask for one site, app, book, poster, or creator whose taste feels close.
- If the user says "像个人博客", do not assume minimalism; ask what kind of person the blog should make them seem like.
- If the user dislikes a preview, ask what feels wrong: color, spacing, image style, density, typography, or personality.

## Implementation Guardrails

- Keep style tokens explicit in CSS or config so the site can be restyled later.
- Avoid hard-coding a one-off visual direction across many files.
- Keep content structure separate from visual styling.
- After the first preview, ask for reactions in concrete categories: color, typography, layout, imagery, and mood.
