# 이력서 원본

> 취업 준비용 기본 이력서입니다. 지원할 때는 채용공고에 맞춰 프로젝트와 기술의 순서를 조정하고, 실제로 수행한 범위와 확인된 결과만 기재합니다.

## 기본 정보

- 이름: 허민 (HEO MIN)
- 이메일: gjals0318@gmail.com
- GitHub: https://github.com/mingming-01
- 포트폴리오 저장소: https://github.com/mingming-01/career-portfolio
- 공개 프로필: https://my-profile-ohhl.onrender.com/

---

## 핵심 소개

반도체공학을 전공하고 Java·Spring 기반 백엔드 개발 교육과 Python·Flask 프로젝트를 경험했습니다. 개인 프로젝트에서는 NEXON Open API 데이터를 가공해 성장 기록을 저장·시각화하는 웹서비스를 만들고 Render에 배포했습니다. ALEPH 캡스톤 SENTRA에서는 Flask API, JWT 인증, 직원 초대 가입과 기간제 접근권한 흐름을 구현하고 주요 시나리오를 검증했습니다. 제조·생산관리 팀 프로젝트에서 BOM, 원자재, 입고·LOT, 창고와 재고 데이터를 다루며 제조 업무와 IT 시스템을 연결하는 분야에도 관심을 넓혀 왔습니다.

## 학력

### 인제대학교 나노융합공학부 반도체공학 전공
- 학위: 학사
- 관련 경험: 반도체 공정 실습, 클린룸 실습, 전공 실험
- 프로젝트: Arduino, Bluetooth, MIT App Inventor를 활용한 화재 알림 시제품

## 교육

### SKT K-뉴딜 ALEPH 1기
- 기간: 2026.08 ~ 2026.11 (2026년 11월 기준 과정 진행 중)
- 주요 내용: AI 활용, Python, Linux, API, 자동화, 데이터 분석 및 인프라 보안 실습
- 관련 경험: SENTRA 캡스톤, T10 타이핑 연구, Studio 과제 및 개인 앱 프로젝트

### ITWill 백엔드 개발 교육
- 기간: 2024.08 ~ 2025.05
- 주요 내용: Java, JavaScript, 웹 백엔드 개발, Spring 계열 기술, JSP, MyBatis 및 데이터베이스
- 관련 프로젝트: Stock-Mate, MrBean, Packtory_DE

---

## 기술 경험

| 분야 | 사용 경험 |
|---|---|
| 프로그래밍 | Java, JavaScript, Python, HTML5, CSS3, TypeScript |
| 백엔드 / 웹 | Spring Boot, Spring MVC, Flask, REST API, JSP, Thymeleaf, React |
| 데이터베이스 | MySQL, SQLite, H2, PostgreSQL(Supabase 연동 경험) |
| 데이터 접근 | MyBatis, JPA/Hibernate, SQLAlchemy |
| 인증 / 보안 | JWT, 비밀번호 해시, 역할·소속·자원 기반 접근 정책, WebAuthn/Passkey 실습 |
| API / AI | NEXON Open API, Gemini API, OpenRouter |
| 데이터 분석 | CSV 처리, Python 분석, 실험 결과 비교, Chart.js 시각화 |
| 개발 환경 / 배포 | Git, GitHub, Linux, Bash, Gradle, Node.js, npm, Render, GitHub Pages |
| 기타 | Arduino, Bluetooth, MIT App Inventor, CAD, 반도체 공정 실습 |

※ 각 기술의 숙련도는 동일하지 않습니다. 위 항목은 교육과 프로젝트에서 실제로 사용하거나 실습한 경험을 기준으로 정리했습니다.

---

## 주요 프로젝트

