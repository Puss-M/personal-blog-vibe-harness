# CMS And Deployment Notes

## Pages CMS

Use Pages CMS when the repository contains editable Markdown, YAML, or JSON and the user wants browser-based editing.

Implementation notes:

- Place `.pages.yml` at the repository root.
- Define `media` first, then `content`.
- Use a `collection` for blog posts and `file` entries for site settings or homepage copy.
- Keep field names aligned with frontmatter keys.
- Prefer `string`, `text`, `rich-text`, `date`, `image`, `select`, and `boolean` fields for a first version.
- Do not expose technical files such as package manifests, lockfiles, workflows, or generated output to the CMS.

Starter asset:

- Copy `assets/pages-cms-astro-blog.yml` to the target project root as `.pages.yml`.
- Adjust `path`, `media.input`, and frontmatter fields after inspecting the actual project.

## GitHub Pages

Use GitHub Pages when the user wants free GitHub-native hosting.

Implementation notes:

- For static-site generators, prefer a GitHub Actions workflow over branch-folder publishing.
- The build artifact must include the generated `index.html` at its root.
- For Astro project pages, set the correct `site` and `base` values if the site is under `https://USER.github.io/REPO/`.
- If the route is not a user/organization site, verify asset paths under the repository base path.

Starter asset:

- Copy `assets/github-pages-astro.yml` to `.github/workflows/pages.yml`.
- Adjust Node version and build output directory if the project differs.

## Cloudflare Pages

Use Cloudflare Pages when:

- the user already has Cloudflare;
- custom domain setup matters soon;
- preview deployments are useful;
- GitHub Actions should stay minimal.

Typical settings:

- Astro build command: `npm run build`
- Astro output directory: `dist`
- Hugo build command: `hugo --minify`
- Hugo output directory: `public`

## Deployment Handoff

Tell the user exactly which UI action remains:

- connect GitHub repository;
- enable GitHub Pages from Actions;
- connect Cloudflare Pages to the repository;
- add a custom domain;
- wait for DNS propagation.

Do not imply those account actions were completed unless they were actually performed.
