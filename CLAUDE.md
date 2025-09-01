# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a terminal-based Japanese Language Proficiency Test (JLPT) quiz application with a Korean UI. The application provides vocabulary and reading comprehension quizzes for JLPT preparation, currently supporting N4 level with plans for N5-N1 levels.

## Development Commands

### Setup and Execution
```bash
# Setup virtual environment and install dependencies
make setup

# Run the main application
make run

# Run quick demo (3 vocabulary questions)
make demo
```

### Development Workflow
```bash
# Install development dependencies (black, flake8, mypy)
make dev-install

# Format code
make format

# Run linting
make lint

# Type checking
make type-check

# Run tests (when implemented)
make test
```

### Data Validation
```bash
# Validate N4 data (default)
make validate

# Validate specific level
make validate LEVEL=N3

# Validate all levels
make validate-all

# Direct validation command
python src/main.py --validate --level N4
```

### Cleaning
```bash
# Clean generated files (__pycache__, .pyc files)
make clean

# Clean everything including virtual environment
make clean-all
```

## Architecture and Code Organization

### Core Architecture Pattern
The application follows a layered architecture with clear separation of concerns:

- **UI Layer** (`src/ui/`): Korean-language terminal interface using Rich library
- **Quiz Engine** (`src/quiz/`): Quiz logic, scoring, and flow management
- **Data Layer** (`src/data/`): CSV data loading and question generation
- **Utils** (`src/utils/`): Korean UI text management and shared utilities

### Key Components

**Main Entry Points:**
- `src/main.py` - Primary CLI with click commands and data validation
- `src/run.py` - Convenience runner script
- `src/demo.py` - Quick demo mode without full menu navigation

**Core Classes:**
- `QuizEngine` - Central quiz management, coordinates question flow and scoring
- `QuestionGenerator` - Creates quiz questions from CSV data with pattern hiding for grammar questions
- `CSVLoader` - Handles data loading with caching and validation
- `MainMenu` - Terminal UI menu system with Korean text
- `QuizDisplay` - Rich-based question presentation and feedback

### Data Flow
1. **Data Loading**: CSVLoader reads N4 vocabulary/grammar CSV files with pandas
2. **Question Generation**: QuestionGenerator creates quiz questions, handles hiragana hiding for grammar patterns
3. **Quiz Execution**: QuizEngine manages question flow, answer validation, and scoring
4. **UI Presentation**: QuizDisplay renders questions using Rich tables and panels
5. **Results Analysis**: Score calculation and weakness identification

### Korean UI System
The application uses a centralized Korean text system (`src/utils/korean_ui.py`) with UI_TEXT dictionary containing all Korean interface strings. Use `get_text(section, key)` for consistent Korean text retrieval.

### Data Validation
Comprehensive data integrity checking is built into CSVLoader:
- Required column validation for vocabulary and grammar data
- Data type checking and missing value detection
- Validation commands available through CLI and Make targets

## Current Implementation Status

**Completed:**
- ✅ Full N4 vocabulary and grammar quiz system
- ✅ Korean UI with Rich library styling and ASCII art landing page
- ✅ Question generation with hiragana hiding for grammar patterns  
- ✅ Bidirectional reading comprehension (Japanese↔Korean) with randomization
- ✅ Score tracking and results analysis with complete option translations
- ✅ Data validation and integrity checking
- ✅ Make-based development workflow
- ✅ Persistent settings system (level, hiragana display, feedback mode)
- ✅ Simplified navigation with proper back/forth functionality
- ✅ Question randomization for all quiz modes

**In Progress:**
- Progress saving and session management
- Additional JLPT levels (N5, N3, N2, N1)
- Test suite implementation

## Dependencies

Core dependencies managed in `requirements.txt`:
- `rich>=13.0.0` - Terminal UI and styling
- `click>=8.0.0` - CLI interface
- `pandas>=2.0.0` - CSV data processing  
- `pytest>=7.0.0` - Testing framework

Development tools installed via `make dev-install`:
- `black` - Code formatting
- `flake8` - Linting  
- `mypy` - Type checking

## Testing Notes

The project uses pytest but tests are not yet implemented. The current `make test` command will show a warning about missing tests. When implementing tests, follow the existing pattern and place test files in the `tests/` directory.