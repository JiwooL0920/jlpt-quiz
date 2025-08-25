# JLPT Quiz Application Development Plan

## Executive Summary
Development of a comprehensive terminal-based quiz application for JLPT (Japanese Language Proficiency Test) study. The application will feature vocabulary and grammar sections with multiple difficulty levels (N5-N1), customizable quiz options, Korean language support, and comprehensive scoring analytics.

## Project Overview

### Objectives
1. Create a terminal-based quiz application for JLPT study (initially N4, expandable to N5-N1)
2. Provide separate vocabulary and grammar quiz modes
3. Support customizable quiz lengths (25, 50, 100, all questions)
4. Offer immediate or deferred answer feedback
5. Include optional hiragana display for kanji
6. Provide Korean translations for questions and answers
7. Generate comprehensive performance analytics

### Key Features
- **Level Selection**: N5-N1 support (starting with N4)
- **Study Modes**: Vocabulary and Grammar sections
- **Quiz Customization**: Variable question counts, feedback modes, hiragana display
- **Korean Language Support**: All interface, questions, and explanations in Korean
- **Comprehensive Analytics**: Score tracking, weak area identification, progress monitoring
- **CSV-based Questions**: Easy content management and updates

## JLPT Structure Reference

### JLPT Levels
- **N5**: Basic level (800 vocabulary, basic grammar)
- **N4**: Elementary level (1,500 vocabulary, elementary grammar) - **INITIAL FOCUS**
- **N3**: Intermediate level (3,750 vocabulary, intermediate grammar)
- **N2**: Upper-intermediate level (6,000 vocabulary, advanced grammar)  
- **N1**: Advanced level (10,000 vocabulary, expert grammar)

### Current Data Structure
#### Vocabulary CSV (n4_vocabulary.csv)
- `kanji`: Japanese kanji form
- `hiragana`: Hiragana reading
- `pos`: Part of speech
- `korean_meaning`: Korean translation
- `question_type`: reading/meaning_to_japanese/japanese_to_meaning
- `difficulty`: Difficulty level (1-3)

#### Grammar CSV (n4_grammar.csv)
- `grammar_pattern`: Grammar pattern being tested
- `japanese_sentence`: Example sentence in Japanese
- `hiragana_reading`: Full hiragana reading
- `korean_translation`: Korean translation
- `question_type`: sentence_completion/meaning_comprehension
- `difficulty`: Difficulty level (1-3)
- `file_source`: Source file reference

## Technical Architecture

### Technology Stack
- **Language**: Python 3.9+
- **UI Framework**: Rich (for terminal UI with Korean font support)
- **Data Storage**: CSV files for questions, JSON for progress tracking
- **Testing**: pytest
- **Internationalization**: Korean language interface

### Project Structure
```
jlpt-quiz/
├── docs/
│   ├── PLAN.md
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── quiz/
│   │   ├── __init__.py
│   │   ├── quiz_engine.py
│   │   ├── vocabulary_quiz.py
│   │   ├── grammar_quiz.py
│   │   └── score_tracker.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── menu.py
│   │   ├── quiz_display.py
│   │   └── results_display.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── csv_loader.py
│   │   ├── question_generator.py
│   │   └── progress_manager.py
│   └── utils/
│       ├── __init__.py
│       ├── korean_ui.py
│       └── validators.py
├── data/
│   ├── n4_vocabulary.csv
│   ├── n4_grammar.csv
│   └── (future: n5_vocabulary.csv, n3_vocabulary.csv, etc.)
├── progress/
│   ├── quiz_history.json
│   └── user_progress.json
├── tests/
│   └── test_*.py
├── requirements.txt
└── README.md
```

## Question Generation System

### Vocabulary Question Types
1. **Reading Questions**: Show kanji → select hiragana
2. **Meaning to Japanese**: Show Korean meaning → select kanji/hiragana
3. **Japanese to Meaning**: Show kanji/hiragana → select Korean meaning

