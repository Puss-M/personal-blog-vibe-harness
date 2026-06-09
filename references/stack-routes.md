# Stack Routes

## Recommended Routes

### Route A: Astro + Markdown + Pages CMS

Use for simple personal blogs, essays, notes, learning logs, newsletters, and lightweight portfolios.

Strengths:

- Markdown or MDX content is easy for Codex to generate and edit.
- Astro content collections provide structure for blog posts.
- Static output deploys cleanly to GitHub Pages, Cloudflare Pages, Netlify, or Vercel.
- Pages CMS can edit repository files without adding a database.

Risks:

- The user still needs a GitHub connection for browser editing.
- CMS config paths must match the Astro content paths exactly.
- Some visual changes require code edits.

### Route B: HugoBlox + Markdown

Use for academic, research, engineering, consulting, resume, project, talk, publication, or lab-style sites.

Strengths:

- Strong default content types for profile-heavy sites.
- Markdown-first structure works well with AI agents.
- Existing blocks reduce custom UI work.

Risks:

- Hugo concepts, modules, and frontmatter can confuse beginners.
- Visual customization can become theme-specific.
- CMS integration should be kept narrow at first.

### Route C: Existing Blog + Pages CMS

Use when the user already has a static blog and mainly needs no-code editing.

Strengths:

- Lower migration risk than rebuilding.
- Keeps existing URLs and design when they already work.

Risks:

- Old content paths may be inconsistent.
- Existing frontmatter may need normalization.

### Route D: TinaCMS or Keystatic

Use only when the project already uses React/Next/Astro integration patterns or the user needs richer editorial structure.

Strengths:

- Strong schema-driven editing.
- Better fit for teams or structured content.

Risks:

- More setup and dependency surface.
- More concepts for a non-coder to own.

## Avoid in MVP

- Building a custom CMS.
- Building a new static site generator.
- Building an AI coding platform.
- Adding a database for a personal blog unless the site needs dynamic user data.
- Adding auth beyond what the CMS or hosting platform already requires.

## Selection Heuristic

Pick the simplest route that supports the user's next six months of publishing.

If two routes are close, choose the one with fewer accounts, fewer build steps, and fewer concepts the user must remember.
