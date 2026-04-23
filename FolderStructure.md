# 프로젝트 폴더 구조 설명

```
SpezProgrammierungGr1/
├── services/
│   ├── data-service/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── routes.py
│   │   ├── tests/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── ai-service/
│       ├── app/
│       │   ├── __init__.py
│       │   ├── main.py
│       │   ├── analysis.py
│       │   └── charts.py
│       ├── tests/
│       ├── Dockerfile
│       └── requirements.txt
├── k8s/
│   ├── data-service/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── ai-service/
│       ├── deployment.yaml
│       └── service.yaml
├── data/
│   └── csv/
├── docs/
│   ├── aufgabe.md
│   └── roles.md
├── docker-compose.yml
├── .env.example
├── CLAUDE.md
└── README.md
```

---

## services/
마이크로서비스들을 모아두는 폴더. 서비스가 늘어나도 여기에 추가하면 됨.

### services/data-service/
Viet 담당. CSV 파일을 읽어서 통계(Mean, Peak, Trend)를 계산하고 JSON API로 제공하는 서비스.

- **app/** — FastAPI 앱 코드를 담는 Python 패키지 폴더
  - **`__init__.py`** — 이 폴더가 Python 패키지임을 알려주는 빈 파일. 없으면 import가 안 됨
  - **`main.py`** — FastAPI 앱 진입점. 서버 설정, 앱 시작 코드가 여기 들어감
  - **`routes.py`** — API 엔드포인트 정의. 예: `GET /stats` → Mean, Peak, Trend 반환
- **tests/** — 단위 테스트 파일 보관
- **`Dockerfile`** — 이 서비스를 Docker 컨테이너로 만드는 설정 파일
- **`requirements.txt`** — 필요한 Python 라이브러리 목록 (fastapi, pandas 등)

### services/ai-service/
내(Dongwoo) 담당. Data Service에서 통계를 받아와서 LLM으로 해석하고 시각화를 생성하는 서비스.

- **app/** — FastAPI 앱 코드를 담는 Python 패키지 폴더
  - **`__init__.py`** — 패키지 선언용 빈 파일
  - **`main.py`** — FastAPI 앱 진입점
  - **`analysis.py`** — OpenAI API 호출해서 텍스트 해석 생성하는 로직
  - **`charts.py`** — matplotlib으로 시각화 차트 생성하는 로직
- **tests/** — 단위 테스트 파일 보관
- **`Dockerfile`** — 이 서비스를 Docker 컨테이너로 만드는 설정 파일
- **`requirements.txt`** — 필요한 Python 라이브러리 목록 (fastapi, openai, matplotlib 등)

---

## k8s/
Kubernetes 배포 설정 파일들. Viet 담당.

- **data-service/**
  - **`deployment.yaml`** — Data Service 컨테이너를 Kubernetes에서 몇 개 실행할지, 어떤 이미지 쓸지 정의
  - **`service.yaml`** — Data Service를 클러스터 내부에서 접근 가능하게 네트워크 설정
- **ai-service/**
  - **`deployment.yaml`** — AI Service 배포 설정
  - **`service.yaml`** — AI Service 네트워크 설정

---

## data/csv/
Google Trends에서 받은 CSV 파일 보관 폴더.
- `interest_over_time.csv` — 시간별 검색 관심도
- `top_queries.csv` — 연관 상위 검색어
- `rising_queries.csv` — 급상승 검색어

---

## docs/
프로젝트 내부 문서. 제출물 아님.
- **`aufgabe.md`** — 교수님이 준 과제 원본
- **`roles.md`** — 팀 역할 분담

---

## 루트 파일들

- **`docker-compose.yml`** — 로컬에서 두 서비스를 동시에 실행하는 설정. `docker compose up -d` 명령어로 실행
- **`.env.example`** — 필요한 환경변수 목록 예시. 실제 API 키는 `.env`에 넣고 gitignore로 커밋 안 함
- **`CLAUDE.md`** — Claude Code AI가 이 프로젝트에서 어떻게 동작할지 정의한 설정 파일
- **`README.md`** — 제출용. 7개 질문 답변 (프로젝트 완성 후 작성)