### Grammar Question Types
1. **Sentence Completion**: Fill in missing grammar pattern
2. **Meaning Comprehension**: Choose correct Korean translation
3. **Pattern Recognition**: Identify correct grammar usage

### Question Structure
```python
{
    "id": "unique_id",
    "type": "vocabulary|grammar",
    "level": "N4",
    "category": "reading|meaning_to_japanese|japanese_to_meaning|sentence_completion|meaning_comprehension",
    "difficulty": 1|2|3,
    "kanji": "愛",
    "hiragana": "あい",
    "korean_meaning": "사랑",
    "question_text": "다음 한자의 올바른 읽기를 선택하세요:",
    "options": ["あい", "こい", "めい", "らい"],
    "correct_answer": "あい",
    "explanation": "愛(あい)는 '사랑'을 의미합니다.",
    "show_hiragana": True|False
}
```

## User Experience Flow

### Main Menu (Korean Interface)
```
╔════════════════════════════════════════╗
║           JLPT 학습 퀴즈              ║
╠════════════════════════════════════════╣
║ 1. 레벨 선택 (N5-N1)                   ║
║ 2. 이전 결과 보기                      ║
║ 3. 설정                               ║
║ 4. 종료                               ║
╚════════════════════════════════════════╝
```

### Level Selection
```
╔════════════════════════════════════════╗
║            레벨 선택                   ║
╠════════════════════════════════════════╣
║ 1. N5 (기초)           [준비중]        ║
║ 2. N4 (초급)           [사용가능]      ║
║ 3. N3 (중급)           [준비중]        ║
║ 4. N2 (중상급)         [준비중]        ║
║ 5. N1 (상급)           [준비중]        ║
║ 6. 메인메뉴로                          ║
╚════════════════════════════════════════╝
```

### Study Mode Selection (N4)
```
╔════════════════════════════════════════╗
║            N4 학습 선택                ║
╠════════════════════════════════════════╣
║ 1. 어휘 (단어) 퀴즈                    ║
║ 2. 문법 퀴즈                          ║
║ 3. 혼합 퀴즈                          ║
║ 4. 뒤로                               ║
╚════════════════════════════════════════╝
```

### Quiz Configuration
```
╔════════════════════════════════════════╗
║            퀴즈 설정                   ║
╠════════════════════════════════════════╣
║ 문제 수:                              ║
║ 1. 25문제    2. 50문제                 ║
║ 3. 100문제   4. 전체                   ║
║                                       ║
║ 답안 표시:                            ║
║ 1. 즉시 표시 (문제마다)                ║
║ 2. 마지막에 표시 (전체 완료 후)         ║
║                                       ║
║ 히라가나 표시:                         ║
║ 1. 한자만    2. 한자+히라가나           ║
╚════════════════════════════════════════╝
```

### Question Display Example (Vocabulary)
```
╔════════════════════════════════════════╗
║ 문제 1/25 | 어휘 | N4                  ║
╠════════════════════════════════════════╣
║ 다음 한자의 올바른 읽기를 선택하세요:    ║
║                                       ║
║        愛                             ║
║      (あい)  ← 히라가나 표시 옵션       ║
║                                       ║
║ 1. あい      2. こい                   ║
║ 3. めい      4. らい                   ║
╚════════════════════════════════════════╝
```

### Immediate Feedback Display
```
╔════════════════════════════════════════╗
║              ✓ 정답                   ║
╠════════════════════════════════════════╣
║ 선택한 답: 1. あい                     ║
║ 정답: 1. あい                          ║
║                                       ║
║ 해설:                                 ║
║ 愛(あい)는 '사랑'을 의미하는 명사입니다. ║
║ 일상생활에서 자주 사용되는 단어입니다.   ║
║                                       ║
║ [Enter] 다음 문제                      ║
╚════════════════════════════════════════╝
```

## Implementation Phases

### Phase 1: Foundation (Week 1)
- [x] Research JLPT structure and existing data
- [x] Analyze CKAD quiz architecture patterns
- [ ] Set up project structure
- [ ] Implement Korean UI framework with Rich
- [ ] Create CSV data loader

