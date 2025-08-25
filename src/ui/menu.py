"""Main menu system for JLPT Quiz Application"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Confirm
from rich.table import Table
from rich.text import Text
from typing import Optional
import sys

from ..utils.korean_ui import UI_TEXT, get_text
from ..data.csv_loader import CSVLoader
from ..quiz.quiz_engine import QuizEngine
from .quiz_display import QuizDisplay

class MainMenu:
    """Main menu controller for JLPT Quiz Application"""
    
    def __init__(self, console: Console):
        self.console = console
        self.csv_loader = CSVLoader()
        self.quiz_engine = QuizEngine()
        self.quiz_display = QuizDisplay(console)
        
    def run(self):
        """Run the main menu loop"""
        while True:
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 1:
                self.level_selection()
            elif choice == 2:
                self.show_previous_results()
            elif choice == 3:
                self.show_settings()
            elif choice == 4:
                self.console.print(f"[yellow]{get_text('common', 'success')}! 다음에 또 만나요![/yellow]")
                break
    
    def display_main_menu(self):
        """Display the main menu"""
        self.console.clear()
        
        # Create menu content
        content = f"""[bold cyan]{get_text('main_menu', 'title')}[/bold cyan]
[dim]{get_text('main_menu', 'subtitle')}[/dim]

[1] {get_text('main_menu', 'level_select')}
[2] {get_text('main_menu', 'previous_results')}
[3] {get_text('main_menu', 'settings')}
[4] {get_text('main_menu', 'exit')}"""
        
        self.console.print(Panel(content, border_style="cyan"))
    
    def get_menu_choice(self) -> int:
        """Get user menu choice"""
        try:
            choice = IntPrompt.ask(
                f"\n[cyan]선택하세요[/cyan]", 
                choices=["1", "2", "3", "4"]
            )
            return choice
        except KeyboardInterrupt:
            self.console.print(f"\n[yellow]종료합니다...[/yellow]")
            sys.exit(0)
    
    def level_selection(self):
        """Display level selection menu"""
        self.console.clear()
        
        # Get available levels
        available_levels = self.csv_loader.get_available_levels()
        
        # Create level menu content
        levels_info = [
            ("1", "N5", get_text('level_menu', 'n5'), "N5" in available_levels),
            ("2", "N4", get_text('level_menu', 'n4'), "N4" in available_levels),
            ("3", "N3", get_text('level_menu', 'n3'), "N3" in available_levels),
            ("4", "N2", get_text('level_menu', 'n2'), "N2" in available_levels),
            ("5", "N1", get_text('level_menu', 'n1'), "N1" in available_levels),
        ]
        
        content_lines = [""]
        for num, level_code, level_desc, is_available in levels_info:
            status = get_text('level_menu', 'available') if is_available else get_text('level_menu', 'coming_soon')
            color = "green" if is_available else "dim"
            content_lines.append(f"[{num}] {level_desc} [{color}][{status}][/{color}]")
        
        content_lines.extend(["", f"[6] {get_text('level_menu', 'back')}"])
        content = "\n".join(content_lines)
        
        self.console.print(Panel(
            content, 
            title=f"[bold]{get_text('level_menu', 'title')}[/bold]", 
            border_style="cyan"
        ))
        
        try:
            choice = IntPrompt.ask("선택하세요", choices=["1", "2", "3", "4", "5", "6"])
            
            if choice == 6:
                return  # Back to main menu
            
            level_code = ["N5", "N4", "N3", "N2", "N1"][choice - 1]
            
            if level_code in available_levels:
                self.study_mode_selection(level_code)
            else:
                self.console.print(f"[yellow]{level_code}는 아직 준비중입니다.[/yellow]")
                self.console.input("\n[Enter]를 눌러 계속...")
                
        except KeyboardInterrupt:
            return
    
    def study_mode_selection(self, level: str):
        """Display study mode selection for chosen level"""
        self.console.clear()
        
        # Get data counts
        vocab_count = self.csv_loader.get_vocabulary_count(level)
        grammar_count = self.csv_loader.get_grammar_count(level)
        
        # Create study mode content
        content = f"""
