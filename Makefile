# JLPT Quiz Application Makefile
.PHONY: help setup run demo clean validate test install dev-install

# Default target
help: ## Show this help message
	@echo "🎌 JLPT 학습 퀴즈 - Make Commands"
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""

setup: ## 🔧 Setup virtual environment and install dependencies
	@echo "🎌 JLPT 학습 퀴즈 설치를 시작합니다..."
	@if ! command -v python3 >/dev/null 2>&1; then \
		echo "❌ Python 3가 필요합니다. Python 3를 먼저 설치해주세요."; \
		exit 1; \
	fi
	@echo "📦 가상환경을 생성합니다..."
	python3 -m venv venv
	@echo "📚 필요한 패키지를 설치합니다..."
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	@echo "✅ 데이터 무결성을 확인합니다..."
	venv/bin/python src/main.py --validate --level N4
	@echo ""
	@echo "🎉 설치가 완료되었습니다!"
	@echo "실행하려면: make run"

run: ## 🚀 Run the JLPT quiz application
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make setup'을 먼저 실행하세요."; \
		exit 1; \
	fi
	@echo "🎌 JLPT 학습 퀴즈를 시작합니다..."
	venv/bin/python src/run.py

demo: ## 🎯 Run a quick quiz demo (3 vocabulary questions)
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make setup'을 먼저 실행하세요."; \
		exit 1; \
	fi
	@echo "🎌 JLPT 퀴즈 데모를 시작합니다..."
	venv/bin/python src/demo.py

validate: ## ✅ Validate data integrity for specified level (default: N4)
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make setup'을 먼저 실행하세요."; \
		exit 1; \
	fi
	venv/bin/python src/main.py --validate --level $(or $(LEVEL),N4)

validate-all: ## ✅ Validate all available data levels
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make setup'을 먼저 실행하세요."; \
		exit 1; \
	fi
	@for level in N5 N4 N3 N2 N1; do \
		echo "검사 중: $$level"; \
		venv/bin/python src/main.py --validate --level $$level 2>/dev/null || true; \
		echo ""; \
	done

test: ## 🧪 Run tests (when implemented)
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make setup'을 먼저 실행하세요."; \
		exit 1; \
	fi
	@echo "🧪 테스트를 실행합니다..."
	venv/bin/python -m pytest tests/ -v || echo "⚠️  테스트가 아직 구현되지 않았습니다."

dev-install: ## 🔧 Install development dependencies
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make setup'을 먼저 실행하세요."; \
		exit 1; \
	fi
	@echo "🛠️  개발 의존성을 설치합니다..."
	venv/bin/pip install black flake8 mypy
	@echo "✅ 개발 도구가 설치되었습니다."

format: ## 🎨 Format code with black
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make dev-install'을 먼저 실행하세요."; \
		exit 1; \
	fi
	@echo "🎨 코드를 포맷팅합니다..."
	venv/bin/black src/ --line-length 88
	@echo "✅ 코드 포맷팅이 완료되었습니다."

lint: ## 🔍 Run code linting
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make dev-install'을 먼저 실행하세요."; \
		exit 1; \
	fi
	@echo "🔍 코드 린팅을 실행합니다..."
	venv/bin/flake8 src/ --max-line-length=88 --exclude=venv
	@echo "✅ 린팅이 완료되었습니다."

type-check: ## 🔍 Run type checking with mypy
	@if [ ! -d "venv" ]; then \
		echo "❌ 가상환경이 설정되지 않았습니다. 'make dev-install'을 먼저 실행하세요."; \
		exit 1; \
	fi
	@echo "🔍 타입 체킹을 실행합니다..."
	venv/bin/mypy src/ --ignore-missing-imports
	@echo "✅ 타입 체킹이 완료되었습니다."

clean: ## 🧹 Clean up generated files
	@echo "🧹 정리를 시작합니다..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache
	@echo "✅ 정리가 완료되었습니다."

clean-all: clean ## 🧹 Clean up everything including virtual environment
	@echo "🗑️  가상환경을 삭제합니다..."
	rm -rf venv
	@echo "✅ 모든 정리가 완료되었습니다."

install: setup ## 🔧 Alias for setup
	@echo "✅ 설치 완료!"

info: ## ℹ️  Show project information
	@echo "🎌 JLPT 학습 퀴즈 v1.0.0"
	@echo ""
	@echo "프로젝트 정보:"
	@echo "  - 언어: Python 3.9+"
	@echo "  - UI: Rich (터미널 기반)"
	@echo "  - 데이터: CSV 파일"
	@echo "  - 현재 지원 레벨: N4"
	@echo ""
	@if [ -d "venv" ]; then \
		echo "상태: ✅ 설치됨"; \
		echo "Python: $$(venv/bin/python --version)"; \
		echo "패키지: $$(venv/bin/pip list | wc -l) 개 설치됨"; \
	else \
		echo "상태: ❌ 미설치 (make setup 실행 필요)"; \
	fi
	@echo ""
	@if [ -f "data/n4_vocabulary.csv" ] && [ -f "data/n4_grammar.csv" ]; then \
		echo "데이터 파일:"; \
		echo "  - N4 어휘: $$(tail -n +2 data/n4_vocabulary.csv | wc -l | tr -d ' ') 개"; \
		echo "  - N4 문법: $$(tail -n +2 data/n4_grammar.csv | wc -l | tr -d ' ') 개"; \
	fi

# Show help by default
.DEFAULT_GOAL := help