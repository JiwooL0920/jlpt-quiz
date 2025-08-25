#!/bin/bash
# JLPT Quiz Installation Script

echo "🎌 JLPT 학습 퀴즈 설치를 시작합니다..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3가 필요합니다. Python 3를 먼저 설치해주세요."
    exit 1
fi

# Create virtual environment
echo "📦 가상환경을 생성합니다..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 가상환경을 활성화합니다..."
source venv/bin/activate

# Install dependencies
echo "📚 필요한 패키지를 설치합니다..."
pip install -r requirements.txt

# Validate data
echo "✅ 데이터 무결성을 확인합니다..."
python src/main.py --validate --level N4

echo ""
echo "🎉 설치가 완료되었습니다!"
echo ""
echo "실행하려면 다음 명령어를 사용하세요:"
echo "  source venv/bin/activate && python run.py"
echo ""
echo "또는 가상환경을 활성화한 후:"
echo "  source venv/bin/activate"
echo "  python run.py"