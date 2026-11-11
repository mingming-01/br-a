# BR-A · Backend & Web Service Developer Portfolio

반도체공학을 전공한 뒤 백엔드 개발을 공부하고, 개인·팀 프로젝트에서 웹서비스와 업무 시스템을 구현해 온 허민의 개발자 포트폴리오입니다.

**Portfolio:** https://mingming-01.github.io/br-a/  
**GitHub:** https://github.com/mingming-01  
**Contact:** gjals0318@gmail.com

## 소개

현재 신입 백엔드·웹서비스 개발을 중심으로 취업을 준비하고 있으며, 반도체 전공과 제조 프로젝트 경험을 연결할 수 있는 MES·ERP·제조 IT 분야에도 관심이 있습니다.

프로젝트를 소개할 때 기술 목록만 나열하기보다 다음 내용을 구분해 기록합니다.

- 해결하려고 한 문제와 서비스의 목적
- 직접 담당해 구현한 기능과 팀 전체의 기술 환경
- 구현 과정에서 고려한 데이터·인증·권한·실패 처리
- 테스트하거나 실제 실행해 확인한 범위
- 완료하지 못했거나 별도 환경에서 확인해야 하는 범위

## 사이트 구성

| 섹션 | 내용 |
|---|---|
| Hero | 개발 방향, 주력 기술, 대표 프로젝트와 문서 링크 |
| About me | 반도체 전공에서 소프트웨어 개발로 방향을 정한 과정 |
| Works | 대표 프로젝트 3개, ALEPH 보안 과제와 보조 프로젝트 |
| Records | 리추얼 기록의 집계 절차와 공개 기준 (수치 재검증 중) |
| Project Stack | 기술을 실제 적용한 프로젝트와 연결해 소개 |
| Documents | 이력서·자기소개서·경력기술서 PDF |
| Continuing Device | Python으로 기록을 집계하고 공개 내용을 선택하는 자동화 흐름 |

## 대표 프로젝트

### 01. Maple Growth Tracker

**공개 API 데이터를 날짜별로 축적하고 성장 흐름을 분석하는 개인 웹서비스**

- 서비스: https://maple-growth-tracker.onrender.com/
- 저장소: https://github.com/mingming-01/maple-growth-tracker
- 담당: 기획, 화면·서버 개발, 데이터 저장 구조, 외부 API 연동, 배포

캐릭터 조회 API는 현재 상태를 보여 주는 데 집중되어 있어, 시간에 따른 성장을 보려면 과거 데이터를 직접 수집하고 보관해야 했습니다. NEXON Open API의 캐릭터 정보를 날짜별로 저장해 성장 추이, 캐릭터 비교, 상세 정보, AI 리포트를 제공하도록 만들었습니다. 배포 후 지인 10명 내외가 사용했고, 받은 피드백과 건의사항 중 서비스 방향에 맞는 내용을 일부 반영해 개선했습니다.

**구현한 내용**
- Flask API와 React 19 화면을 분리하고 Vite 기반 프런트엔드 개발 환경 구성
- 최근 7일 기록 수집과 30일·90일 과거 기록 보충, 10일 단위 요청 및 저장 데이터 재사용
- 경험치 증가량, 일평균, 레벨 진행률, 랭킹 변화, 기간 비교와 타임라인 계산
- 두 캐릭터의 동일 기간 성장 지표 비교와 AI 성장 리포트
- 스탯·장비·심볼·스킬·링크·유니온 등 상세 정보를 탭 선택 시 개별 조회
- PostgreSQL(배포)과 SQLite(로컬) 저장 환경 구성
- Python 테스트, JavaScript 테스트, React 빌드 검사를 GitHub Actions에 연결

**설계에서 고려한 점**
- API가 아직 공개하지 않은 날짜, 아직 수집하지 않은 날짜, 일시적인 조회 오류를 구분합니다.
- 정상적으로 저장된 과거 기록을 빈 응답이나 일시적 오류로 덮어쓰지 않습니다.
- 기록이 없는 구간의 성장량을 0으로 간주하거나 임의로 보간하지 않습니다.
- 성장 지표는 애플리케이션 로직에서 계산하고, AI는 계산된 값과 기록을 자연어로 설명합니다.
- Gemini를 우선 사용하며 설정 및 오류 조건에 따라 OpenRouter를 대체 경로로 사용합니다.
- 다음 레벨 예상은 계산 가능한 관측값이 충분할 때만 참고값으로 표시합니다.

