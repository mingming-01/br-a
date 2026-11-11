# BR-A · Backend & Web Service Developer Portfolio

반도체 전공을 바탕으로 백엔드와 웹서비스를 개발하고, 제조·업무 시스템과 연결되는 문제를 탐구하는 개인 포트폴리오입니다.

**공개 사이트:** https://mingming-01.github.io/br-a/

## 목적

이 사이트는 이력서의 내용을 그대로 반복하기보다, 개발자로 방향을 정한 과정과 실제 프로젝트에서 맡은 역할, 문제를 해결하고 검증한 경험을 보여주기 위해 만들었습니다.

기존의 개인 소개와 기록을 유지하면서 대표 프로젝트의 기술적 내용과 담당 범위를 구체적으로 정리합니다. 팀 프로젝트는 전체 기능과 직접 구현한 범위를 구분하고, 학습·시연용 프로젝트는 그 한계를 함께 밝힙니다.

## 사이트 구성

- **Hero:** 백엔드·웹서비스 개발 지향점과 주력 기술, 프로젝트·문서 바로가기
- **About me:** 반도체 전공에서 소프트웨어 개발로 방향을 찾은 과정, 교육과 협업 경험
- **Records:** ALEPH 기간 중 작성한 리추얼 기록의 확인된 집계
- **Works:** 대표 프로젝트와 기타 개인·팀 프로젝트
- **Project Stack:** 실제 프로젝트에서 사용한 기술과 적용 영역
- **Documents:** 이력서, 자기소개서, 경력기술서 PDF
- **Continuing Device:** 기록을 정리하고 공개할 내용을 직접 선택하는 Python 자동화 장치

## 대표 프로젝트

### 01. Maple Growth Tracker

NEXON Open API의 캐릭터 데이터를 날짜별로 저장하고 성장 추이, 캐릭터 비교, AI 성장 리포트를 제공하는 개인 웹서비스입니다.

- 기획, 화면·서버 개발, 외부 API 연동, 데이터 저장 구조, 배포 담당
- 정상 데이터, 미공개 날짜, 일시적인 API 오류를 구분해 기록 관리
- 경험치와 랭킹 등 성장 지표는 별도 로직으로 계산하고 AI는 결과를 설명하도록 역할 분리
- Gemini 우선 사용 및 조건에 따른 OpenRouter 대체
- 자동 테스트와 GitHub Actions 검사 연결
- 기술: Python, Flask, React 19, Vite, PostgreSQL, SQLite, NEXON Open API, Gemini, OpenRouter
- 서비스: https://maple-growth-tracker.onrender.com/
- GitHub: https://github.com/mingming-01/maple-growth-tracker

### 02. SENTRA

직원의 역할·소속·개인 권한에 따라 사내 자원 접근을 판정하는 3인 팀 캡스톤 프로젝트입니다. 서버 백엔드를 담당했습니다.

- 로그인 인증, 토큰 발급, 비활성 계정 접근 차단
- 직원 명부 기반 사원번호·일회용 초대 코드 가입 및 재사용 방지
- 기간제 권한 요청·승인·반려·만료·회수 흐름
- 담당 기능의 요구사항, DB 스키마, 플로우차트 작성
- 직원 가입, 권한 요청, 승인과 회수 등 주요 시나리오 직접 확인
- 기술: Python, Flask, PyJWT, SQLite (화면은 React/TypeScript)
- 서비스 시연: https://sentra.koreacentral.cloudapp.azure.com/
- GitHub: https://github.com/mingming-01/sentra (비공개 저장소)

네트워크 장비 연동, Syslog/NetFlow 수집 등 별도 환경에서 확인할 기능은 직접 구현한 백엔드 범위와 구분합니다.

### 03. Packtory_DE

인사, 제품, 원자재, 창고, 입출고, 품질 검사, 근무 관리를 연결한 제조·물류 중심의 MES형 팀 프로젝트입니다.

- 직원·부서·직급 관리와 부서 코드 연결
- Product 구조 정리, 원자재·창고·위치·입출고 기능
- 품질 기준·검사 이력, 근무 스케줄 기능
- 기존 공통코드와 Mapper·Service·Controller 규칙을 읽고 팀 구조에 맞춰 개발
- 기술: Java 21, Spring Boot, JPA/Hibernate, MyBatis, QueryDSL, MySQL, Thymeleaf
- GitHub: https://github.com/mingming-01/packtory_

## 기타 프로젝트

- **My Profile:** 공개 프로필에서 출발해 Task 8에서 WebAuthn Passkey 기반 Private Space를 추가한 개인 웹 프로젝트. 계정별 데이터 분리와 Passkey 등록·로그인 검증을 구현했습니다. 학습·시연용 프로토타입입니다. 서비스: https://my-profile-ohhl.onrender.com/ · GitHub: https://github.com/mingming-01/my-profile
- **MrBean:** 원자재·완제품·BOM·입고·LOT 관리. Java 11, Spring MVC, MyBatis, MySQL, JSP. GitHub: https://github.com/shoqying/MrBean
- **Stock-Mate:** QR/바코드 기반 상품·재고·창고 관리. 카테고리와 재고 기능 담당. Java 11, Spring MVC, MyBatis, MySQL, JSP, jQuery. GitHub: https://github.com/in27sung/stock-mate
- **T10 타이핑 연구:** 화면 효과 ON/OFF 조건 각 15회, 총 30회 측정 후 Python 분석. 표본이 작고 동일 문장 비교 결과가 일관되지 않아 관찰 범위 안에서만 해석했습니다. 연구 결과: https://mingming-01.github.io/typing-focus-research/ · GitHub: https://github.com/mingming-01/typing-focus-research
- **BR-B:** T10 연구를 바탕으로 개인 타이핑 속도와 정확도를 비교하는 웹 앱. 앱: https://mingming-01.github.io/typing-focus-app/ · GitHub: https://github.com/mingming-01/typing-focus-app
- **PDS Diary:** PLAN / DO / SEE 방식의 계획·실행·회고 서비스. 계획 변경 이력, 예상·실제 시간 비교, 데이터 내보내기 및 자동 테스트 15개. 서비스: https://pds-diary-0u5g.onrender.com/ · GitHub: https://github.com/mingming-01/pds-diary

