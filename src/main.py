#!/usr/bin/env python3
"""
JLPT Quiz Application - Main Entry Point
Japanese Language Proficiency Test study tool with Korean interface
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path.parent))

import click
from rich.console import Console
from rich.panel import Panel
from rich.traceback import install

from src.ui.menu import MainMenu
from src.data.csv_loader import CSVLoader
from src.utils.korean_ui import get_text

# Install rich traceback handler
install()

console = Console()

@click.command()
@click.option('--validate', is_flag=True, help='데이터 무결성 검사')
@click.option('--level', default='N4', help='검사할 레벨 (기본값: N4)')
def main(validate, level):
    """JLPT 학습 퀴즈 애플리케이션
    
    일본어 능력시험 학습을 위한 터미널 기반 퀴즈 도구
    """
    
    if validate:
        validate_data(level)
        return
    
    try:
        # Initialize and run main menu directly
        menu = MainMenu(console)
        menu.run()
        
    except KeyboardInterrupt:
        console.print(f"\n[yellow]안녕히 가세요![/yellow]")
    except Exception as e:
        console.print(f"[red]오류가 발생했습니다: {str(e)}[/red]")
        console.print_exception()

def validate_data(level: str):
    """데이터 무결성 검사"""
    console.print(f"[cyan]{level} 데이터 검사 중...[/cyan]")
    
    try:
        csv_loader = CSVLoader()
        issues = csv_loader.validate_data_integrity(level)
        
        if not any(issues.values()):
            console.print(f"[green]✓ {level} 데이터가 정상입니다![/green]")
        else:
            console.print(f"[yellow]⚠️  {level} 데이터에서 문제가 발견되었습니다:[/yellow]")
            
            if issues['vocabulary']:
                console.print("\n[bold]어휘 데이터 문제:[/bold]")
                for issue in issues['vocabulary']:
                    console.print(f"  - {issue}")
            
            if issues['grammar']:
                console.print("\n[bold]독해 데이터 문제:[/bold]")
                for issue in issues['grammar']:
                    console.print(f"  - {issue}")
        
        # Display data statistics
        console.print(f"\n[bold]데이터 통계:[/bold]")
        try:
            vocab_count = csv_loader.get_vocabulary_count(level)
            grammar_count = csv_loader.get_grammar_count(level)
            console.print(f"어휘 문제: {vocab_count}개")
            console.print(f"독해 문제: {grammar_count}개")
            console.print(f"총 문제: {vocab_count + grammar_count}개")
        except Exception as e:
            console.print(f"[red]통계 정보를 가져올 수 없습니다: {str(e)}[/red]")
        
    except FileNotFoundError as e:
        console.print(f"[red]파일을 찾을 수 없습니다: {str(e)}[/red]")
    except Exception as e:
        console.print(f"[red]검사 중 오류가 발생했습니다: {str(e)}[/red]")

if __name__ == "__main__":
    main()