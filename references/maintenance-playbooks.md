# Maintenance Playbooks

## New Post

For a Markdown blog:

1. Create a post file in the posts folder.
2. Add title, date, description, tags, draft status, and optional cover image.
3. Write the body in Markdown.
4. Preview locally or through the hosting preview.
5. Publish by saving through the CMS or committing the file.

If Pages CMS is configured, explain the same flow as:

1. Open Pages CMS.
2. Choose Posts.
3. Click New.
4. Fill in title, summary, date, tags, cover image, and article body.
5. Save or publish.

## Edit Homepage

Prefer putting homepage text in one obvious content file or site settings file. If the homepage is code-only, create a small editable data file before handing the site to a non-coder.

## Add Images

Rules:

- Store reusable images in the configured media folder.
- Use descriptive filenames.
- Avoid spaces in filenames.
- Compress large photos before committing.
- Confirm image usage rights.

## Build Failure

First checks:

- Did a frontmatter field lose a quote or colon?
- Does the post date use a valid format?
- Did an image path point to a missing file?
- Did the user paste raw HTML or unsupported embed code into Markdown?
- Did a dependency install fail?

Escalate to project-specific logs only after checking content mistakes.

## Design Changes

Group changes as:

- content-only: copy, navigation labels, post organization;
- theme-level: colors, fonts, spacing, layout choices;
- structural: new page type, new collection, new CMS fields.

For non-coders, complete content-only changes immediately, batch theme-level changes, and treat structural changes as a mini design task.