## Project Stack

기술 숙련도를 임의의 점수로 표현하지 않고, 실제 사용한 프로젝트와 연결해 소개합니다.

| 영역 | 기술 및 경험 |
|---|---|
| Backend | Python, Flask, Java, Spring Boot, Spring MVC, REST API |
| Frontend | JavaScript, TypeScript, React, HTML, CSS, Thymeleaf, JSP |
| Database | PostgreSQL, SQLite, MySQL, JPA/Hibernate, MyBatis |
| Authentication & Integration | JWT, WebAuthn, NEXON Open API, Gemini API, OpenRouter |
| Test & Delivery | unittest, pytest, GitHub Actions, Git, Linux, Render, Vercel, GitHub Pages |
| Domain | 제조·생산관리, 원자재, BOM, 재고, 창고, 입출고, 품질·근무 관리 |

## Records 집계 기준

최신 자기소개서에 반영된 집계를 사용합니다.

- 기록 기간: 2026-08-11 ~ 2026-11-12
- 기록한 날: **61일**
- '실천했다': **57일**
- '일부 실천했다': **4일**

이 수치는 날짜별 원문 회고를 공개하지 않고, 확인된 집계값만 공개합니다. 별도로 관리하는 대표 기록 후보 35건은 전체 기록 일수와 다른 자료이며, 역량별 분류(자기조절력 14건, 대인관계력 13건, 자기동기력 8건)는 해당 후보 35건에만 적용됩니다.

## 제출 문서와 자동화

공개 문서는 원본 저장소 mingming-01/career-portfolio에서 관리합니다.

- 웹페이지용 Markdown: 01_이력서 폴더의 최신 문서
- 제출용 서식 원본: 제출용_초안 폴더의 최신 DOCX
- BR-A 공개 파일: documents 폴더의 Markdown 및 PDF

자동화 흐름은 다음과 같습니다.

1. 원본 저장소의 지정 Markdown 또는 DOCX가 변경되면 GitHub Actions가 실행됩니다.
2. Markdown은 BR-A의 documents 폴더로 복사합니다.
3. DOCX는 LibreOffice headless로 PDF 변환합니다. PDF의 레이아웃은 Markdown이 아니라 DOCX를 기준으로 합니다.
4. BR-A에 문서 동기화 PR을 생성합니다.
5. BR-A의 문서 검증 workflow가 허용된 파일 경로, Markdown, PDF 형식을 검사하고 통과한 문서 동기화 PR을 자동 병합합니다.

원본 저장소에는 BRA_SYNC_TOKEN을 GitHub Actions secret으로 설정해야 합니다. PDF 변환 결과는 원본 DOCX의 서식과 변환 환경에 영향을 받으므로, 배포 후 페이지별 시각 검수도 필요합니다.

## Continuing Device

device 폴더에는 공개할 기록 후보와 통계를 다시 생성하는 Python 프로그램이 있습니다.

- device/src/generate.py: device/input/records.json에서 공개 후보 생성
- device/src/stats.py: 최신 확인 집계와 대표 기록 후보를 읽어 device/output/stats.json 생성
- device/input/ritual-summary.json: 최신 자기소개서 기준의 확인된 합계
- device/input/ritual-days.json: 날짜별 상태를 별도로 보관한 상세 요약 자료
- device/output/: 사이트에서 사용하는 결과 파일

통계는 다음 명령으로 재생성할 수 있습니다.

```bash
python3 device/src/generate.py
python3 device/src/stats.py
```

AI가 내용을 자동으로 게시하지 않습니다. 생성된 후보를 확인하고 실제 공개할 내용을 선택하는 최종 판단은 직접 합니다.

## 로컬 확인

정적 사이트이므로 별도 빌드 과정 없이 저장소 루트의 index.html을 브라우저에서 열어 확인할 수 있습니다. Records 통계는 device/output/stats.json을 읽습니다.

## 개인정보와 표현 원칙

- 공개 가능한 개인 연락처와 프로젝트 링크만 표시합니다.
- 팀 프로젝트는 직접 담당한 기능과 팀 전체 기능을 구분합니다.
- 실제로 완료하지 못한 DB 전환이나 별도 환경이 필요한 네트워크 연동은 완료한 것처럼 표현하지 않습니다.
- My Profile은 학습·시연용 프로토타입이며 실제 민감정보 보관 서비스가 아닙니다.
- SENTRA 저장소는 비공개이며 공개 페이지에는 공개 가능한 역할과 기술만 요약합니다.