### Phase 2: Core Quiz Engine (Week 2)
- [ ] Implement vocabulary quiz engine
- [ ] Implement grammar quiz engine
- [ ] Add question randomization
- [ ] Create answer validation system
- [ ] Implement scoring system

### Phase 3: User Interface (Week 3)
- [ ] Design Korean main menu system
- [ ] Implement level selection
- [ ] Add quiz configuration options
- [ ] Create question display system
- [ ] Implement feedback modes (immediate/deferred)

### Phase 4: Advanced Features (Week 4)
- [ ] Add hiragana display toggle
- [ ] Implement comprehensive analytics
- [ ] Create progress tracking
- [ ] Add weak area identification
- [ ] Implement quiz history

### Phase 5: Testing & Polish (Week 5)
- [ ] Unit testing
- [ ] Integration testing
- [ ] Korean font and display optimization
- [ ] Performance optimization
- [ ] User acceptance testing

### Phase 6: Future Expansion (Week 6+)
- [ ] Add N5, N3, N2, N1 level support
- [ ] Implement SRS (Spaced Repetition System)
- [ ] Add audio pronunciation support
- [ ] Create web interface option

## Key Components

### 1. CSV Data Loader
```python
class CSVLoader:
    - load_vocabulary(level: str)
    - load_grammar(level: str)
    - validate_data()
    - get_question_count()
```

### 2. Question Generator
```python
class QuestionGenerator:
    - generate_vocabulary_question()
    - generate_grammar_question()
    - create_multiple_choice()
    - randomize_options()
```

### 3. Quiz Engine
```python
class QuizEngine:
    - start_quiz(mode, level, count, feedback, hiragana)
    - load_questions()
    - track_answers()
    - calculate_score()
    - identify_weak_areas()
```

### 4. Korean UI Manager
```python
class KoreanUIManager:
    - display_korean_menu()
    - show_question_korean()
    - display_feedback_korean()
    - show_results_korean()
    - format_korean_text()
```

## Scoring & Analytics

### Score Calculation
- **Overall Score**: Percentage of correct answers
- **Category Scores**: Vocabulary vs Grammar performance
- **Difficulty Analysis**: Performance by difficulty level (1-3)
- **Question Type Analysis**: Reading vs Meaning comprehension
- **Time Analysis**: Average time per question

### Weakness Identification
```python
def identify_weak_areas(results):
    weak_areas = []
    
    # Vocabulary weak areas
    vocab_score = calculate_vocabulary_score(results)
    if vocab_score < 70:
        weak_areas.append({
            'area': '어휘 (단어)',
            'score': vocab_score,
            'recommendations': ['기본 단어 복습', 'N4 어휘집 학습']
        })
    
    # Grammar weak areas
    grammar_score = calculate_grammar_score(results)
    if grammar_score < 70:
        weak_areas.append({
            'area': '문법',
            'score': grammar_score,
            'recommendations': ['기본 문법 패턴 복습', 'N4 문법서 학습']
        })
    
    return weak_areas
```

### Results Report (Korean)
```
╔════════════════════════════════════════╗
║              퀴즈 결과                 ║
╠════════════════════════════════════════╣
║ 전체 점수: 78%                         ║
║ 정답: 39/50 문제                       ║
║ 소요시간: 25분                         ║
╠════════════════════════════════════════╣
║ 분야별 점수:                           ║
║ • 어휘 (단어): 85%                     ║
║ • 문법: 72%                           ║
╠════════════════════════════════════════╣
║ 개선이 필요한 분야:                     ║
║ • てしまう 문법 (60%)                  ║
║ • 동사 활용 (65%)                      ║
║ • 형용사 변화 (68%)                    ║
╠════════════════════════════════════════╣
║ 학습 권장사항:                         ║
║ • N4 문법 패턴 집중 학습                ║
║ • 동사 활용 연습 강화                   ║
║ • 일상 어휘 확장                       ║
╚════════════════════════════════════════╝
```

