# cuspymd.github.io

개인 블로그/웹사이트 - Jekyll 기반 GitHub Pages

## 개요

Jekyll과 "hacker" 테마를 사용한 개인 블로그입니다. Markdown으로 작성된 블로그 포스트와 커스텀 스타일링을 포함하고 있습니다.

## 개발 환경 설정

### 필수 요구사항
- Ruby 3.0 이상
- Bundler

### 설치

1. Ruby 설치 (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install -y ruby-full build-essential zlib1g-dev
```

2. Gem 경로 설정:
```bash
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

3. Bundler 설치:
```bash
gem install bundler
```

4. 의존성 설치:
```bash
bundle install
```

## 사용법

### 로컬 개발 서버 실행

```bash
bundle exec jekyll serve
```

서버가 http://localhost:4000 에서 실행됩니다.

외부 접속을 허용하려면:
```bash
bundle exec jekyll serve --host 0.0.0.0 --port 4000
```

### 새 블로그 포스트 작성

1. `_posts/` 디렉토리에 새 파일 생성
2. 파일명 형식: `YYYY-MM-DD-title.markdown`
3. Jekyll front matter 포함:

```yaml
---
layout: post
title: "포스트 제목"
date: 2024-01-01 12:00:00 +0900
categories: 카테고리
---

포스트 내용...
```

### 빌드

정적 사이트 빌드:
```bash
bundle exec jekyll build
```

빌드된 파일은 `_site/` 디렉토리에 생성됩니다.

## 프로젝트 구조

```
├── _config.yml              # Jekyll 설정
├── _posts/                  # 블로그 포스트
├── _layouts/                # 레이아웃 템플릿
├── _includes/               # 재사용 가능한 컴포넌트
├── assets/                  # CSS, 이미지 등
├── Gemfile                  # Ruby 의존성
├── index.md                 # 홈페이지
└── README.md
```

## 커스터마이징

- **스타일**: `assets/css/style.scss` 에서 CSS 수정
- **레이아웃**: `_layouts/` 에서 HTML 템플릿 수정
- **설정**: `_config.yml` 에서 사이트 설정 변경

## GitHub Pages 배포

이 저장소는 GitHub Pages로 자동 배포됩니다. `main` 브랜치에 push하면 자동으로 빌드되고 배포됩니다.

## 문제 해결

### Ruby 권한 오류
Gem 경로가 올바르게 설정되었는지 확인:
```bash
echo $GEM_HOME
echo $PATH
```

### Jekyll 서버 오류
의존성을 업데이트:
```bash
bundle update
```

### 포트 충돌
다른 포트 사용:
```bash
bundle exec jekyll serve --port 4001
```