[1] {get_text('study_mode', 'vocabulary')} ({vocab_count}개)
[2] {get_text('study_mode', 'grammar')} ({grammar_count}개)  
[3] {get_text('study_mode', 'mixed')} ({vocab_count + grammar_count}개)

[4] {get_text('study_mode', 'back')}
        """
        
        self.console.print(Panel(
            content.strip(),
            title=f"[bold]{level} {get_text('study_mode', 'title')}[/bold]",
            border_style="cyan"
        ))
        
        try:
            choice = IntPrompt.ask("선택하세요", choices=["1", "2", "3", "4"])
            
            if choice == 4:
                return  # Back to level selection
            
            mode = ["vocabulary", "grammar", "mixed"][choice - 1]
            self.quiz_configuration(level, mode)
            
        except KeyboardInterrupt:
            return
    
    def quiz_configuration(self, level: str, mode: str):
        """Display quiz configuration options"""
        self.console.clear()
        
        self.console.print(Panel(
            f"[bold]{get_text('quiz_config', 'title')}[/bold]\n{level} - {mode}",
            border_style="cyan"
        ))
        
        # Question count selection
        self.console.print(f"\n{get_text('quiz_config', 'question_count')}")
        self.console.print(f"[1] {get_text('quiz_config', 'questions_25')}")
        self.console.print(f"[2] {get_text('quiz_config', 'questions_50')}")
        self.console.print(f"[3] {get_text('quiz_config', 'questions_100')}")
        self.console.print(f"[4] {get_text('quiz_config', 'questions_all')}")
        
        question_choice = IntPrompt.ask("선택하세요", choices=["1", "2", "3", "4"])
        question_counts = [25, 50, 100, -1]  # -1 means all
        question_count = question_counts[question_choice - 1]
        
        # Feedback mode selection
        self.console.print(f"\n{get_text('quiz_config', 'feedback_mode')}")
        self.console.print(f"[1] {get_text('quiz_config', 'immediate')}")
        self.console.print(f"[2] {get_text('quiz_config', 'deferred')}")
        
        feedback_choice = IntPrompt.ask("선택하세요", choices=["1", "2"])
        feedback_mode = "immediate" if feedback_choice == 1 else "deferred"
        
        # Hiragana display selection (for all modes)
        show_hiragana = False
        if mode in ["vocabulary", "grammar", "mixed"]:
            self.console.print(f"\n{get_text('quiz_config', 'hiragana_display')}")
            self.console.print(f"[1] {get_text('quiz_config', 'kanji_only')}")
            self.console.print(f"[2] {get_text('quiz_config', 'kanji_hiragana')}")
            
            hiragana_choice = IntPrompt.ask("선택하세요", choices=["1", "2"])
            show_hiragana = hiragana_choice == 2
        
        # Confirm and start quiz
        self.console.print("\n[bold cyan]퀴즈 설정 완료[/bold cyan]")
        self.console.print(f"레벨: {level}")
        self.console.print(f"모드: {mode}")
        self.console.print(f"문제 수: {question_count if question_count > 0 else '전체'}")
        self.console.print(f"답안 표시: {get_text('quiz_config', feedback_mode)}")
        if mode in ["vocabulary", "grammar", "mixed"]:
            hiragana_text = get_text('quiz_config', 'kanji_hiragana') if show_hiragana else get_text('quiz_config', 'kanji_only')
            self.console.print(f"히라가나: {hiragana_text}")
        
        if Confirm.ask(f"\n{get_text('quiz_config', 'start_quiz')}?"):
            self.start_quiz(level, mode, question_count, feedback_mode, show_hiragana)
    
    def start_quiz(self, level: str, mode: str, question_count: int, feedback_mode: str, show_hiragana: bool):
        """Start the quiz with specified parameters"""
        self.console.clear()
        
        # Prepare quiz
        self.quiz_display.show_loading_message("퀴즈를 준비하는 중...")
        
        success = self.quiz_engine.prepare_quiz(level, mode, question_count, feedback_mode, show_hiragana)
        if not success:
            self.console.print("[red]퀴즈를 준비하는 중 오류가 발생했습니다.[/red]")
            self.console.input("\n[Enter]를 눌러 계속...")
            return
        
        # Start quiz
        self.quiz_engine.start_quiz()
        
        # Quiz loop
        while not self.quiz_engine.is_quiz_finished():
            # Get current question
            question = self.quiz_engine.get_current_question()
            if not question:
                break
            
            # Show question and get answer
            answer_index = self.quiz_display.show_question(question)
            
            # Handle quit signal
            if answer_index == -1:
                if self.quiz_display.confirm_quit():
                    return
                else:
                    continue
            
            # Submit answer
            feedback = self.quiz_engine.submit_answer(answer_index)
            
            # Show immediate feedback if configured
            if feedback_mode == 'immediate':
                continue_quiz = self.quiz_display.show_immediate_feedback(feedback)
                if not continue_quiz:
                    if self.quiz_display.confirm_quit():
                        return
                    else:
                        continue
            
            # Move to next question
            self.quiz_engine.next_question()
        
        # Quiz finished - get results
        results = self.quiz_engine.get_quiz_results()
        
        # Show deferred answers if configured
        if feedback_mode == 'deferred':
            self.quiz_display.show_deferred_answers(results)
        
        # Show final results
        self.quiz_display.show_quiz_results(results)
    
    def show_previous_results(self):
        """Display previous quiz results"""
        self.console.clear()
        self.console.print(Panel(
            f"[bold]{get_text('results', 'title')}[/bold]\n\n이전 결과가 없습니다.\n(구현 예정)",
            border_style="cyan"
        ))
        self.console.input(f"\n[Enter]를 눌러 계속...")
    
    def show_settings(self):
        """Display settings menu"""
        self.console.clear()
        
        content = f"""