### SENTRA — 사내망 다계층 접근통제 시스템
- **유형:** ALEPH 1기 캡스톤 팀 프로젝트
- **기술:** Python, Flask, PyJWT, SQLite, React, TypeScript
- **GitHub:** https://github.com/mingming-01/sentra
- **주요 기여:**
  - Flask API 및 SQLite 기반 데이터 처리
  - 로그인 인증과 토큰 발급, 계정 상태 확인
  - 직원 명부와 사원번호·일회용 초대 코드를 이용한 가입 흐름
  - 직원 계정 비활성화에 따른 접근 제한
  - 기간제 권한 요청, 운영자 승인·반려, 만료·회수 흐름 구현
  - 접근 거부 사유 및 감사 로그 관련 기능 연결
  - 주요 가입·비활성화·권한 승인 전후 및 회수 후 시나리오 테스트
- **배운 점:** 인증과 인가의 구분, 서버 중심 접근통제, 임시 권한의 만료·회수 관리

### Maple Growth Tracker — 게임 성장 데이터 웹서비스
- **유형:** 개인 프로젝트
- **기술:** Python, Flask, NEXON Open API, JavaScript, Chart.js, Gemini API, SQLite, PostgreSQL(Supabase), Render
- **GitHub:** https://github.com/mingming-01/maple-growth-tracker
- **배포:** https://maple-growth-tracker.onrender.com
- **주요 기여:**
  - NEXON Open API 연동 및 캐릭터 데이터 가공
  - 날짜별 성장 기록 저장·조회 및 30일·90일 기간 데이터 수집
  - 경험치·성장량·랭킹 변화 계산과 그래프 시각화
  - Gemini API / OpenRouter 기반 AI 성장 리포트
  - 캐릭터 비교, 관심 캐릭터, PNG/PDF 결과 저장
  - 관리자 로그 조회 및 배포 환경의 DB 연결·저장 상태 점검
- **배운 점:** 외부 API 예외 처리, 데이터 누락 관리, 로컬·배포 환경의 데이터 저장 차이

### Packtory_DE — MES형 생산관리 팀 프로젝트
- **기간:** 2025.03 ~ 2025.05
- **기술:** Java 21, Spring Boot, JPA/Hibernate, MyBatis, QueryDSL, MySQL, H2, Thymeleaf, Gradle
- **GitHub:** https://github.com/mingming-01/packtory_
- **주요 기여:**
  - 직원 등록·조회·수정·삭제 및 상세 화면
  - 부서·하위 부서 코드 연결과 화면 표시 매핑
  - 직급 CRUD
  - Product 중심 데이터 구조 정리 및 제품 기능 구현
  - 원자재·창고·입출고 관련 기능
  - 품질 기준·검사 이력 및 근무 스케줄 기능
- **배운 점:** 공통코드와 계층형 조직 데이터, JPA·MyBatis 병행 구조, 기존 코드 구조를 이해한 뒤 기능을 확장하는 방식
- **추가 경험:** 팀 서버에서 기능을 시연·테스트했으며, 프로젝트 후반 Oracle 전환은 시도했으나 연결까지 완료하지 못함

### MrBean — 제조·생산관리 웹 프로젝트
- **기술:** Java 11, Spring MVC, MyBatis, MySQL, JSP, JSTL, JavaScript
- **GitHub:** https://github.com/shoqying/MrBean
- **주요 기여:**
  - 원자재 CRUD 및 JSP·Controller·Service·DAO·Mapper 연결
  - 완제품 CRUD와 BOM ID 연결
  - BOM 등록·조회·수정·삭제, 이름 중복 확인, ID 자동 생성
  - BOM 비율 0~100 검증 및 원자재 정보 JOIN 조회
  - 원자재 입고 CRUD와 날짜 기반 LOT 번호 생성·연결
  - 창고 관련 화면 일부 수정
- **배운 점:** 제조 데이터 간 관계와 Spring MVC·MyBatis 계층별 요청 흐름

