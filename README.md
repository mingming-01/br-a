# BR-A · 나를 소개하는 한 페이지

궁금한 것을 파고들어 의미를 발견하고, 사람들과 함께 앞으로 나아가는 사람을 소개하는 개인 포트폴리오 사이트입니다.

## 공개 사이트

https://mingming-01.github.io/br-a/

첫 화면에서 이름과 한 줄 소개를 확인할 수 있으며, 이후 개인적인 경험과 성장 과정, 대표 작업, 제출 문서를 확인할 수 있습니다.

## 프로젝트 목적

이 사이트는 단순한 이력서 대신 지금까지의 경험과 앞으로의 방향을 이야기 형태로 보여주기 위해 만들었습니다.

이야기는 진로를 고민했던 시기부터 시작하여 소프트웨어를 직접 배우게 된 과정, 팀 프로젝트 경험, 현재의 ALEPH 활동과 개인 프로젝트까지 이어집니다.

특히 다음 세 가지 능력이 실제 경험에서 어떻게 나타났는지를 중심으로 정리했습니다.

- 자기조절력
- 대인관계력
- 자기동기력

## 사이트 구성

### About me

진로를 고민했던 대학 시기부터 소프트웨어에 관심을 갖게 된 과정, 개발 공부와 팀 프로젝트 경험을 정리했습니다. 최근에는 사내망 접근통제 캡스톤 SENTRA와 WebAuthn 기반 Passkey Private Space를 구현하며 백엔드·인증·데이터 저장 및 운영 환경까지 경험한 내용을 추가했습니다.

실제 경험을 바탕으로 작성했으며, 다른 사람의 실명이나 개인정보는 공개하지 않았습니다.

### Records

SKT ALEPH 활동 중 작성한 리추얼 기록을 바탕으로 활동 기간과 기록 수, 확인된 능력을 보여줍니다.

2026년 11월 2일 원자료 집계는 다음과 같습니다.

- 기록 날짜: 53일
- 마감 기록: 52일
- 진행 중 기록: 1일 (2026-11-02)
- 마감 기록 중 '실천했다': 48일
- 마감 기록 중 '일부 실천했다': 4일
- 기록 기간: 2026-08-11 ~ 2026-11-02

원자료의 일기 내용과 동료 관련 내용은 공개 저장소에 포함하지 않습니다. 날짜, 마감 여부, 본인이 선택한 실천 상태만 device/input/ritual-days.json에 별도로 정리했습니다.

device/input/records.json의 35건은 전체 리추얼 일수와 다른 데이터입니다. 사이트에 소개할 대표 기록 후보를 선별·요약해 둔 자료이며, 후보 문장 생성과 기존 세 가지 역량 분류에 사용합니다. 해당 분류별 건수는 이 선별 자료에만 적용됩니다.

### Works

대표 작업은 실제 구현 범위와 담당 역할을 기준으로 정리했습니다.

#### SENTRA · 사내망 다계층 접근통제 시스템

사내 사용자와 자원에 대한 접근을 역할·부서·개인 단위로 통제하고, 요청 결과를 감사 로그로 관리하는 팀 캡스톤 프로젝트입니다.

- 담당: Flask 백엔드 API, 로그인 인증, SQLite 데이터베이스 설계 및 마이페이지 연동
- Nginx·Gunicorn 기반 서버 실행 환경 구성
- 부서별·개인별 접근 정책 요구사항과 정책 판정 흐름 검토
- 팀 프로젝트로 진행했으며 소스 저장소는 비공개입니다.

#### Passkey Private Space · 개인 인증 공간

Task 8에서 시작한 개인 프로필 프로젝트를 WebAuthn 기반 Passkey 인증 서비스로 확장했습니다.

- 계정별 1회용 초대 코드 기반 최초 등록
- WebAuthn Challenge, RP ID, Origin 검증
- 세션 보안, 로그인 제한, Passkey 추가·삭제 시 재인증
- 로컬 SQLite와 운영 PostgreSQL 분리
- Render 배포 및 Supabase PostgreSQL 운영 저장소 연결

- 서비스: https://my-profile-ohhl.onrender.com/
- GitHub: https://github.com/mingming-01/my-profile

#### Task 10 · 타이핑 연구

