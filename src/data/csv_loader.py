"""CSV data loader for JLPT quiz questions"""

import pandas as pd
import os
from typing import List, Dict, Optional
from pathlib import Path

class CSVLoader:
    """Loads and manages JLPT question data from CSV files"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.vocabulary_cache = {}
        self.grammar_cache = {}
    
    def load_vocabulary(self, level: str = "N4") -> List[Dict]:
        """Load vocabulary data for specified JLPT level"""
        if level in self.vocabulary_cache:
            return self.vocabulary_cache[level]
        
        filename = f"{level.lower()}_vocabulary.csv"
        filepath = self.data_dir / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"Vocabulary file not found: {filepath}")
        
        try:
            df = pd.read_csv(filepath)
            
            # Validate required columns
            required_columns = ['kanji', 'hiragana', 'pos', 'korean_meaning', 'question_type', 'difficulty']
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")
            
            # Convert to list of dictionaries
            vocabulary_data = df.to_dict('records')
            
            # Cache the data
            self.vocabulary_cache[level] = vocabulary_data
            
            return vocabulary_data
            
        except pd.errors.EmptyDataError:
            raise ValueError(f"Empty vocabulary file: {filepath}")
        except Exception as e:
            raise RuntimeError(f"Error loading vocabulary data: {str(e)}")
    
    def load_grammar(self, level: str = "N4") -> List[Dict]:
        """Load grammar data for specified JLPT level"""
        if level in self.grammar_cache:
            return self.grammar_cache[level]
        
        filename = f"{level.lower()}_grammar.csv"
        filepath = self.data_dir / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"Grammar file not found: {filepath}")
        
        try:
            df = pd.read_csv(filepath)
            
            # Validate required columns
            required_columns = ['grammar_pattern', 'japanese_sentence', 'hiragana_reading', 
                               'korean_translation', 'question_type', 'difficulty']
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")
            
            # Convert to list of dictionaries
            grammar_data = df.to_dict('records')
            
            # Cache the data
            self.grammar_cache[level] = grammar_data
            
            return grammar_data
            
        except pd.errors.EmptyDataError:
            raise ValueError(f"Empty grammar file: {filepath}")
        except Exception as e:
            raise RuntimeError(f"Error loading grammar data: {str(e)}")
    
    def get_vocabulary_count(self, level: str = "N4", question_type: Optional[str] = None) -> int:
        """Get count of vocabulary questions"""
        data = self.load_vocabulary(level)
        
        if question_type:
            return len([item for item in data if item['question_type'] == question_type])
        return len(data)
    
    def get_grammar_count(self, level: str = "N4", question_type: Optional[str] = None) -> int:
        """Get count of grammar questions"""
        data = self.load_grammar(level)
        
        if question_type:
            return len([item for item in data if item['question_type'] == question_type])
        return len(data)
    
    def get_available_levels(self) -> List[str]:
        """Get list of available JLPT levels"""
        available_levels = []
        
        for level in ['N5', 'N4', 'N3', 'N2', 'N1']:
            vocab_file = self.data_dir / f"{level.lower()}_vocabulary.csv"
            grammar_file = self.data_dir / f"{level.lower()}_grammar.csv"
            
            if vocab_file.exists() and grammar_file.exists():
                available_levels.append(level)
        
        return available_levels
    
    def get_question_types(self, level: str = "N4", category: str = "vocabulary") -> List[str]:
        """Get available question types for a category"""
        if category == "vocabulary":
            data = self.load_vocabulary(level)
        else:
            data = self.load_grammar(level)
        
        question_types = list(set(item['question_type'] for item in data))
        return sorted(question_types)
    
    def filter_by_difficulty(self, data: List[Dict], difficulty: int) -> List[Dict]:
        """Filter questions by difficulty level (1-3)"""
        return [item for item in data if item['difficulty'] == difficulty]
    
    def filter_by_question_type(self, data: List[Dict], question_type: str) -> List[Dict]:
        """Filter questions by question type"""
        return [item for item in data if item['question_type'] == question_type]
    
    def validate_data_integrity(self, level: str = "N4") -> Dict[str, List[str]]:
        """Validate data integrity and return any issues found"""
        issues = {'vocabulary': [], 'grammar': []}
        
        # Validate vocabulary data
        try:
            vocab_data = self.load_vocabulary(level)
            for i, item in enumerate(vocab_data):
                if not item.get('kanji'):
                    issues['vocabulary'].append(f"Row {i+1}: Missing kanji")
                if not item.get('hiragana'):
                    issues['vocabulary'].append(f"Row {i+1}: Missing hiragana")
                if not item.get('korean_meaning'):
                    issues['vocabulary'].append(f"Row {i+1}: Missing Korean meaning")
                if item.get('difficulty') not in [1, 2, 3]:
                    issues['vocabulary'].append(f"Row {i+1}: Invalid difficulty level")
        except Exception as e:
            issues['vocabulary'].append(f"Failed to load vocabulary: {str(e)}")
        
        # Validate grammar data
        try:
            grammar_data = self.load_grammar(level)
            for i, item in enumerate(grammar_data):
                if not item.get('grammar_pattern'):
                    issues['grammar'].append(f"Row {i+1}: Missing grammar pattern")
                if not item.get('japanese_sentence'):
                    issues['grammar'].append(f"Row {i+1}: Missing Japanese sentence")
                if not item.get('korean_translation'):
                    issues['grammar'].append(f"Row {i+1}: Missing Korean translation")
                if item.get('difficulty') not in [1, 2, 3]:
                    issues['grammar'].append(f"Row {i+1}: Invalid difficulty level")
        except Exception as e:
            issues['grammar'].append(f"Failed to load grammar: {str(e)}")
        
        return issues
    
    def clear_cache(self):
        """Clear cached data"""
        self.vocabulary_cache.clear()
        self.grammar_cache.clear()