# AGENTS.md

MkDocs personal notes/blog site (Spanish, with English translations). Published at https://apuntes.eduardofilo.es/.

## Commands

« `mkdocs serve` — dev server (uses `mkdocs.yml`)
« `mkdocs build` — build to `site/`
« `./deploy.sh` — builds to a sibling repo (`~/git/eduardofilo.github.io`), NOT to `site/`
« Virtualenv: `/home/edu/.virtualenvs/mkdocs` — must be activated before mkdocs commands

## Content conventions

« Blog posts: `docs/YYYY-MM-DD_topic.md` (underscores in topic)
« English translations: add `.en.md` suffix, same base name (e.g., `2020-05-08-rg350_dosbox.en.md`)
« Category pages: `docs/<category>/<topic>.md` (no date prefix)
« Images: `docs/images/posts/YYYY-MM-DD_topic/` for blog post images
« New blog posts: must be added to `nav:` in `mkdocs.yml` AND to `docs/index.md` as an admonition entry

## Key gotchas

« `nav:` in `mkdocs.yml` is **manually maintained** — new pages won't appear without adding them
« `exclude_docs` in `mkdocs.yml` lists excluded files — respect these
« `use_directory_urls: false` — generates flat `.html` files, not subdirectories
« RSS plugin `match_path` regex filters which pages get feeds: `\d{4}-\d{2}-\d{2}[-_a-zA-Z0-9]+(\.en)?\.md`
« i18n uses `suffix` docs structure with `es` as default, `en` as secondary
« `deploy.sh` pulls, resets, then runs `mkdocs gh-deploy` into `eduardofilo.github.io` — it does NOT deploy from this repo's `site/` dir

## Don't

« Don't add pages to `nav:` without also adding the corresponding `index.md` entry
« Don't create files listed in `exclude_docs` (check `mkdocs.yml` for the list)
« Don't modify the redirect map unless actually moving an existing page
