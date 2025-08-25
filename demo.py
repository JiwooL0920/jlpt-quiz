#!/usr/bin/env python3
"""
Demo script to show JLPT Quiz functionality
Run this to see a quick demo without going through the full menu system
"""

import sys
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from rich.console import Console
from src.quiz.quiz_engine import QuizEngine
from src.ui.quiz_display import QuizDisplay

console = Console()

def demo_quiz():
    """Run a quick demo quiz"""
    console.clear()
    
    console.print("[bold cyan]🎌 JLPT 퀴즈 데모[/bold cyan]\n")
    console.print("N4 어휘 문제 3개를 풀어보세요!")
    console.print("(실제 앱에서는 메뉴에서 모든 설정을 할 수 있습니다)\n")
    
    input("[Enter]를 눌러 시작...")
    
    # Initialize quiz components
    quiz_engine = QuizEngine()
    quiz_display = QuizDisplay(console)
    
    # Prepare a small demo quiz
    success = quiz_engine.prepare_quiz(
        level='N4',
        mode='vocabulary',
        question_count=3,
        feedback_mode='immediate',
        show_hiragana=True
    )
    
    if not success:
        console.print("[red]데모 퀴즈 준비 실패[/red]")
        return
    
    # Start quiz
    quiz_engine.start_quiz()
    
    # Quiz loop
    while not quiz_engine.is_quiz_finished():
        # Get current question
        question = quiz_engine.get_current_question()
        if not question:
            break
        
        # Show question and get answer
        answer_index = quiz_display.show_question(question)
        
        # Handle quit signal
        if answer_index == -1:
            console.print("[yellow]데모 종료[/yellow]")
            return
        
        # Submit answer
        feedback = quiz_engine.submit_answer(answer_index)
        
        # Show immediate feedback
        continue_quiz = quiz_display.show_immediate_feedback(feedback)
        if not continue_quiz:
            console.print("[yellow]데모 종료[/yellow]")
            return
        
        # Move to next question
        quiz_engine.next_question()
    
    # Show final results
    results = quiz_engine.get_quiz_results()
    quiz_display.show_quiz_results(results)
    
    console.print("\n[bold cyan]데모 완료![/bold cyan]")
    console.print("전체 앱을 사용하려면 'python run.py' 또는 'make run'을 실행하세요.")

if __name__ == "__main__":
    try:
        demo_quiz()
    except KeyboardInterrupt:
        console.print("\n[yellow]데모가 중단되었습니다.[/yellow]")
    except Exception as e:
        console.print(f"\n[red]오류: {str(e)}[/red]")