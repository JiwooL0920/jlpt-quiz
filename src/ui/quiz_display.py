"""Quiz display system for JLPT application"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.text import Text
from rich.table import Table
from typing import Dict, Optional
import time

from ..utils.korean_ui import get_text, format_score, format_time, get_grade_text

class QuizDisplay:
    """Handles quiz display and user interaction"""
    
    def __init__(self, console: Console):
        self.console = console
    
    def show_question(self, question: Dict) -> int:
        """Display question and get user answer"""
        self.console.clear()
        
        # Create question header
        header_text = get_text('question', 'question_format').format(
            current=question['current_index'],
            total=question['total_questions'],
            type=question['type'],
            level=question['level']
        )
        
        # Create question content
        content = Text()
        content.append(f"{question['question_text']}\n\n", style="bold")
        
        # Display the main text (kanji, sentence, or meaning)
        display_text = question['display_text']
        if '\n' in display_text:  # Multi-line display (kanji + hiragana)
            lines = display_text.split('\n')
            content.append(f"        {lines[0]}\n", style="bold cyan")
            if len(lines) > 1:
                content.append(f"      {lines[1]}\n", style="dim cyan")
        else:
            content.append(f"        {display_text}\n", style="bold cyan")
        
        content.append("\n")
        
        # Display options
        for i, option in enumerate(question['options'], 1):
            content.append(f"{i}. {option}\n")
        
        # Show the panel
        self.console.print(Panel(
            content,
            title=f"[bold]{header_text}[/bold]",
            border_style="cyan"
        ))
        
        # Get user input
        try:
            choice = IntPrompt.ask(
                "\n[cyan]답을 선택하세요[/cyan]",
                choices=[str(i) for i in range(1, len(question['options']) + 1)]
            )
            return choice - 1  # Convert to 0-based index
        except KeyboardInterrupt:
            return -1  # Signal to quit
    
    def show_immediate_feedback(self, feedback: Dict) -> bool:
        """Show immediate feedback after answering. Returns True to continue, False to quit"""
        self.console.clear()
        
        # Determine feedback style
        if feedback['is_correct']:
            title = f"[bold green]{get_text('feedback', 'correct')}[/bold green]"
            border_style = "green"
        else:
            title = f"[bold red]{get_text('feedback', 'incorrect')}[/bold red]"
            border_style = "red"
        
        # Create feedback content
        content = Text()
        content.append(f"{get_text('feedback', 'your_answer')} {feedback['submitted_answer']}\n")
        content.append(f"{get_text('feedback', 'correct_answer')} {feedback['correct_answer']}\n\n")
        
        content.append(f"{get_text('feedback', 'explanation')}\n", style="bold")
        content.append(f"{feedback['explanation']}\n\n")
        
        # For vocabulary and grammar questions, show translations for all options
        if feedback.get('option_translations'):
            if feedback.get('question_type') == 'vocabulary':
                content.append("모든 선택지 번역:\n", style="bold dim")
            elif feedback.get('question_type') == 'grammar':
                content.append("모든 선택지 원문:\n", style="bold dim")
            else:
                content.append("모든 선택지 번역:\n", style="bold dim")
                
            for translation in feedback['option_translations']:
                # Check if translation already starts with bullet point (reading comprehension format)
                if translation.startswith('•'):
                    # Reading comprehension format: already has bullet points, just add indentation
                    content.append(f"  {translation}\n", style="dim")
                    # Add extra spacing between reading comprehension options
                    content.append("\n")
                else:
                    # Vocabulary format: add bullet points
                    content.append(f"  • {translation}\n", style="dim")
            content.append("\n")
        
        # Show continue prompt
        if feedback['question_number'] < feedback['total_questions']:
            continue_text = get_text('feedback', 'continue')
        else:
            continue_text = get_text('feedback', 'finish')
        
        content.append(continue_text, style="dim")
        
        self.console.print(Panel(
            content,
            title=title,
            border_style=border_style
        ))
        
        try:
            self.console.input()
            return True
        except KeyboardInterrupt:
            return False
    
    def show_deferred_answers(self, results: Dict):
        """Show all answers at the end for deferred feedback mode"""
        self.console.clear()
        
        self.console.print(Panel(
            "[bold]전체 문제 답안[/bold]",
            border_style="cyan"
        ))
        
        for i, answer in enumerate(results['detailed_answers'], 1):
            question = answer['question']
            
            # Question info
            status = "✓" if answer['is_correct'] else "✗"
            status_color = "green" if answer['is_correct'] else "red"
            
            self.console.print(f"\n[bold]문제 {i}[/bold] [{status_color}]{status}[/{status_color}]")
            self.console.print(f"질문: {question['question_text']}")
            self.console.print(f"내용: {question['display_text']}")
            self.console.print(f"선택한 답: {question['options'][answer['submitted_answer']]}")
            self.console.print(f"정답: {question['options'][answer['correct_answer']]}")
            self.console.print(f"해설: {question['explanation']}")
            
            if i % 3 == 0 and i < len(results['detailed_answers']):  # Show 3 at a time
                self.console.input("\n[Enter]를 눌러 계속...")
                self.console.clear()
        
        self.console.input(f"\n[Enter]를 눌러 결과 화면으로...")
    
    def show_quiz_results(self, results: Dict):
        """Display final quiz results"""
        self.console.clear()
        
        # Calculate grade and color
        score_percentage = results['score_percentage']
        grade_text, grade_color = get_grade_text(score_percentage)
        
        # Create results content
        content = Text()
        content.append(f"{get_text('results', 'overall_score')} ", style="bold")
        content.append(f"{format_score(score_percentage)}\n", style=f"bold {grade_color}")
        
        content.append(f"{get_text('results', 'correct_answers')} ")
        content.append(f"{results['correct_answers']}/{results['total_questions']}개\n")
        
        content.append(f"{get_text('results', 'total_time')} ")
        content.append(f"{format_time(results['total_time_seconds'])}\n\n")
        
        # Category breakdown
        if results['category_scores']:
            content.append(f"{get_text('results', 'category_breakdown')}\n", style="bold")
            
            for category, scores in results['category_scores'].items():
                category_name = get_text('results', 'vocabulary') if category == 'vocabulary' else get_text('results', 'grammar')
                category_score = scores['percentage']
                category_color = get_grade_text(category_score)[1]
                
                content.append(f"• {category_name} ")
                content.append(f"{format_score(category_score)}\n", style=category_color)
        
        # Weak areas
        if results['weak_areas']:
            content.append(f"\n{get_text('results', 'weak_areas')}\n", style="bold red")
            
            for weak_area in results['weak_areas']:
                category_name = self._get_category_korean_name(weak_area['category'])
                percentage = weak_area['performance']['percentage']
                content.append(f"• {category_name} ({format_score(percentage)})\n")
            
            content.append(f"\n{get_text('results', 'recommendations')}\n", style="bold cyan")
            
            # Show recommendations from all weak areas
            all_recommendations = []
            for weak_area in results['weak_areas']:
                all_recommendations.extend(weak_area['recommendations'])
            
            # Remove duplicates and show top 5
            unique_recommendations = list(dict.fromkeys(all_recommendations))[:5]
            for rec in unique_recommendations:
                content.append(f"• {rec}\n")
        else:
            content.append(f"\n[bold green]모든 분야에서 우수한 성과를 보였습니다![/bold green]\n")
        
        content.append(f"\n{get_text('results', 'continue')}", style="dim")
        
        # Show results panel
        self.console.print(Panel(
            content,
            title=f"[bold]{get_text('results', 'title')} - {grade_text}[/bold]",
            border_style=grade_color
        ))
        
        try:
            self.console.input()
        except KeyboardInterrupt:
            pass
    
    def show_quiz_progress(self, progress: Dict):
        """Show quiz progress indicator"""
        current = progress['current_question']
        total = progress['total_questions']
        correct = progress['correct_so_far']
        
        progress_text = f"진행: {current}/{total} | 정답: {correct}개"
        self.console.print(f"[dim]{progress_text}[/dim]")
    
    def show_loading_message(self, message: str):
        """Show a loading message"""
        self.console.print(f"[cyan]{message}[/cyan]")
    
    def confirm_quit(self) -> bool:
        """Ask user to confirm quitting the quiz"""
        from rich.prompt import Confirm
        return Confirm.ask("\n[yellow]정말로 퀴즈를 종료하시겠습니까?[/yellow]")
    
    def _get_category_korean_name(self, category: str) -> str:
        """Get Korean name for question category"""
        category_names = {
            'reading': '한자 읽기',
            'meaning_to_japanese': '의미 → 일본어',
            'japanese_to_meaning': '일본어 → 의미',
            'sentence_completion': '문장 완성',
            'meaning_comprehension': '의미 이해'
        }
        return category_names.get(category, category)