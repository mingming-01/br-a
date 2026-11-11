# 이력서

(사진 3 x 4 cm 자리)
- **이름**: 허민 (HEO MIN)
- **지원 분야**: 신입 백엔드/웹서비스 개발 (MES, ERP, 제조 IT 포함)
- **연락처**: 010-0000-0000
- **이메일**: gjals0318@gmail.com
- **링크**: github.com/mingming-01 / mingming-01.github.io/br-a

## 자기소개

반도체공학을 전공했고, 대학 캡스톤에서 직접 만든 장치가 반응하는 재미를 느껴 소프트웨어 개발을 시작했습니다. 백엔드 교육과 팀, 개인 프로젝트에서 외부 API 연동, 데이터 저장과 검증, 접근 권한 처리를 구현했고, 만든 서비스를 배포해 다른 사람이 쓰는 데까지 해 봤습니다. 백엔드와 웹서비스 개발자로 일하고 싶고, 제조 업무 시스템에도 관심이 있습니다.

## 학력 및 교육

| 기간 | 기관/과정 | 내용 |
|---|---|---|
| 2020 ~ 2024 | **인제대학교 나노융합공학부**; 반도체공학 전공 / 학사 졸업 | 반도체 공정과 클린룸 실습, 전공 실험. 2학년과 4학년 캡스톤 2건 수행 (기타 활동 참고) |
| 2024.08 ~ 2025.05 | **ITWill 백엔드 개발 교육**; 약 9개월 과정 | Java와 JavaScript 기반 웹 개발. 팀 프로젝트 3건(Stock-Mate, MrBean, Packtory_DE) 수행 |
| 2026.08 ~ 2026.11 | **SKT K-뉴딜 ALEPH 1기**; 2026.11.12 수료 예정 | Python, Linux, 데이터 분석, 인프라 보안 실습. 3인 팀 캡스톤 SENTRA 수행. 과제 다수를 Render, Vercel 등에 배포 |

## 프로젝트

각 프로젝트의 담당 기능, 문제 해결 과정, 검증 내용은 경력기술서에 정리했습니다.

#### Maple Growth Tracker
*개인 프로젝트 / 2026.09 ~ 진행 중 / Python, Flask, React, PostgreSQL, SQLite, Render*

- **개요**  NEXON Open API의 캐릭터 레벨, 경험치, 랭킹을 날짜별로 저장해 기간별 성장 추이, 캐릭터 비교, AI 성장 리포트를 보여 주는 웹서비스. 배포해 지인 10명 내외가 사용, 받은 피드백 일부 반영
- **담당**  기획, 개발, 배포 전체. React 화면, Flask API, 외부 API와 AI 연동, DB 저장소를 계층으로 나눠 구성
- **확인**  정상 데이터, 데이터가 없는 날짜, API 오류 상황을 나눠 테스트하고 GitHub Actions로 자동 검사 연결
- github.com/mingming-01/maple-growth-tracker | maple-growth-tracker.onrender.com

#### SENTRA
*ALEPH 1기 캡스톤 | 3인 팀 / 2026 / Python, Flask, PyJWT, SQLite*

- **개요**  직원의 역할, 소속, 개인 권한에 따라 사내 자원 접근을 서버가 허용하거나 거부하는 접근통제 시스템
- **담당**  서버(백엔드) 전반. 로그인 인증, 초대 코드 기반 직원 가입, 계정 비활성화, 기간제 권한의 승인, 만료, 회수. 담당 기능의 요구사항, DB 스키마, 플로우차트 문서 작성
- **확인**  직원 가입, 초대 코드 재사용 방지, 비활성 계정 차단, 권한 승인과 회수 시나리오를 직접 실행해 확인
- github.com/mingming-01/sentra | sentra.koreacentral.cloudapp.azure.com

#### Packtory_DE
*ITWill 심화 팀 프로젝트 / 2025.03 ~ 2025.05 / Java 21, Spring Boot, JPA, MyBatis, QueryDSL, MySQL*

- **개요**  인사, 제품, 원자재, 창고, 입출고, 품질, 근무관리를 연결한 생산관리(MES형) 시스템. 팀 서버에서 시연
- **담당**  직원/부서/직급 관리, 원자재/창고/입출고, 품질 기준, 근무 스케줄 기능. 팀 리더가 만든 공통 규칙을 읽고 맞춰 개발
- github.com/mingming-01/packtory_

#### MrBean
*ITWill 팀 프로젝트 / Java 11, Spring MVC, MyBatis, MySQL, JSP*

- **개요**  제조/생산관리 웹 서비스. **담당**  원자재, 완제품, BOM(제품 구성) 관리, 원자재 입고와 LOT 번호 생성
- github.com/shoqying/MrBean

#### Stock-Mate
*ITWill 팀 프로젝트 / Java 11, Spring MVC, MyBatis, MySQL, JSP, jQuery*

- **개요**  QR/바코드 기반 상품, 재고, 창고 관리 웹 서비스. **담당**  카테고리와 재고 기능
- github.com/in27sung/stock-mate

## 기술

- **주력**: Python/Flask, Java/Spring Boot, SQL
- **언어**: Java, Python, JavaScript, SQL, HTML/CSS
- **서버/웹**: Spring Boot, Spring MVC, Flask, REST API, React, JSP, Thymeleaf
- **데이터**: MySQL, SQLite, PostgreSQL(Supabase), MyBatis, JPA/Hibernate, SQLAlchemy
- **인증/보안**: 비밀번호 해시, JWT, 기간제 권한 처리, WebAuthn(패스키)
- **도구/배포**: Git/GitHub, Linux, unittest, pytest, GitHub Actions, Render, Vercel, GitHub Pages

프로젝트에서 직접 사용한 기술만 적었습니다.

## 기타 활동

- **ALEPH 보안 방어전**: 로그인, 본인 자료만 조회, 등록 기기 판정, 백업 한 건 복원 API를 단계별로 구현 (Vercel, Supabase)
- **내 보안 Agent**: 방어전 서비스를 직원 화면으로 확장한 개인 앱. 로컬 실행
- **My Profile**: 패스키(WebAuthn) 등록과 로그인과 계정별 데이터 분리 실습 (Render, Supabase)
- **XDR 웹 주입 탐지**: 경보 기록을 차단, 경고, 기록으로 나누는 판정 규칙 작성
- **T10 타이핑 연구**: 화면 효과 ON/OFF 각 15회, 총 30회 측정과 Python 분석. 표본이 작아 관찰한 범위에서만 해석 (2026.10)
- **PDS Diary**: 계획, 실행, 회고를 기록하는 개인 서비스. 자동 테스트 15개로 동작 확인
- **BR-A 포트폴리오**: 소개, 대표 작업, 제출 문서를 한곳에 공개 (GitHub Pages)
- **대학 캡스톤 2건**: 2학년: Arduino 센서 정보를 Bluetooth로 휴대폰 앱(MIT App Inventor)에 전달하는 화재 알림 시제품; 4학년: 온습도 센서 값에 따라 가습기 모듈이 동작과 정지하고 앱으로 원격 제어하는 가습기 (팀 프로젝트, 제어 코드, 앱 연동, 시연 담당)
