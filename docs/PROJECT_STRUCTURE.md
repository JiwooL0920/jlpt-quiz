# 🎌 JLPT Quiz - Project Structure

## 📁 Directory Layout

```
jlpt-quiz/
├── 📄 README.md                    # Main project documentation (English)
├── 📄 PLAN.md                     # Development roadmap
├── 📄 PROJECT_STRUCTURE.md        # This file
├── 📄 Makefile                    # Build and run commands
├── 📄 requirements.txt            # Python dependencies
├── 🔧 .gitignore                  # Git ignore rules
│
├── 📊 data/                       # Quiz data (CSV files)
│   ├── n4_vocabulary.csv         # N4 vocabulary questions (3,262 items)
│   └── n4_grammar.csv            # N4 reading comprehension (999 items)
│
├── 🐍 src/                        # Source code
│   ├── main.py                   # Main application entry point
│   ├── run.py                    # Convenience runner
│   ├── demo.py                   # Quick demo script
│   │
│   ├── data/                     # Data management
│   │   ├── csv_loader.py         # CSV file loading
│   │   └── question_generator.py # Question generation logic
│   │
│   ├── quiz/                     # Quiz engine
│   │   └── quiz_engine.py        # Core quiz functionality
│   │
│   ├── ui/                       # User interface
│   │   ├── menu.py              # Main menu system
│   │   └── quiz_display.py      # Quiz display logic
│   │
│   └── utils/                    # Utilities
│       └── korean_ui.py          # Korean UI text and formatting
│
├── 📦 release/                    # Distribution files
│   ├── README.md                 # Release documentation
│   ├── JLPT-Quiz                 # Standalone macOS executable (27MB)
│   │
│   └── StreamDeck/               # Stream Deck integration
│       ├── launch-jlpt-quiz.sh   # Stream Deck launcher (recommended)
│       ├── JLPT_QUIZ.app         # macOS app bundle
│       ├── Stream_Deck_Setup.md  # Setup guide
│       └── Stream_Deck_Solutions.md # Troubleshooting
│
├── 🔧 scripts/                    # Build and utility scripts
│   └── install.sh                # Automated installation
│
├── 📝 docs/                       # Documentation
├── 📊 progress/                   # User progress storage
├── 🧪 tests/                      # Test files
└── 🐍 venv/                       # Python virtual environment
```

## 🚀 Key Files

### For Users:
- `release/JLPT-Quiz` - Ready-to-run executable
- `release/StreamDeck/launch-jlpt-quiz.sh` - Stream Deck integration
- `README.md` - How to use the application

### For Developers:
- `src/main.py` - Application entry point
- `src/data/question_generator.py` - Core question logic
- `Makefile` - Development commands
- `requirements.txt` - Dependencies

### For Distribution:
- `release/` - Complete distribution package
- All files needed to run the quiz on any macOS system

## 🎯 Clean Organization

✅ **Production ready**
✅ **Stream Deck compatible** 
✅ **Development friendly**
✅ **Distribution ready**