### Stock-Mate — QR·바코드 기반 재고 관리 팀 프로젝트
- **기술:** Java 11, Spring Framework, MyBatis, MySQL, JSP, HTML5, CSS3, JavaScript, jQuery
- **GitHub:** https://github.com/in27sung/stock-mate
- **주요 기여:**
  - Category 등록·조회·수정·삭제 CRUD와 관련 SQL 및 JSP 화면
  - Stock 기능의 Controller, Service, DAO, Mapper, VO와 재고 JSP 수정
  - 사용자 정보 수정 오류 및 로그인 화면 일부 수정
  - UserController, 공통 예외 처리, Warehouse Mapper 일부 수정
- **배운 점:** 상품·카테고리·창고·재고·입출고 간 데이터 관계와 여러 계층을 연결하는 개발 방식

### T10 타이핑 연구 — 실험 설계 및 데이터 분석
- **유형:** ALEPH 연구 과제
- **기술:** HTML, CSS, JavaScript, Python, CSV
- **주요 기여:**
  - 시각적 효과 ON/OFF 조건의 타이핑 실험 페이지 구성
  - 총 10회 실험 및 CSV 데이터 수집
  - Python으로 조건별 속도·정확도 분석 및 그래프 작성
  - 가설과 실제 결과 비교
- **분석 결과:** OFF 평균 속도 594.67 / ON 평균 566.00, OFF 정확도 100 / ON 99.47
- **해석:** 제한된 실험에서 관찰한 결과로 한정하고 일반적인 효과로 확대하지 않음

---

## 기타 프로젝트

### My Profile — 개인 프로필 웹사이트
- GitHub: https://github.com/mingming-01/my-profile
- 배포: https://my-profile-ohhl.onrender.com/
- 개인 프로필 페이지 구성 및 배포
- T08 과제에서 WebAuthn/Passkey 등록·로그인, challenge 검증, 공개키 기반 인증, Flask session과 계정별 Private 데이터 접근 제어 실습

### PDS Diary — 계획·실행 기록 서비스
- 기술: Python, Flask, SQLAlchemy, SQLite, HTML/CSS/JavaScript, pytest
- Plan → Do → See → Improvement → Next Plan 구조의 개인 기록 서비스
- Plan Version History, Task와 Execution 분리, 예상·실제 시간 비교, 집계 근거 조회, JSON Export
- 자동화 테스트 15개 통과 및 실제 데이터 검증

### Arduino + Bluetooth + App Inventor 화재 알림 프로젝트
- Arduino 센서와 Bluetooth, MIT App Inventor를 연결해 센서 정보를 휴대폰에서 확인하는 화재 알림 시제품 구성

---

## 강점과 업무 방식

- **원인을 따라가며 해결합니다.** 오류가 발생하면 화면만 수정하지 않고 요청·응답, Controller, Service, 데이터 접근 계층과 실행 환경을 살펴봅니다.
- **실행 결과로 검증합니다.** 기능을 구현한 뒤 정상 상황과 예외 상황을 나누어 다시 실행합니다.
- **데이터를 기준으로 판단합니다.** T10에서 가설에 맞추기보다 실제 실험 결과를 기준으로 분석했습니다.
- **업무 흐름을 함께 봅니다.** 제조 프로젝트에서 BOM, 원자재, 입고, LOT, 창고와 재고 데이터가 연결되는 과정을 경험했습니다.
- **기존 구조를 이해하려고 합니다.** 팀 프로젝트에서는 기존 코드와 데이터 흐름을 먼저 살펴보고 다른 기능과 자연스럽게 연결되도록 작업합니다.

## 관심 직무

- 백엔드 / 웹서비스 개발
- MES / ERP 개발 및 제조 IT
- 제조·반도체 분야의 IT / 전산
- 계정·권한 및 시스템 운영 관련 직무

현재는 한 직무만으로 지원 방향을 고정하기보다 실제 채용공고의 담당 업무와 요구 기술을 비교하며 경험을 연결할 수 있는 직무를 좁혀 가고 있습니다.

## 자기소개 한 줄

> 궁금한 것을 파고들어 의미를 발견하고, 실제로 동작하는 결과로 만들며, 사람들과 함께 앞으로 나아가는 사람.
