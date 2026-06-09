---
name: personal-blog-vibe-harness
description: Help non-coders create, launch, and maintain a personal blog or portfolio blog with Codex by composing existing static-site templates, Markdown content, Git-based CMS tools, and deployment platforms. Use when the user wants to "vibe code" a personal blog, set up a no-code publishing workflow, migrate personal writing into a blog, choose an Astro/HugoBlox/Pages CMS route, repair a generated blog project, or create a repeatable blog-building harness for non-technical users.
---

# Personal Blog Vibe Harness

## Operating Goal

Guide Codex to act as a patient implementation harness for personal blogs. The end user should not need to understand Git, Node, Hugo, frontmatter, build logs, or deployment settings to get a maintainable site.

Do not reinvent a blog framework, CMS, or hosting platform. Compose mature tools, keep the architecture boring, and make every handoff readable by a non-coder.

## Default Stack

Prefer this route unless local evidence points elsewhere:

1. Astro starter for simple personal blogs, writing archives, newsletters, or lightweight portfolios.
2. HugoBlox starter for academic, research, resume, lab, technical portfolio, or Markdown-heavy professional sites.
3. Pages CMS for repository-backed content editing when the user needs a browser UI.
4. GitHub Pages for a GitHub-native free deployment, or Cloudflare Pages when the user already uses Cloudflare or wants a custom domain path.

Read `references/stack-routes.md` before making a stack choice that affects implementation.

## Workflow

### 1. Classify the Task

Classify the current request as one of:

- `new-blog`: create a new blog from goals and preferences.
- `repair-blog`: fix a generated or existing blog project.
- `migration`: move existing writing, notes, or old-site content into a new blog.
- `cms-setup`: make an existing static blog editable by a non-coder.
- `deployment`: publish or repair deployment.
- `harness-work`: improve this skill, scripts, templates, or workflow.

If the task is not a code change and can be answered directly, answer directly. If it requires files, create or modify the project rather than stopping at advice.

### 2. Ask Only Blocking Questions

For non-coders, ask at most three questions before starting. Prefer defaults when the answer is not risky.

Minimum useful questions:

1. What is the blog for: personal essays, technical notes, research profile, portfolio, newsletter, or mixed?
2. Do they already have writing, images, domain, or a GitHub account?
3. Do they want the simplest route or a more customizable route?

Use `references/intake-and-brief.md` when the user is starting from a vague idea or has many existing materials.

### 3. Produce a Build Brief

Before editing a site, write a short build brief in the target project or in the conversation:

- audience and purpose
- chosen stack and why
- content model
- visual direction
- editing workflow
- deployment target
- risks and assumptions

Keep this brief practical. It is a working contract, not a strategy memo.

### 4. Build or Repair Incrementally

Use the existing project style when a project already exists. For a new project:

- scaffold from a maintained starter instead of writing a site from scratch;
- keep content in Markdown or MDX;
- create clear folders for posts, pages, images, and site settings;
- add starter content that teaches the user what to replace;
- add CMS configuration only after the content paths are stable;
- avoid extra databases, auth systems, server runtimes, or bespoke admin panels.

For CMS/deploy specifics, read `references/cms-deployment.md`.

### 5. Make Maintenance Obvious

Every delivered blog should include an obvious way to do these tasks:

- write a new post
- edit homepage text
- add or replace an image
- preview locally or through deployment preview
- publish changes
- recover when a build fails

Use `references/maintenance-playbooks.md` to generate concise user-facing instructions.

### 6. Validate

After code or configuration changes, run the checks appropriate to the project:

- package manager install/build when dependencies are present;
- static-site build command (`npm run build`, `hugo --minify`, or equivalent);
- link/path sanity check for homepage, posts, images, and generated routes;
- CMS config presence and path consistency;
- deployment workflow syntax check when a workflow is created.

Use `scripts/audit_blog_project.py <project-root>` for a quick structural audit. Treat warnings as action items unless they are clearly irrelevant to the chosen stack.

### 7. Handoff

End with:

- what was created or changed;
- where the user should open the project;
- how to preview;
- how to write the next post;
- what still needs a human account action, such as connecting GitHub, Pages CMS, Cloudflare, or DNS.

Never ask the user to paste API keys into chat. For GitHub or hosting auth, ask them to sign in through the official UI or local CLI flow.

## Decision Rules

- Choose Astro when the user wants a simple blog, fast iteration, low conceptual overhead, and good Markdown/MDX ergonomics.
- Choose HugoBlox when the user is a researcher, student, consultant, engineer, or creator who needs publications, projects, CV, talks, or profile blocks.
- Choose Pages CMS when browser-based editing is important and the repository stores Markdown/YAML/JSON content.
- Choose TinaCMS or Keystatic only when the project already uses them or the user explicitly wants a richer editing model and accepts setup complexity.
- Choose Decap CMS only when a project already uses it or deployment constraints make it the lowest-risk path.
- Avoid Cloudflare VibeSDK for a personal-blog MVP; it is a platform-building kit, not the simplest blog harness.

## Bundled Resources

- `references/stack-routes.md`: stack selection matrix and build-vs-buy rationale.
- `references/intake-and-brief.md`: concise intake flow and build brief template.
- `references/cms-deployment.md`: Pages CMS and deployment implementation notes.
- `references/maintenance-playbooks.md`: non-coder maintenance handoff patterns.
- `scripts/audit_blog_project.py`: structural audit for generated or repaired blog projects.
- `assets/pages-cms-astro-blog.yml`: starter `.pages.yml` for an Astro-style Markdown blog.
- `assets/github-pages-astro.yml`: starter GitHub Actions workflow for Astro on GitHub Pages.
- `assets/content-brief-template.md`: reusable user-facing build brief.
- `assets/first-post-template.md`: starter post template for non-coders.
