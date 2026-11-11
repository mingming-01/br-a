# Continuing Device · 기록 집계 장치

BR-A의 기록 후보와 통계를 다시 생성하는 로컬 Python 프로그램입니다. AI가 내용을 자동으로 공개하지 않으며, 생성 결과를 확인하고 사이트에 반영할 내용은 직접 선택합니다. [저장소의 device 코드](https://github.com/mingming-01/br-a/tree/main/device)와 [문서 검증 workflow](https://github.com/mingming-01/br-a/blob/main/.github/workflows/auto-merge-career-documents.yml)에서 구현을 확인할 수 있습니다.

## 구조

```text
device/
├── input/
│   ├── records.json
│   ├── ritual-days.json
│   └── ritual-summary.json
├── output/
│   ├── candidates.json
│   └── stats.json
└── src/
    ├── generate.py
    └── stats.py
```

## 입력 데이터

- records.json: 사이트에 공개할 대표 기록 후보. 현재 35건.
- ritual-days.json: 날짜별 상태를 보관한 상세 요약 자료. 개인 회고 원문이나 동료 관련 텍스트는 포함하지 않습니다.
- ritual-summary.json: 과거에 입력한 집계 요약입니다. 현재 ritual-days.json과 날짜·건수가 일치하지 않아 재검증 전까지 공개 수치의 기준으로 사용하지 않습니다.

### 집계 검증 상태

현재 요약 파일은 기록 기간 2026-08-11 ~ 2026-11-12, 기록 61일로 되어 있지만, 날짜별 파일에는 53건만 있으며 마지막 날짜는 2026-11-02입니다. 마감 상태와 실천 상태별 수도 서로 일치하지 않습니다.

따라서 이 요약값을 사이트의 공개 통계로 사용하지 않습니다. 검증되지 않은 기존 `output/stats.json`은 삭제했습니다. 날짜별 원본을 확인해 요약 파일을 정정한 뒤 다시 생성해야 합니다. `stats.py`는 요약값과 날짜별 데이터의 일관성을 검사하며, 불일치가 있으면 생성에 실패하도록 관리합니다.

### 대표 기록 후보

대표 기록 후보 35건의 역량별 분포는 다음과 같습니다.

- 자기조절력: 14건
- 대인관계력: 13건
- 자기동기력: 8건

이 분포는 선별된 후보 35건에만 적용되며 전체 리추얼 기록의 역량별 분포를 의미하지 않습니다.

## 실행 방법

저장소 루트에서 실행합니다.

```bash
python3 device/src/generate.py
python3 device/src/stats.py
```

생성 결과:
- device/output/candidates.json
- device/output/stats.json

집계 요약과 날짜별 기록이 일치하는 경우에만 통계 파일이 생성됩니다. 불일치하면 `stats.py`가 오류를 내고 기존 결과를 새 값으로 덮어쓰지 않습니다.

## 업데이트 원칙

1. 공개할 대표 기록 후보는 input/records.json에 선별해 추가합니다.
2. 전체 기록의 최신 집계가 바뀌면 확인된 합계만 input/ritual-summary.json에 반영합니다.
3. 날짜별 상태를 공개 가능한 형태로 보완할 때는 개인 회고 원문을 넣지 않고 input/ritual-days.json에 필요한 요약만 추가합니다.
4. Python 프로그램을 실행하고 결과를 확인합니다.
5. 사이트에 공개할 내용을 직접 선택해 반영합니다.

## 판단과 개인정보

- 프로그램은 후보와 통계를 계산할 뿐 사이트에 자동 게시하지 않습니다.
- 원문 회고와 타인의 개인정보는 공개 입력 파일에 넣지 않습니다.
- 집계 숫자는 날짜별 원본 기록과 요약 파일, 최신 커리어 문서를 서로 대조해 확인한 뒤 업데이트합니다.