「시각적 효과가 타이핑 성능에 미치는 영향」을 주제로 직접 실험하고 데이터를 분석한 연구 프로젝트입니다.

전체 평균에서는 ON 조건의 타이핑 속도가 OFF보다 낮게 나타났지만, 동일 문장 비교에서는 결과가 일관되지 않았습니다. 따라서 시각 효과가 타이핑 성능을 낮춘다고 단정하지 않고 실제 데이터를 기준으로 결과와 결론을 작성했습니다.

- 연구 결과물: `typing-focus-research`
- 공개 페이지: https://mingming-01.github.io/typing-focus-research/

#### Maple Growth Tracker

게임 캐릭터의 성장 기록을 확인하기 위해 만든 개인 웹서비스입니다.

공개 API에서 데이터를 가져와 성장 추이를 확인할 수 있도록 구현하고 실제 서비스 형태로 배포했습니다.

- GitHub: https://github.com/mingming-01/maple-growth-tracker
- 서비스: https://maple-growth-tracker.onrender.com/

#### BR-B · 타이핑 집중 환경 비교기

Task 10에서 진행한 논문 실험 결과를 실제 사용 가능한 웹 앱으로 구현한 프로젝트입니다.

시각 효과가 없는 환경과 있는 환경에서 같은 문장을 직접 입력하고, 자신의 타이핑 속도와 정확도를 비교할 수 있습니다. 개인 테스트 결과와 논문 실험의 집계 결과를 구분하여 보여주며, 논문의 결과를 단순히 재현하는 것이 아니라 사용자가 직접 자신의 결과를 확인할 수 있도록 구성했습니다.

- 앱: https://mingming-01.github.io/typing-focus-app/
- GitHub: https://github.com/mingming-01/typing-focus-app

### Project Stack

프로젝트에서 실제 사용한 기술을 분야별로 정리합니다. 기술 숙련도를 임의 점수로 표현하지 않고, 적용한 프로젝트와 함께 확인할 수 있도록 구성했습니다.

- **Backend:** Java, Python, Flask, REST API
- **Frontend:** JavaScript, HTML, CSS, React, TypeScript
- **Database:** SQLite, PostgreSQL, Supabase
- **Security & Operations:** WebAuthn, Git, GitHub, Linux, Nginx, Gunicorn
- **External API / AI:** Nexon Open API, Gemini API

## 제출 문서

다음 문서를 함께 제출합니다.

- `documents/resume.pdf` · 이력서
- `documents/self-introduction.pdf` · 자기소개서
- `documents/career-description.pdf` · 경력기술서

원본 Markdown도 같은 폴더에 보관합니다.

- `documents/resume.md`
- `documents/self-introduction.md`
- `documents/career-description.md`

## 계속 새로 쓰는 장치

새로운 활동 기록이 생겼을 때 사이트의 기록과 통계를 다시 계산할 수 있도록 간단한 Python 자동화 장치를 만들었습니다.

장치의 구조는 다음과 같습니다.

    device/input/records.json ──→ generate.py ──→ candidates.json
                                      (대표 기록 후보)

    device/input/ritual-days.json ─┐
                                   ├─→ stats.py ──→ stats.json
    device/input/records.json ─────┘
                                      (기간·마감·실천 현황)

### 후보 생성

`generate.py`는 입력된 기록을 읽어 후보 기록을 생성합니다.

### 통계 계산

`stats.py`는 입력된 기록을 다시 집계하여 기록 수와 능력별 통계를 계산합니다.

### 현재 결과

2026-11-02 원자료 집계 결과입니다.

- 전체 기록 날짜: 53일
- 마감 기록: 52일
- 진행 중 기록: 1일
- '실천했다': 48일
- '일부 실천했다': 4일

대표 기록 후보는 별도 입력 파일에 35건이 있으며, 해당 자료의 역량별 분포는 다음과 같습니다.

- 자기조절력: 14건
- 대인관계력: 13건
- 자기동기력: 8건

원자료 전체 회고 내용이나 동료 관련 텍스트는 공개하지 않습니다.

### 실행 방법

프로젝트 루트에서 다음 명령을 실행합니다.

    python3 device/src/generate.py
    python3 device/src/stats.py

