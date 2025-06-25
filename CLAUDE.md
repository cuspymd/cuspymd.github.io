# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based personal blog/website hosted on GitHub Pages. The repository contains:
- A Jekyll site configured with the "hacker" theme
- Blog posts written in Markdown and stored in `_posts/`
- Custom layouts and styling

## Architecture

- **Content**: Blog posts in `_posts/` follow Jekyll naming convention `YYYY-MM-DD-title.markdown`
- **Layouts**: Custom Jekyll layouts in `_layouts/` (home.html, post.html)
- **Styling**: Custom SCSS in `assets/css/style.scss` that imports the hacker theme
- **Configuration**: Jekyll config in `_config.yml`, Ruby dependencies in `Gemfile`

## Development Commands

### Local Development
```bash
bundle install          # Install Ruby dependencies
bundle exec jekyll serve # Start local development server
```


### Building
```bash
bundle exec jekyll build # Build static site to _site/
```

## Content Creation

- Blog posts go in `_posts/` with format `YYYY-MM-DD-title.markdown`
- Include Jekyll front matter with layout, title, date, and categories
- Images and assets go in `assets/`

## Key Files

- `_config.yml`: Main Jekyll configuration
- `Gemfile`: Ruby gem dependencies
- `_layouts/home.html`: Custom home page layout
- `assets/css/style.scss`: Custom styling on top of hacker theme