[1] {get_text('settings', 'clear_history')}
[2] {get_text('settings', 'export_results')}
[3] {get_text('settings', 'about')}

[4] {get_text('settings', 'back')}
        """
        
        self.console.print(Panel(
            content.strip(),
            title=f"[bold]{get_text('settings', 'title')}[/bold]",
            border_style="cyan"
        ))
        
        try:
            choice = IntPrompt.ask("선택하세요", choices=["1", "2", "3", "4"])
            
            if choice == 1:
                if Confirm.ask(get_text('settings', 'confirm_clear')):
                    self.console.print(f"[green]{get_text('settings', 'history_cleared')}[/green]")
            elif choice == 2:
                self.console.print(f"[green]{get_text('settings', 'results_exported')} results.json[/green]")
            elif choice == 3:
                self.show_about()
            elif choice == 4:
                return
                
            if choice != 4:
                self.console.input(f"\n[Enter]를 눌러 계속...")
                
        except KeyboardInterrupt:
            return
    
    def show_about(self):
        """Show about information"""
        about_text = """[bold cyan]JLPT 학습 퀴즈 v1.0.0[/bold cyan]

일본어 능력시험(JLPT) 학습을 위한 터미널 기반 퀴즈 애플리케이션

[bold]기능:[/bold]
• N5-N1 레벨 지원 (현재 N4 사용 가능)
• 어휘 및 문법 퀴즈
• 한국어 인터페이스 및 해설
• 맞춤형 퀴즈 설정
• 학습 진도 추적

[bold]개발자:[/bold] JLPT Quiz Team
[bold]라이센스:[/bold] MIT License"""

        self.console.print(Panel(about_text, border_style="cyan"))