---
layout: post
title: "크롬 확장 개발 시 각 스크립트별 로그 확인하는 방법"
date: 2025-06-24 12:00:00 +0900
categories: [Development, Chrome Extension]
tags: [chrome-extension, javascript, debugging, devtools, console-log]
author: 
description: "크롬 확장 개발에서 content.js, background.js, popup.js 각각의 로그를 확인하는 방법을 상세히 알아봅니다."
image: 
  path: /assets/img/chrome-extension-debug.png
  alt: Chrome Extension Debugging Guide
---

크롬 확장을 개발하다 보면 가장 답답한 순간 중 하나가 바로 **로그가 어디서 나오는지 모를 때**입니다. `console.log()`를 열심히 찍어놨는데 아무리 DevTools를 뒤져봐도 로그가 보이지 않아서 머리를 쥐어뜯은 경험, 누구나 한 번쯤은 있을 거예요.

크롬 확장의 각 스크립트(`content.js`, `background.js`, `popup.js`)는 서로 다른 실행 환경에서 동작하기 때문에 로그를 확인하는 방법도 각각 다릅니다. 이 글에서는 각 스크립트별로 로그를 확인하는 정확한 방법을 알아보겠습니다.

## 1. Content Script (content.js) 로그 확인

**Content Script는 웹페이지의 DOM에 직접 접근하는 스크립트**입니다. 이 스크립트의 로그는 가장 직관적으로 확인할 수 있습니다.

### 확인 방법
1. 확장이 실행되는 웹페이지에서 **F12** 또는 **우클릭 → 검사** 클릭
2. **Console 탭**에서 로그 확인

### 예시 코드
```javascript
// content.js
console.log("Content script가 실행되었습니다!");
console.log("현재 페이지 URL:", window.location.href);

// 페이지의 특정 요소 찾기
const title = document.querySelector('h1');
if (title) {
    console.log("페이지 제목:", title.textContent);
}
```

### 주의사항
- 확장이 특정 사이트에만 실행되도록 설정된 경우, 해당 사이트에서만 로그가 나타납니다
- 페이지를 새로고침하면 로그가 초기화됩니다

## 2. Background Script (background.js) 로그 확인

**Background Script는 백그라운드에서 계속 실행되는 스크립트**로, 확장의 핵심 로직을 담당합니다. 이 스크립트의 로그를 확인하는 방법이 가장 헷갈리는 부분입니다.

### 확인 방법
1. **chrome://extensions/** 페이지로 이동
2. 개발자 모드 활성화 (우상단 토글 스위치)
3. 해당 확장의 **"서비스 워커"** 또는 **"배경 페이지"** 링크 클릭
4. 새로 열린 DevTools 창의 **Console 탭**에서 로그 확인

### 예시 코드
```javascript
// background.js
console.log("Background script가 시작되었습니다!");

// 확장 설치 시 실행
chrome.runtime.onInstalled.addListener(() => {
    console.log("확장이 설치되었습니다!");
});

// 메시지 수신 시 실행
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log("메시지 수신:", message);
    console.log("발신자:", sender);
});
```

### 주의사항
- Manifest V3에서는 "서비스 워커"로, Manifest V2에서는 "배경 페이지"로 표시됩니다
- 서비스 워커는 비활성화될 수 있으므로, 활동이 없을 때는 로그가 보이지 않을 수 있습니다

## 3. Popup Script (popup.js) 로그 확인

**Popup Script는 확장 아이콘을 클릭했을 때 나타나는 팝업 창의 스크립트**입니다.

### 확인 방법
1. 확장 아이콘을 클릭하여 팝업 열기
2. 팝업 창에서 **우클릭 → 검사** 클릭
3. DevTools의 **Console 탭**에서 로그 확인

### 예시 코드
```javascript
// popup.js
console.log("Popup이 열렸습니다!");

document.addEventListener('DOMContentLoaded', () => {
    console.log("Popup DOM이 로드되었습니다!");
    
    // 버튼 클릭 이벤트
    const button = document.getElementById('myButton');
    if (button) {
        button.addEventListener('click', () => {
            console.log("버튼이 클릭되었습니다!");
        });
    }
});
```

### 주의사항
- 팝업을 닫으면 DevTools도 함께 닫힙니다
- 팝업이 열린 상태에서만 로그를 확인할 수 있습니다

## 4. 각 스크립트별 로그 확인 요약표

| 스크립트 | 실행 환경 | 로그 확인 위치 | 접근 방법 |
|---------|----------|---------------|----------|
| **content.js** | 웹페이지 | 해당 웹페이지 DevTools | F12 → Console |
| **background.js** | 확장 백그라운드 | 확장 관리 페이지 | chrome://extensions/ → 서비스 워커 |
| **popup.js** | 팝업 창 | 팝업 DevTools | 팝업 우클릭 → 검사 |

## 5. 디버깅 팁

### 로그가 안 보일 때 체크리스트
- [ ] 올바른 위치에서 DevTools를 열었는가?
- [ ] 확장이 제대로 로드되었는가?
- [ ] 스크립트에 문법 오류가 없는가?
- [ ] 조건문 안에 있는 로그가 실제로 실행되는가?

### 유용한 디버깅 방법
```javascript
// 오류 발생 시 자세한 정보 출력
try {
    // 실행할 코드
} catch (error) {
    console.error("오류 발생:", error);
    console.error("스택 트레이스:", error.stack);
}

// 객체 전체 내용 확인
console.log("전체 객체:", JSON.stringify(myObject, null, 2));

// 실행 시점 확인
console.log("현재 시간:", new Date().toISOString());
```

## 마무리

크롬 확장 개발에서 로그 확인은 디버깅의 핵심입니다. 각 스크립트의 실행 환경을 이해하고 올바른 위치에서 로그를 확인하는 것이 중요합니다. 이 방법들을 익혀두면 개발 과정에서 훨씬 수월하게 문제를 해결할 수 있을 것입니다.

개발하면서 로그가 안 보인다고 당황하지 마시고, 이 가이드를 참고해서 차근차근 확인해보세요! 🚀