**기술:** Python, Flask, React 19, Vite, PostgreSQL, SQLite, Chart.js, NEXON Open API, Gemini API, OpenRouter, Render

### 02. SENTRA

**직원 계정과 기간제 권한을 관리하는 사내망 다계층 접근통제 시스템**

- 서비스 시연: https://sentra.koreacentral.cloudapp.azure.com/
- 저장소: https://github.com/mingming-01/sentra (비공개)
- 형태: ALEPH 1기 3인 팀 캡스톤
- 역할 분담: 조장은 Azure 서버·아키텍처·프론트엔드·챗봇, 다른 팀원은 네트워크 가상망·Packet Tracer, 본인은 Flask 서버 백엔드
- 담당: 인증·직원 데이터·권한 요청 처리, 화면과 API의 요청·응답 규격 조율

직원의 역할과 소속, 개인별 권한에 따라 사내 자원 접근을 허용하거나 거부하는 시스템입니다. 저는 서버 백엔드를 맡아 계정 생성부터 접근 권한의 요청·승인·만료·회수까지 이어지는 흐름을 구현했습니다.

**구현한 내용**
- 비밀번호 해시 기반 로그인과 JWT 발급
- 직원 명부의 사원번호와 일회용 초대 코드를 확인하는 가입 절차
- 초대 코드 재사용 방지 및 비활성 계정의 로그인·보호 API 접근 차단
- 직원 및 사용자 데이터 저장 구조와 마이페이지 연동
- 기간제 권한 요청, 운영자 승인·반려, 승인 권한 만료·회수 처리
- React 기반 팀 화면과 Flask API의 요청·응답 규격 조율 (TypeScript는 조장 담당 화면의 기술 환경)
- 담당 기능의 요구사항 정의, DB 스키마, 플로우차트 작성

**검증한 시나리오**
직원 사전 등록과 초대 가입, 사용한 초대 코드 재사용 거부, 비활성 계정 차단, 권한 요청·승인·회수 후 접근 결과를 실행해 확인했습니다. 화면에서 메뉴를 숨기는 것만으로 접근을 통제하지 않고 서버가 요청마다 인증과 정책을 판단하도록 구성했습니다.

**기술:** 개인 담당 범위는 Python, Flask, PyJWT, SQLite입니다. React·TypeScript는 조장이 담당한 팀 화면의 기술 환경이며 개인 담당 기술과 구분합니다.

네트워크 가상망·Packet Tracer, Syslog/NetFlow 수집, Discord 알림 등은 팀의 별도 담당 영역 또는 별도 환경에서 확인할 범위로 구분합니다.

### 03. Packtory_DE

**인사·제품·자재·창고·품질·근무 업무를 연결한 MES형 생산관리 팀 프로젝트**

- 저장소: https://github.com/mingming-01/packtory_
- 기간: 2025.03 ~ 2025.05
- 형태: ITWill 심화 과정 팀 프로젝트

기존 공통 구조를 이해한 뒤 여러 제조 업무 기능을 연결해 구현한 프로젝트입니다. 프로젝트 중 팀원 한 명이 취업으로 이탈했고, 남은 팀원들과 팀 서버 시연까지 마쳤습니다. 직원 등록·조회·수정·삭제, 부서·하위 부서와 직급 관리, Product 구조 정리, 원자재·창고·위치·입출고, 품질 기준·검사 이력, 근무 스케줄 기능을 작업했습니다.

**개발 과정에서 경험한 내용**
- Controller, Service, DTO, Entity, Mapper와 Thymeleaf 화면을 함께 수정
- 관리자가 등록한 공통코드를 사용하고 DB에는 코드값, 화면에는 한글 명칭을 표시하는 변환 처리
- 기존 Item 중심 코드를 Product 중심으로 정리
- JPA와 MyBatis가 함께 사용되는 데이터 접근 구조 파악
- 팀 서버에서 기능 실행 및 시연

