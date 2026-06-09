# Intake And Build Brief

## Fast Intake

Ask no more than three questions before starting:

1. What kind of blog is this: personal essays, technical notes, research profile, portfolio, newsletter, or mixed?
2. Do you already have materials: old posts, images, bio, domain name, GitHub account, or design references?
3. Which mode do you prefer: simplest route, visually polished route, or research/portfolio route?

If the user is unsure, default to:

- Astro for simple personal writing;
- HugoBlox for research/profile-heavy sites;
- Pages CMS for browser-based editing;
- GitHub Pages for free deployment.

## Content Inventory

Collect or create:

- site name
- one-sentence positioning
- author name or display name
- short bio
- homepage sections
- navigation labels
- first three post ideas
- image sources and usage rights
- contact/social links
- domain, if any

Mark missing items as placeholders. Do not block implementation unless the missing item affects routing, deployment, or privacy.

## Build Brief Template

Use this structure in the project when the task is more than a tiny edit:

```markdown
# Blog Build Brief

## Purpose

## Audience

## Stack

## Content Model

## Visual Direction

## Editing Workflow

## Deployment

## Assumptions

## Risks
```

## Non-Coder Copy Rules

- Use "write a post" instead of "create a Markdown entry".
- Use "publish" instead of "push to main".
- Use "site settings" instead of "config".
- Explain any required GitHub, Cloudflare, or DNS action as a UI step.
- Keep handoff instructions under one screen when possible.