결과는 다음 파일에 생성됩니다.

    device/output/candidates.json
    device/output/stats.json

### 재현성

이 장치는 AI 모델 호출이나 랜덤 요소를 사용하지 않습니다.

같은 `records.json`, `ritual-days.json`과 같은 Python 코드를 사용하면 같은 결과를 다시 생성할 수 있습니다.

새로운 폴더에서도 다음 명령으로 다시 실행할 수 있습니다.

    cd br-a
    python3 device/src/generate.py
    python3 device/src/stats.py

장치에 대한 자세한 설명과 입력 형식은 `device/README.md`에서 확인할 수 있습니다.

## 사이트 업데이트 방식

새로운 기록이 생기면 다음 순서로 업데이트합니다.

    records.json 또는 ritual-days.json 수정
          ↓
    Python 프로그램 실행
          ↓
    결과 확인
          ↓
    사이트에 반영할 내용 직접 선택
          ↓
    Git commit / push
          ↓
    GitHub Pages 업데이트

자동으로 사이트에 게시하지 않고, 최종 공개 내용은 직접 확인하고 판단합니다.

## 재현·통과 확인

1. 공개 사이트 주소를 브라우저에서 확인합니다.
2. About me에서 진로를 고민했던 과정부터 현재까지의 이야기가 이어지는지 확인합니다.
3. Records에서 실제 리추얼 기록을 기준으로 한 숫자를 확인합니다.
4. Works에서 SENTRA, Passkey Private Space, Maple Growth Tracker, Task 10 연구, BR-B 타이핑 집중 환경 비교기를 확인합니다.
5. Project Stack에서 기술을 사용한 프로젝트와 적용 범위를 확인합니다.
6. BR-B 링크를 열어 로그인 없이 앱을 실행하고 OFF → ON 테스트와 결과 비교가 가능한지 확인합니다.
7. `documents/`에서 이력서, 자기소개서, 경력기술서를 확인합니다.
8. `device/README.md`의 실행 방법에 따라 장치를 다시 실행할 수 있는지 확인합니다.
9. 같은 `records.json`을 사용하면 동일한 결과가 생성되는지 확인합니다.

## AI와 나의 판단 3줄

- **AI가 한 일:** 기록 구조 정리, 코드 작성 및 수정, 문서 초안과 표현 개선을 도왔습니다.
- **내가 직접 판단한 일:** 실제 리추얼 기록과 Task 10 실험 결과를 확인하고 공개할 경험, 숫자, 프로젝트와 문장을 직접 선택했습니다.
- **AI 제안을 따르지 않은 일:** 실제 기록이나 실험 결과에 없는 내용을 추가하지 않고, 직접 확인한 데이터와 판단을 기준으로 사이트와 결과물을 구성했습니다.

## 개인정보 및 보안

- 다른 사람의 실명과 연락처를 사이트에 공개하지 않았습니다.
- 비밀번호, API 키, 토큰 등의 비밀정보를 저장하거나 공개하지 않았습니다.
- 사이트 방문자의 로그인, 댓글, 별도 회원가입 기능은 사용하지 않습니다.
- BR-B 타이핑 앱은 개인 테스트 결과를 서버로 전송하지 않고 현재 브라우저에서만 표시합니다.
- SENTRA는 팀 프로젝트이며 저장소가 비공개이므로, 포트폴리오에는 공개 가능한 역할과 기술 요약만 제공합니다.
- Passkey Private Space는 WebAuthn 학습·시연용 프로젝트이며 실제 민감정보 보관 서비스가 아닙니다.

## 현재 한계

Continuing Device는 로컬 Python 프로그램입니다.

GitHub Pages에서 `records.json`을 수정한다고 해서 Python 프로그램이 서버에서 자동 실행되는 구조는 아닙니다.

따라서 새로운 기록을 사이트에 반영하려면 로컬에서 프로그램을 실행하고 결과를 확인한 뒤 GitHub Pages에 다시 배포해야 합니다.

BR-B 타이핑 집중 환경 비교기는 Task 10의 실험 결과를 기반으로 만든 개인 테스트 앱입니다. 논문 실험의 표본과 환경을 그대로 재현하는 도구가 아니며, 개인 테스트 결과와 논문 전체 실험 결과를 구분해서 확인하도록 구성했습니다.