프로젝트 후반 MySQL에서 Oracle로 전환을 시도했으나 SQL·드라이버·설정 수정 범위가 예상보다 커 최종 연결까지 완료하지 못했습니다. 따라서 DB 전환은 완료한 결과로 표현하지 않습니다.

**기술:** Java 21, Spring Boot, JPA/Hibernate, MyBatis, QueryDSL, MySQL, Thymeleaf

## 기타 프로젝트

- **My Profile:** ALEPH 과제로 공개 프로필과 WebAuthn Passkey Private Space를 구현한 프로젝트. 일회용 초대 코드, Challenge 및 RP ID·Origin 검증, 계정별 데이터 분리와 Passkey 관리 기능을 적용했습니다. 학습·시연용 프로토타입이며 실제 민감정보 보관 서비스가 아닙니다. [서비스](https://my-profile-ohhl.onrender.com/) · [GitHub](https://github.com/mingming-01/my-profile)
- **ALEPH 보안 과제:** 보안 방어전 로그인·본인 자료 조회·등록 기기 판정·백업 복원 API, 방어전 결과를 확인하는 로컬 앱, XDR 웹 주입 탐지 판정 규칙을 수행했습니다.
- **MrBean:** 원자재·완제품 CRUD, BOM 연결과 입력값 검증, 날짜 기반 LOT 번호 생성, 입고일 기준 유통기한 계산. Java 11, Spring MVC, MyBatis, MySQL, JSP. [GitHub](https://github.com/shoqying/MrBean)
- **Stock-Mate:** QR·바코드 기반 상품·재고·창고 관리 프로젝트. 카테고리 CRUD와 SQL·화면 연결, 재고 목록 및 사용자 정보 수정 오류 등을 담당. Java 11, Spring MVC, MyBatis, MySQL, JSP, jQuery. [GitHub](https://github.com/in27sung/stock-mate)
- **T10 · BR-B:** 시각 효과 ON/OFF 조건 각 15회, 총 30회 측정과 Python 분석을 수행하고, 결과를 바탕으로 개인 타이핑 속도와 정확도를 비교하는 웹 앱을 만들었습니다. 표본이 작고 비교 결과가 일관되지 않아 관찰 범위 안에서 해석했습니다. [연구 결과](https://mingming-01.github.io/typing-focus-research/) · [비교 앱](https://mingming-01.github.io/typing-focus-app/)
- **PDS Diary:** PLAN / DO / SEE 방식의 계획·실행·회고 서비스. 계획 변경 이력, 예상·실제 시간 비교, 데이터 내보내기와 자동 테스트 15개를 구현했습니다. [서비스](https://pds-diary-0u5g.onrender.com/) · [GitHub](https://github.com/mingming-01/pds-diary)

## 기술과 적용 경험

| 영역 | 기술 | 적용 프로젝트 |
|---|---|---|
| Backend | Python, Flask, Java, Spring Boot, Spring MVC, REST API | Maple Growth Tracker, SENTRA, Packtory_DE, MrBean, Stock-Mate |
| Frontend | JavaScript, React, HTML, CSS, Thymeleaf, JSP | Maple Growth Tracker, ITWill 팀 프로젝트 |
| Team UI environment | TypeScript | SENTRA 팀 화면 (조장 담당, 개인 담당 기술과 구분) |
| Database | PostgreSQL, SQLite, MySQL, JPA/Hibernate, MyBatis | Maple Growth Tracker, SENTRA, Packtory_DE |
| Authentication & Integration | 비밀번호 해시, JWT, WebAuthn, NEXON Open API, Gemini, OpenRouter | SENTRA, My Profile, Maple Growth Tracker |
| Test & Delivery | unittest, pytest, GitHub Actions, Git, Linux, Render, Vercel, GitHub Pages | 개인 서비스와 팀 프로젝트 |
| Domain | 제조·생산관리, 원자재, BOM, 재고, 창고, 입출고, 품질·근무 관리 | Packtory_DE, MrBean, Stock-Mate |

기술 숙련도를 임의의 점수로 표현하지 않고, 프로젝트에서 실제 사용한 기술과 담당 범위를 함께 제시합니다.

## Records 집계 기준

리추얼 기록은 Python으로 집계하고, 공개할 기록 후보는 직접 검토하는 방식으로 관리합니다. 다만 현재 BR-A의 요약 파일(61일, 2026-11-12 종료)과 날짜별 상세 기록(53건, 2026-11-02 마지막 기록)이 일치하지 않습니다. 최신 자기소개서에서도 해당 수치의 출처를 확인하지 못했습니다.

따라서 **날짜별 원본과 요약 기준을 다시 대조하기 전까지 전체 기록 수와 실천 수치는 공개하지 않습니다.** 공개 후보 35건의 역량별 분포는 전체 기록 일수와 별개인 선별 자료이므로 전체 기록 통계처럼 사용하지 않습니다.

## 제출 문서와 자동 동기화

이력서·자기소개서·경력기술서의 원본은 [career-portfolio](https://github.com/mingming-01/career-portfolio)에서 관리합니다. BR-A의 `documents/` 폴더는 공개용 사본입니다.

현재 자동화 흐름은 다음과 같습니다.

1. 원본 저장소의 지정 Markdown 또는 DOCX 변경을 GitHub Actions가 감지합니다.
2. 웹페이지용 Markdown을 BR-A의 `documents/`로 복사합니다.
3. 제출용 DOCX는 LibreOffice headless로 PDF 변환합니다. PDF 레이아웃의 기준은 Markdown이 아니라 DOCX입니다.
4. BR-A에 문서 동기화 PR을 생성합니다.
5. BR-A의 문서 검증 workflow가 허용된 경로와 파일 형식을 검사하고, 검증을 통과한 문서 동기화 PR을 자동 병합합니다.

원본 저장소에는 `BRA_SYNC_TOKEN`을 GitHub Actions secret으로 설정해야 합니다. PDF 변환은 원본 DOCX 서식과 변환 환경의 영향을 받으므로, 자동화 성공 여부와 별개로 페이지별 시각 검수가 필요합니다.

## Continuing Device

`device/`에는 기록 후보와 집계 결과를 생성하는 Python 프로그램이 있습니다. [기록 집계 코드](https://github.com/mingming-01/br-a/tree/main/device)와 [문서 검증 workflow](https://github.com/mingming-01/br-a/blob/main/.github/workflows/auto-merge-career-documents.yml)를 공개합니다.

- `device/src/generate.py`: `device/input/records.json`에서 공개 기록 후보 생성
- `device/src/stats.py`: 확인된 최신 집계와 대표 기록 후보를 읽어 `device/output/stats.json` 생성
- `device/input/ritual-summary.json`: 과거에 입력한 집계 요약. 날짜별 기록과 불일치가 확인되어 재검증 전까지 공개 수치의 근거로 사용하지 않음
- `device/input/ritual-days.json`: 날짜별 상태를 보관한 상세 요약 자료
- `device/output/`: 웹페이지에서 사용하는 결과 파일

재생성 명령:

```bash
python3 device/src/generate.py
python3 device/src/stats.py
```

AI가 내용을 자동 게시하지 않습니다. 생성된 후보를 확인하고 공개할 내용을 선택하는 최종 판단은 직접 합니다.

## 로컬 확인

정적 사이트이므로 별도 빌드 도구 없이 저장소 루트의 `index.html`을 브라우저에서 열어 확인할 수 있습니다. Records는 `device/output/stats.json`을 읽으므로 로컬 파일 직접 열기에서 fetch가 제한되면 간단한 정적 서버를 사용합니다.

## 업데이트 원칙

- 프로젝트 내용은 career-portfolio의 최신 이력서·자기소개서·경력기술서와 프로젝트별 정보를 기준으로 갱신합니다.
- 직접 구현한 기능과 팀 전체의 기능을 구분합니다.
- 미완료 작업과 별도 환경에서 검증해야 하는 항목은 완료한 것처럼 쓰지 않습니다.
- 기술 목록은 실제 저장소와 프로젝트 문서에서 사용 여부를 확인한 뒤 반영합니다.
- 공개 가능한 연락처와 링크만 게시하며, 비공개 저장소의 코드나 민감한 정보를 공개하지 않습니다.