## Data Management

### Question Database Expansion Plan
```
Current: n4_vocabulary.csv, n4_grammar.csv
Future:
├── vocabulary/
│   ├── n5_vocabulary.csv (~800 entries)
│   ├── n4_vocabulary.csv (~1500 entries) ✓
│   ├── n3_vocabulary.csv (~3750 entries)
│   ├── n2_vocabulary.csv (~6000 entries)
│   └── n1_vocabulary.csv (~10000 entries)
└── grammar/
    ├── n5_grammar.csv (~basic patterns)
    ├── n4_grammar.csv (~elementary patterns) ✓
    ├── n3_grammar.csv (~intermediate patterns)
    ├── n2_grammar.csv (~advanced patterns)
    └── n1_grammar.csv (~expert patterns)
```

### Progress Tracking
```json
{
    "user_id": "default_user",
    "current_level": "N4",
    "total_quizzes": 15,
    "total_questions": 750,
    "correct_answers": 580,
    "overall_accuracy": 77.3,
    "level_progress": {
        "N4": {
            "vocabulary_accuracy": 82.5,
            "grammar_accuracy": 71.2,
            "weak_areas": ["てしまう", "passive_form"],
            "strong_areas": ["basic_adjectives", "time_expressions"]
        }
    },
    "last_quiz_date": "2025-08-25",
    "study_streak": 7
}
```

## Korean Language Implementation

### UI Text Constants
```python
UI_TEXT = {
    'main_menu': {
        'title': 'JLPT 학습 퀴즈',
        'level_select': '레벨 선택 (N5-N1)',
        'previous_results': '이전 결과 보기',
        'settings': '설정',
        'exit': '종료'
    },
    'quiz_config': {
        'question_count': '문제 수:',
        'feedback_mode': '답안 표시:',
        'hiragana_display': '히라가나 표시:',
        'immediate': '즉시 표시',
        'deferred': '마지막에 표시'
    },
    'results': {
        'correct': '정답',
        'incorrect': '오답',
        'score': '점수',
        'time': '소요시간',
        'weak_areas': '개선이 필요한 분야'
    }
}
```

### Font and Display Considerations
- Ensure proper Korean character rendering in terminal
- Use Rich library with Korean-compatible fonts
- Test on various terminal environments
- Provide fallback for systems without Korean font support

## Success Metrics

### Quantitative Metrics
- Support for complete N4 vocabulary and grammar (initial release)
- >90% question accuracy and Korean translation quality
- <200ms response time for question loading
- Support for 25/50/100/all question configurations

### Qualitative Metrics
- Intuitive Korean user interface
- Clear and helpful Korean explanations
- Accurate weak area identification
- Effective learning progression tracking

## Risk Mitigation

### Technical Risks
- **Korean font rendering**: Test across different terminals, provide documentation
- **CSV data integrity**: Implement validation and error handling
- **Performance with large datasets**: Optimize loading and caching

### Content Risks
- **Translation accuracy**: Review Korean translations with native speakers
- **JLPT alignment**: Ensure questions align with official JLPT standards
- **Difficulty balancing**: Test and adjust difficulty levels based on user feedback

## Future Roadmap

### Phase 2 Expansion (3-6 months)
- Add N5 and N3 levels
- Implement spaced repetition system
- Add audio pronunciation features
- Create mobile-friendly web interface

### Phase 3 Enhancement (6-12 months)
- Complete N2 and N1 levels
- Add reading comprehension sections
- Implement adaptive difficulty
- Community features and shared progress

## Conclusion

This comprehensive plan outlines the development of a robust JLPT study application specifically designed for Korean speakers. The application will provide an effective learning tool through customizable quizzes, immediate feedback, and detailed analytics to track progress and identify areas for improvement.

The modular architecture ensures easy expansion to additional JLPT levels, while the focus on Korean language support ensures accessibility for the target audience. The CSV-based data structure allows for easy content management and updates as the question database grows.