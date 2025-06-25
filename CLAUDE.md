# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based personal blog/website hosted on GitHub Pages. The repository contains:
- A Jekyll site configured with the "hacker" theme
- Blog posts written in Markdown and stored in `docs/_posts/`
- Custom layouts and styling
- Org-mode content that gets converted to HTML

## Architecture

- **Main site**: Located in `docs/` directory
- **Content**: Blog posts in `docs/_posts/` follow Jekyll naming convention `YYYY-MM-DD-title.markdown`
- **Layouts**: Custom Jekyll layouts in `docs/_layouts/` (home.html, post.html)
- **Styling**: Custom SCSS in `docs/assets/css/style.scss` that imports the hacker theme
- **Org content**: Original org-mode files in `org/` directory, converted versions in `docs/_posts/`
- **Configuration**: Jekyll config in `docs/_config.yml`, Ruby dependencies in `docs/Gemfile`

## Development Commands

### Local Development
```bash
cd docs
bundle install          # Install Ruby dependencies
bundle exec jekyll serve # Start local development server
```


### Building
```bash
cd docs
bundle exec jekyll build # Build static site to _site/
```

## Content Creation

- Blog posts go in `docs/_posts/` with format `YYYY-MM-DD-title.markdown`
- Include Jekyll front matter with layout, title, date, and categories
- Org-mode files can be placed in `org/` and converted to HTML for `docs/_posts/`
- Images and assets go in `docs/assets/`

## Key Files

- `docs/_config.yml`: Main Jekyll configuration
- `docs/Gemfile`: Ruby gem dependencies
- `docs/_layouts/home.html`: Custom home page layout
- `docs/assets/css/style.scss`: Custom styling on top of hacker theme