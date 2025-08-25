# JLPT 학습 퀴즈

일본어 능력시험(JLPT) 학습을 위한 터미널 기반 퀴즈 애플리케이션입니다.

## 주요 기능

- **레벨 선택**: N5-N1 레벨 지원 (현재 N4 사용 가능)
- **학습 모드**: 어휘, 문법, 혼합 퀴즈
- **맞춤 설정**: 문제 수, 답안 표시 방식, 히라가나 표시 옵션
- **한국어 인터페이스**: 모든 UI와 해설이 한국어로 제공
- **학습 분석**: 점수 추적 및 약점 분석

## 설치 및 실행

### Make를 이용한 설치 및 실행 (가장 간편)
```bash
# 설치
make setup

# 실행
make run

# 도움말 보기
make help
```

### 스크립트를 이용한 자동 설치
```bash
./install.sh
```

### 수동 설치
1. 가상환경 생성 및 활성화:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

3. 애플리케이션 실행:
```bash
python run.py
```

## 퀴즈 데모

전체 메뉴 없이 빠른 퀴즈를 체험해보세요:

```bash
# 가상환경 활성화 후
source venv/bin/activate
python demo.py
```

## Make 명령어

| 명령어 | 설명 |
|--------|------|
| `make setup` | 가상환경 설정 및 의존성 설치 |
| `make run` | 애플리케이션 실행 |
| `make demo` | 빠른 퀴즈 데모 (3문제) |
| `make validate` | N4 데이터 검증 |
| `make validate-all` | 모든 레벨 데이터 검증 |
| `make clean` | 임시 파일 정리 |
| `make clean-all` | 가상환경까지 모두 정리 |
| `make info` | 프로젝트 정보 표시 |
| `make help` | 모든 명령어 보기 |

## 데이터 검증

데이터 무결성을 확인하려면:

```bash
# Make 명령어 사용 (권장)
make validate              # N4 데이터 검증
make validate LEVEL=N3     # 특정 레벨 검증
make validate-all          # 모든 레벨 검증

# 직접 실행
python src/main.py --validate --level N4
```

## 프로젝트 구조

```
jlpt-quiz/
├── Makefile             # Make 명령어 정의
├── PLAN.md              # 개발 계획서
├── README.md            # 사용 설명서
├── requirements.txt     # Python 의존성
├── install.sh           # 자동 설치 스크립트
├── run.py              # 실행 스크립트
├── data/               # CSV 데이터 파일
│   ├── n4_vocabulary.csv
│   └── n4_grammar.csv
├── src/                # 소스 코드
│   ├── main.py         # 메인 애플리케이션
│   ├── ui/             # 사용자 인터페이스
│   ├── data/           # 데이터 관리
│   ├── quiz/           # 퀴즈 엔진
│   └── utils/          # 유틸리티
└── progress/           # 진도 및 결과 저장
```

## 현재 상태

- ✅ 프로젝트 구조 설정
- ✅ 한국어 UI 프레임워크
- ✅ CSV 데이터 로더 (3,262개 어휘 + 2,427개 문법)
- ✅ 메인 메뉴 시스템
- ✅ 퀴즈 엔진 (문제 생성, 채점, 피드백)
- ✅ 결과 분석 (점수, 약점 분석, 학습 권장사항)
- ✅ 완전한 퀴즈 기능 (어휘, 문법, 혼합 모드)

## 다음 단계

1. 진도 저장 및 기록 시스템
2. 추가 레벨 지원 (N5, N3, N2, N1)
3. 성능 최적화
4. 웹 인터페이스 개발

## 기여

이 프로젝트에 기여하고 싶으시면 이슈를 생성하거나 풀 리퀘스트를 보내주세요.

## 라이센스

MIT License