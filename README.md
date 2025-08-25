# JLPT Learning Quiz

A terminal-based quiz application for Japanese Language Proficiency Test (JLPT) learning.

## Key Features

- **Level Selection**: Support for N5-N1 levels (currently N4 available)
- **Study Modes**: Vocabulary and reading comprehension quizzes
- **Customization**: Question count, answer display options, hiragana display settings
- **Korean Interface**: All UI and explanations provided in Korean
- **Learning Analytics**: Score tracking and weakness analysis

## Installation and Usage

### Using Make (Recommended)
```bash
# Install
make setup

# Run
make run

# Show help
make help
```

### Automated Installation Script
```bash
./scripts/install.sh
```

### Manual Installation
1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/run.py
```

## Quick Demo

Try a quick quiz without going through the full menu system:

```bash
# After activating virtual environment
source venv/bin/activate
python src/demo.py
```

## Make Commands

| Command | Description |
|---------|-------------|
| `make setup` | Set up virtual environment and install dependencies |
| `make run` | Run the application |
| `make demo` | Quick quiz demo (3 questions) |
| `make validate` | Validate N4 data |
| `make validate-all` | Validate all level data |
| `make clean` | Clean temporary files |
| `make clean-all` | Clean everything including virtual environment |
| `make info` | Show project information |
| `make help` | Show all commands |

## Data Validation

To verify data integrity:

```bash
# Using Make commands (recommended)
make validate              # Validate N4 data
make validate LEVEL=N3     # Validate specific level
make validate-all          # Validate all levels

# Direct execution
python src/main.py --validate --level N4
```

## Project Structure

```
jlpt-quiz/
├── Makefile             # Make command definitions
├── PLAN.md              # Development plan
├── README.md            # User guide
├── requirements.txt     # Python dependencies
├── data/               # CSV data files
│   ├── n4_vocabulary.csv
│   └── n4_grammar.csv
├── scripts/            # Scripts
│   └── install.sh      # Automated installation script
├── src/                # Source code
│   ├── main.py         # Main application
│   ├── run.py          # Execution script
│   ├── demo.py         # Quiz demo
│   ├── ui/             # User interface
│   ├── data/           # Data management
│   ├── quiz/           # Quiz engine
│   └── utils/          # Utilities
├── tests/              # Test files
└── progress/           # Progress and results storage
```

## Current Status

- ✅ Project structure setup
- ✅ Korean UI framework
- ✅ CSV data loader (3,262 vocabulary + 2,427 grammar items)
- ✅ Main menu system
- ✅ Quiz engine (question generation, scoring, feedback)
- ✅ Results analysis (scoring, weakness analysis, study recommendations)
- ✅ Complete quiz functionality (vocabulary, reading comprehension modes)
- ✅ Clean file structure and cache management

## Next Steps

1. Progress saving and tracking system
2. Additional level support (N5, N3, N2, N1)
3. Performance optimization
4. Web interface development

## Contributing

If you'd like to contribute to this project, please create an issue or submit a pull request.

## License

MIT License