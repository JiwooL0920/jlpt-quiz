"""Korean UI text constants and utilities for JLPT Quiz Application"""

# Korean UI Text Constants
UI_TEXT = {
    'main_menu': {
        'title': 'JLPT 학습 퀴즈',
        'subtitle': '일본어 능력시험 학습 도구',
        'level_select': '레벨 선택 (N5-N1) | Level Selection',
        'previous_results': '이전 결과 보기 | Previous Results',
        'settings': '설정 | Settings',
        'exit': '종료 | Exit'
    },
    
    'level_menu': {
        'title': '레벨 선택',
        'n5': 'N5 (기초)',
        'n4': 'N4 (초급)', 
        'n3': 'N3 (중급)',
        'n2': 'N2 (중상급)',
        'n1': 'N1 (상급)',
        'available': '사용가능',
        'coming_soon': '준비중',
        'back': '뒤로'
    },
    
    'study_mode': {
        'title': '학습 선택',
        'vocabulary': '어휘 (단어) 퀴즈 | Vocabulary Quiz',
        'grammar': '독해 퀴즈 | Reading Comprehension Quiz', 
        'mixed': '혼합 퀴즈 | Mixed Quiz',
        'back': '뒤로 | Back'
    },
    
    'quiz_config': {
        'title': '퀴즈 설정',
        'question_count': '문제 수: | Question Count:',
        'questions_25': '25문제 | 25 Questions',
        'questions_50': '50문제 | 50 Questions', 
        'questions_100': '100문제 | 100 Questions',
        'questions_all': '전체 | All',
        'feedback_mode': '답안 표시: | Answer Display:',
        'immediate': '즉시 표시 (문제마다) | Immediate (after each)',
        'deferred': '마지막에 표시 (전체 완료 후) | At the end (after all)',
        'hiragana_display': '히라가나 표시: | Hiragana Display:',
        'kanji_only': '한자만 | Kanji Only',
        'kanji_hiragana': '한자+히라가나 | Kanji + Hiragana',
        'start_quiz': '퀴즈 시작 | Start Quiz',
        'cancel': '취소 | Cancel'
    },
    
    'question': {
        'question_format': '문제 {current}/{total} | {type} | {level}',
        'vocabulary_prompt': '다음 단어의 올바른 답을 선택하세요:',
        'grammar_prompt': '다음 문장의 올바른 답을 선택하세요:',
        'reading_prompt': '다음 한자의 올바른 읽기를 선택하세요:',
        'meaning_prompt': '다음 뜻에 해당하는 일본어를 선택하세요:',
        'translation_prompt': '다음 일본어의 한국어 뜻을 선택하세요:'
    },
    
    'feedback': {
        'correct': '✓ 정답',
        'incorrect': '✗ 오답',
        'your_answer': '선택한 답:',
        'correct_answer': '정답:',
        'explanation': '해설:',
        'continue': '[Enter] 다음 문제',
        'finish': '[Enter] 결과 보기'
    },
    
    'results': {
        'title': '퀴즈 결과',
        'overall_score': '전체 점수:',
        'correct_answers': '정답:',
        'total_time': '소요시간:',
        'category_breakdown': '분야별 점수:',
        'vocabulary': '어휘 (단어):',
        'grammar': '독해:',
        'weak_areas': '개선이 필요한 분야:',
        'recommendations': '학습 권장사항:',
        'excellent': '우수',
        'good': '양호', 
        'needs_improvement': '개선 필요',
        'continue': '[Enter] 메뉴로 돌아가기'
    },
    
    'settings': {
        'title': '설정',
        'clear_history': '퀴즈 기록 삭제',
        'export_results': '결과 내보내기',
        'about': '정보',
        'back': '뒤로',
        'confirm_clear': '정말로 퀴즈 기록을 삭제하시겠습니까?',
        'history_cleared': '퀴즈 기록이 삭제되었습니다.',
        'results_exported': '결과가 내보내기되었습니다:'
    },
    
    'common': {
        'yes': '예',
        'no': '아니오',
        'minutes': '분',
        'seconds': '초',
        'percent': '%',
        'loading': '로딩중...',
        'error': '오류',
        'success': '성공',
        'cancel': '취소',
        'confirm': '확인'
    }
}

def get_text(category: str, key: str) -> str:
    """Get Korean text for UI elements"""
    try:
        return UI_TEXT[category][key]
    except KeyError:
        return f"[Missing text: {category}.{key}]"

def format_score(score: float) -> str:
    """Format score with Korean percentage"""
    return f"{score:.0f}%"

def format_time(seconds: int) -> str:
    """Format time in Korean"""
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    
    if minutes > 0:
        return f"{minutes}분 {remaining_seconds}초"
    else:
        return f"{remaining_seconds}초"

def get_grade_text(score: float) -> tuple[str, str]:
    """Get grade text and color based on score"""
    if score >= 90:
        return get_text('results', 'excellent'), 'green'
    elif score >= 70:
        return get_text('results', 'good'), 'yellow'
    else:
        return get_text('results', 'needs_improvement'), 'red'