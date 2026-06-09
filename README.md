# Personal Blog Vibe Harness

A Codex skill for helping non-coders create, launch, and maintain a personal blog by composing existing static-site, CMS, and deployment tools instead of rebuilding them from scratch.

Current status: `v0.1.0-alpha`

This version is suitable for self-use and small internal trials. It has not yet been validated through a full end-to-end blog launch.

## What It Does

This skill guides Codex through a practical blog-building workflow:

- clarify the user's blog goal with only a few blocking questions;
- choose a conservative stack such as Astro, HugoBlox, Pages CMS, GitHub Pages, or Cloudflare Pages;
- create or repair a maintainable Markdown-based blog project;
- configure a browser-editable content workflow when needed;
- validate the generated project structure;
- hand off simple publishing and maintenance instructions for non-coders.

The goal is not to create another blog framework or CMS. The goal is to make existing tools easier to combine safely.

## Best-Fit Use Cases

Use this skill when someone asks to:

- vibe-code a personal blog with Codex;
- create a personal essay, notes, portfolio, research, or technical blog;
- migrate existing writing into a static blog;
- make an existing Markdown blog editable by a non-coder;
- add Pages CMS or deployment guidance to a blog project;
- repair a generated blog project so it is easier to maintain.

## Default Architecture

The skill prefers this route unless the project context suggests otherwise:

1. Astro for simple personal blogs, essays, notes, and lightweight portfolios.
2. HugoBlox for research, academic, resume, project, and profile-heavy sites.
3. Pages CMS for browser-based editing of repository-backed Markdown/YAML content.
4. GitHub Pages or Cloudflare Pages for static deployment.

## Repository Structure

```text
personal-blog-vibe-harness/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── content-brief-template.md
│   ├── first-post-template.md
│   ├── github-pages-astro.yml
│   └── pages-cms-astro-blog.yml
├── references/
│   ├── cms-deployment.md
│   ├── intake-and-brief.md
│   ├── maintenance-playbooks.md
│   └── stack-routes.md
└── scripts/
    └── audit_blog_project.py
```

## Install

Clone or copy this folder into your Codex skills directory.

Windows example:

```powershell
git clone https://github.com/Puss-M/personal-blog-vibe-harness.git "$env:USERPROFILE\.codex\skills\personal-blog-vibe-harness"
```

macOS/Linux example:

```bash
git clone https://github.com/Puss-M/personal-blog-vibe-harness.git ~/.codex/skills/personal-blog-vibe-harness
```

Then start a new Codex session so the skill metadata can be discovered.

## Example Prompt

```text
Use $personal-blog-vibe-harness to help me create and launch a personal blog I can maintain without coding.
```

## Audit Script

The bundled audit script checks whether a generated blog project has the expected structure for a non-coder-friendly handoff.

```bash
python scripts/audit_blog_project.py /path/to/blog-project
```

It detects common signals such as:

- Astro, Hugo, Next, Pages CMS, and GitHub Actions;
- missing build scripts;
- missing content folders;
- missing CMS sections;
- missing media folders;
- missing `.gitignore`.

The script is intentionally structural. It does not replace a real static-site build.

## Validation

The skill has been validated with Codex's skill validator:

```bash
python path/to/quick_validate.py path/to/personal-blog-vibe-harness
```

Expected result:

```text
Skill is valid!
```

## Roadmap

- Run an end-to-end Astro blog launch trial.
- Run an end-to-end HugoBlox profile/blog launch trial.
- Add a minimal example output project.
- Add release tags after real-world trial feedback.
- Tighten Pages CMS templates against generated project variants.

## Notes

This is a harness, not a hosted product. Account actions such as GitHub login, Pages CMS connection, Cloudflare setup, and DNS changes still require the user to complete official UI flows.
