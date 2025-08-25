"""Quiz engine for JLPT application"""

import random
import time
from typing import List, Dict, Optional, Tuple
from ..data.csv_loader import CSVLoader
from ..data.question_generator import QuestionGenerator

class QuizEngine:
    """Main quiz engine that manages quiz flow and scoring"""
    
    def __init__(self):
        self.csv_loader = CSVLoader()
        self.question_generator = QuestionGenerator()
        self.reset_quiz()
    
    def reset_quiz(self):
        """Reset quiz state"""
        self.questions = []
        self.current_question_index = 0
        self.answers = []
        self.start_time = None
        self.end_time = None
        self.quiz_config = {}
    
    def prepare_quiz(self, level: str, mode: str, question_count: int, 
                    feedback_mode: str, show_hiragana: bool) -> bool:
        """Prepare quiz with specified configuration"""
        try:
            self.reset_quiz()
            self.quiz_config = {
                'level': level,
                'mode': mode,
                'question_count': question_count,
                'feedback_mode': feedback_mode,
                'show_hiragana': show_hiragana
            }
            
            # Load data based on mode
            if mode == 'vocabulary':
                data = self.csv_loader.load_vocabulary(level)
                question_pool = self._prepare_vocabulary_questions(data, show_hiragana)
            elif mode == 'grammar':
                data = self.csv_loader.load_grammar(level)
                question_pool = self._prepare_grammar_questions(data, show_hiragana)
            elif mode == 'mixed':
                vocab_data = self.csv_loader.load_vocabulary(level)
                grammar_data = self.csv_loader.load_grammar(level)
                vocab_questions = self._prepare_vocabulary_questions(vocab_data, show_hiragana)
                grammar_questions = self._prepare_grammar_questions(grammar_data, show_hiragana)
                question_pool = vocab_questions + grammar_questions
                random.shuffle(question_pool)
            else:
                raise ValueError(f"Unknown quiz mode: {mode}")
            
            # Select questions
            if question_count == -1:  # All questions
                self.questions = question_pool
            else:
                self.questions = random.sample(question_pool, min(question_count, len(question_pool)))
            
            return len(self.questions) > 0
            
        except Exception as e:
            print(f"Error preparing quiz: {str(e)}")
            return False
    
    def _prepare_vocabulary_questions(self, vocab_data: List[Dict], show_hiragana: bool) -> List[Dict]:
        """Prepare vocabulary questions from data"""
        questions = []
        for item in vocab_data:
            try:
                # Skip reading questions when hiragana is being displayed
                if show_hiragana and item['question_type'] == 'reading':
                    continue
                    
                question = self.question_generator.generate_vocabulary_question(item, show_hiragana)
                questions.append(question)
            except Exception as e:
                print(f"Error generating vocabulary question: {str(e)}")
                continue
        return questions
    
    def _prepare_grammar_questions(self, grammar_data: List[Dict], show_hiragana: bool) -> List[Dict]:
        """Prepare grammar questions from data"""
        questions = []
        for item in grammar_data:
            try:
                question = self.question_generator.generate_grammar_question(item, show_hiragana)
                questions.append(question)
            except Exception as e:
                print(f"Error generating grammar question: {str(e)}")
                continue
        return questions
    
    def start_quiz(self):
        """Start the quiz"""
        if not self.questions:
            raise RuntimeError("No questions prepared")
        
        self.start_time = time.time()
        self.current_question_index = 0
        self.answers = []
    
    def get_current_question(self) -> Optional[Dict]:
        """Get the current question"""
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index].copy()
            question['current_index'] = self.current_question_index + 1
            question['total_questions'] = len(self.questions)
            return question
        return None
    
    def submit_answer(self, answer_index: int) -> Dict:
        """Submit answer and get feedback"""
        if self.current_question_index >= len(self.questions):
            raise RuntimeError("No current question")
        
        current_question = self.questions[self.current_question_index]
        correct_answer_index = current_question['correct_answer']
        is_correct = answer_index == correct_answer_index
        
        # Record answer
        answer_record = {
            'question_index': self.current_question_index,
            'question': current_question,
            'submitted_answer': answer_index,
            'correct_answer': correct_answer_index,
            'is_correct': is_correct,
            'timestamp': time.time()
        }
        self.answers.append(answer_record)
        
        # Prepare feedback
        feedback = {
            'is_correct': is_correct,
            'submitted_answer': current_question['options'][answer_index],
            'correct_answer': current_question['options'][correct_answer_index],
            'explanation': current_question['explanation'],
            'question_number': self.current_question_index + 1,
            'total_questions': len(self.questions)
        }
        
        return feedback
    
    def next_question(self) -> bool:
        """Move to next question. Returns True if there are more questions"""
        self.current_question_index += 1
        return self.current_question_index < len(self.questions)
    
    def is_quiz_finished(self) -> bool:
        """Check if quiz is finished"""
        return self.current_question_index >= len(self.questions)
    
    def get_quiz_results(self) -> Dict:
        """Get final quiz results"""
        if not self.is_quiz_finished():
            raise RuntimeError("Quiz not finished yet")
        
        if self.end_time is None:
            self.end_time = time.time()
        
        total_questions = len(self.questions)
        correct_answers = sum(1 for answer in self.answers if answer['is_correct'])
        total_time = int(self.end_time - self.start_time) if self.start_time else 0
        
        # Calculate category-specific scores
        category_scores = self._calculate_category_scores()
        
        # Identify weak areas
        weak_areas = self._identify_weak_areas()
        
        results = {
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'incorrect_answers': total_questions - correct_answers,
            'score_percentage': (correct_answers / total_questions * 100) if total_questions > 0 else 0,
            'total_time_seconds': total_time,
            'average_time_per_question': (total_time / total_questions) if total_questions > 0 else 0,
            'category_scores': category_scores,
            'weak_areas': weak_areas,
            'quiz_config': self.quiz_config,
            'detailed_answers': self.answers
        }
        
        return results
    
    def _calculate_category_scores(self) -> Dict:
        """Calculate scores by category (vocabulary/grammar)"""
        vocab_correct = vocab_total = 0
        grammar_correct = grammar_total = 0
        
        for answer in self.answers:
            question_type = answer['question']['type']
            if question_type == 'vocabulary':
                vocab_total += 1
                if answer['is_correct']:
                    vocab_correct += 1
            elif question_type == 'grammar':
                grammar_total += 1
                if answer['is_correct']:
                    grammar_correct += 1
        
        scores = {}
        if vocab_total > 0:
            scores['vocabulary'] = {
                'correct': vocab_correct,
                'total': vocab_total,
                'percentage': (vocab_correct / vocab_total * 100)
            }
        
        if grammar_total > 0:
            scores['grammar'] = {
                'correct': grammar_correct,
                'total': grammar_total,
                'percentage': (grammar_correct / grammar_total * 100)
            }
        
        return scores
    
    def _identify_weak_areas(self) -> List[Dict]:
        """Identify areas that need improvement"""
        weak_areas = []
        
        # Group by question category and difficulty
        category_performance = {}
        
        for answer in self.answers:
            question = answer['question']
            category = question['category']
            difficulty = question.get('difficulty', 1)
            
            if category not in category_performance:
                category_performance[category] = {'correct': 0, 'total': 0, 'questions': []}
            
            category_performance[category]['total'] += 1
            category_performance[category]['questions'].append(answer)
            if answer['is_correct']:
                category_performance[category]['correct'] += 1
        
        # Identify weak categories (< 70% correct)
        for category, performance in category_performance.items():
            percentage = (performance['correct'] / performance['total'] * 100) if performance['total'] > 0 else 0
            
            if percentage < 70:
                # Get wrong questions for this category
                wrong_questions = [
                    answer for answer in performance['questions'] 
                    if not answer['is_correct']
                ]
                
                weak_area = {
                    'category': category,
                    'performance': {
                        'correct': performance['correct'],
                        'total': performance['total'],
                        'percentage': percentage
                    },
                    'wrong_questions': wrong_questions[:3],  # Show up to 3 examples
                    'recommendations': self._get_recommendations(category, percentage)
                }
                weak_areas.append(weak_area)
        
        return weak_areas
    
    def _get_recommendations(self, category: str, percentage: float) -> List[str]:
        """Get study recommendations based on weak areas"""
        recommendations = []
        
        if category == 'reading':
            recommendations.extend([
                '한자 읽기 연습을 늘려보세요',
                '히라가나 표기를 함께 보며 학습하세요',
                'N4 한자 목록을 체계적으로 복습하세요'
            ])
        elif category == 'meaning_to_japanese':
            recommendations.extend([
                '한국어-일본어 단어 매칭 연습을 하세요',
                '단어의 품사별로 분류해서 학습하세요',
                '일상생활 어휘를 늘려보세요'
            ])
        elif category == 'japanese_to_meaning':
            recommendations.extend([
                '일본어 문맥에서 단어 의미 파악 연습을 하세요',
                '유사한 의미의 단어들을 비교 학습하세요',
                '예문과 함께 단어를 암기하세요'
            ])
        elif category == 'sentence_completion':
            recommendations.extend([
                '문법 패턴별로 체계적인 학습을 하세요',
                '예문을 많이 읽고 패턴을 익히세요',
                '비슷한 문법의 차이점을 정리하세요'
            ])
        elif category == 'meaning_comprehension':
            recommendations.extend([
                '일본어 문장 해석 연습을 늘려보세요',
                '문법과 어휘를 함께 학습하세요',
                '긴 문장 읽기 연습을 하세요'
            ])
        
        if percentage < 50:
            recommendations.append('기초부터 다시 차근차근 복습하세요')
        elif percentage < 70:
            recommendations.append('틀린 문제를 중심으로 집중 학습하세요')
        
        return recommendations[:3]  # Return top 3 recommendations
    
    def get_progress(self) -> Dict:
        """Get current quiz progress"""
        return {
            'current_question': self.current_question_index + 1,
            'total_questions': len(self.questions),
            'answered_questions': len(self.answers),
            'correct_so_far': sum(1 for answer in self.answers if answer['is_correct']),
            'percentage_complete': ((self.current_question_index + 1) / len(self.questions) * 100) if self.questions else 0
        }