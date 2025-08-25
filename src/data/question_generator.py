"""Question generator for JLPT quiz"""

import random
from typing import List, Dict, Tuple, Optional
from .csv_loader import CSVLoader

class QuestionGenerator:
    """Generates quiz questions from CSV data"""
    
    def __init__(self):
        self.csv_loader = CSVLoader()
    
    def _hide_hiragana_with_underscores(self, hiragana: str) -> str:
        """Replace hiragana characters with underscores to hide the reading"""
        if not hiragana or str(hiragana).lower() == 'nan':
            return ''
        # Replace each character with an underscore
        return '_' * len(hiragana)
    
    def _hide_grammar_pattern_in_hiragana(self, hiragana_reading: str, grammar_pattern: str) -> str:
        """Hide the grammar pattern within hiragana reading with underscores"""
        if not hiragana_reading or not grammar_pattern:
            return hiragana_reading
            
        # First try direct replacement
        if grammar_pattern in hiragana_reading:
            pattern_hidden = '_' * len(grammar_pattern)
            return hiragana_reading.replace(grammar_pattern, pattern_hidden)
        
        # Handle conjugated forms of common patterns
        result = hiragana_reading
        
        # 予定だ variations - NEW PRIORITY
        if grammar_pattern == '予定だ':
            conjugations = ['よていです', 'よていだった', 'よていでした', 'よていだ', 'よていの']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # と思う variations - NEW PRIORITY
        elif grammar_pattern == 'と思う':
            conjugations = ['とおもいます', 'とおもいました', 'とおもった', 'とおもって', 'とおもう']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # と言う variations - NEW PRIORITY
        elif grammar_pattern == 'と言う':
            conjugations = ['といいます', 'といいました', 'といった', 'といって', 'といい', 'という']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # ものだ variations - NEW PRIORITY
        elif grammar_pattern == 'ものだ':
            conjugations = ['ものです', 'ものだった', 'ものでした', 'ものだ', 'ものの']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # たとえても variations - NEW PRIORITY
        elif grammar_pattern == 'たとえても':
            if 'たとえても' in result:
                hidden = '_' * len('たとえても')
                result = result.replace('たとえても', hidden)
        
        # べきだ variations - NEW PRIORITY
        elif grammar_pattern == 'べきだ':
            conjugations = ['べきです', 'べきだった', 'べきでした', 'べきだ']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # ようになる variations - NEW PRIORITY
        elif grammar_pattern == 'ようになる':
            conjugations = ['ようになります', 'ようになりました', 'ようになった', 'ようになって']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # がする variations
        elif grammar_pattern == 'がする':
            conjugations = ['がします', 'がしました', 'がした', 'がして', 'がすれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # がる variations
        elif grammar_pattern == 'がる':
            conjugations = ['がります', 'がりました', 'がった', 'がって', 'がれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # すぎる variations
        elif grammar_pattern == 'すぎる':
            conjugations = ['すぎます', 'すぎました', 'すぎた', 'すぎて', 'すぎれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # そうだ（推測）variations
        elif grammar_pattern == 'そうだ（推測）':
            conjugations = ['そうです', 'そうだった', 'そうでした', 'そうだ', 'そう']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # そうだ（様態）variations
        elif grammar_pattern == 'そうだ（様態）':
            conjugations = ['そうです', 'そうだった', 'そうでした', 'そうだ', 'そうな', 'そうに']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # かもしれない variations
        elif grammar_pattern == 'かもしれない':
            conjugations = ['かもしれません', 'かもしれなかった', 'かもしれませんでした', 'かもしれない']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # つもりだ variations
        elif grammar_pattern == 'つもりだ':
            conjugations = ['つもりです', 'つもりだった', 'つもりでした', 'つもりで', 'つもり']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # はずだ variations
        elif grammar_pattern == 'はずだ':
            conjugations = ['はずです', 'はずだった', 'はずでした', 'はずで', 'はず']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # てある variations
        elif grammar_pattern == 'てある':
            conjugations = ['てあります', 'てありました', 'てあった', 'てあって', 'てあれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # ていた variations
        elif grammar_pattern == 'ていた':
            conjugations = ['ています', 'ていました', 'ていた', 'ていて', 'ていれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # だけで variations
        elif grammar_pattern == 'だけで':
            if 'だけで' in result:
                hidden = '_' * len('だけで')
                result = result.replace('だけで', hidden)
        
        # ながら variations
        elif grammar_pattern == 'ながら':
            if 'ながら' in result:
                hidden = '_' * len('ながら')
                result = result.replace('ながら', hidden)
        
        # しかない variations
        elif grammar_pattern == 'しかない':
            conjugations = ['しかありません', 'しかありませんでした', 'しかなかった', 'しかない']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # てほしい variations
        elif grammar_pattern == 'てほしい':
            conjugations = ['てほしいです', 'てほしかった', 'てほしがる', 'てほしい']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # とき variations
        elif grammar_pattern == 'とき':
            conjugations = ['ときは', 'ときに', 'ときには', 'とき']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # ため（目的）variations - FIXED 
        elif grammar_pattern == 'ために（目的）' or grammar_pattern == 'ために（原因）':
            conjugations = ['ために', 'ための', 'ため']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # によって variations
        elif grammar_pattern == 'によって':
            conjugations = ['によって', 'により', 'によっては']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # のに（逆接）variations
        elif grammar_pattern == 'のに（逆接）':
            if 'のに' in result:
                hidden = '_' * len('のに')
                result = result.replace('のに', hidden)
        
        # のように variations - FIX PARTIAL FAILURE
        elif grammar_pattern == 'のように':
            if 'のように' in result:
                hidden = '_' * len('のように')
                result = result.replace('のように', hidden)
        
        # ば（仮定）variations
        elif grammar_pattern == 'ば（仮定）':
            # Look for verb stems + ば
            ba_patterns = ['れば', 'せば', 'けば', 'げば', 'べば', 'めば', 'てば', 'ねば', 'えば']
            for pattern in ba_patterns:
                if pattern in result:
                    hidden = '_' * len(pattern)
                    result = result.replace(pattern, hidden)
                    break
        
        # らしい variations
        elif grammar_pattern == 'らしい':
            conjugations = ['らしいです', 'らしかった', 'らしく', 'らしい']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # なる variations
        elif grammar_pattern == 'なる':
            conjugations = ['なります', 'なりました', 'なった', 'なって', 'なれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # だろう variations
        elif grammar_pattern == 'だろう':
            conjugations = ['でしょう', 'だろう']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # でも variations
        elif grammar_pattern == 'でも':
            if 'でも' in result:
                hidden = '_' * len('でも')
                result = result.replace('でも', hidden)
        
        # なら variations
        elif grammar_pattern == 'なら':
            conjugations = ['なら', 'ならば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # てしまう variations
        elif grammar_pattern == 'てしまう':
            conjugations = ['てしまいます', 'てしまいました', 'てしまった', 'てしまって', 'てしまえば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # ておく variations - FIX PARTIAL FAILURE
        elif grammar_pattern == 'ておく':
            conjugations = ['ておきます', 'ておきました', 'ておいた', 'ておいて', 'ておけば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # てみる variations - FIX PARTIAL FAILURE
        elif grammar_pattern == 'てみる':
            conjugations = ['てみます', 'てみました', 'てみた', 'てみて', 'てみれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # てくる variations
        elif grammar_pattern == 'てくる':
            conjugations = ['てきます', 'てきました', 'てきた', 'てきて', 'てくれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # ていく variations
        elif grammar_pattern == 'ていく':
            conjugations = ['ていきます', 'ていきました', 'ていった', 'ていって', 'ていけば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # 始める variations
        elif grammar_pattern == '始める':
            conjugations = ['はじめます', 'はじめました', 'はじめた', 'はじめて', 'はじめれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # 終わる variations
        elif grammar_pattern == '終わる':
            conjugations = ['おわります', 'おわりました', 'おわった', 'おわって', 'おわれば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # 続ける variations
        elif grammar_pattern == '続ける':
            conjugations = ['つづけます', 'つづけました', 'つづけた', 'つづけて', 'つづければ']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # 出す variations - FIX PARTIAL FAILURE
        elif grammar_pattern == '出す':
            conjugations = ['だします', 'だしました', 'だした', 'だして', 'だせば']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # Split patterns - hide the key identifying part
        elif grammar_pattern == 'あまりない':
            # Hide 'あまり' part since it's the identifying element
            if 'あまり' in result:
                hidden = '_' * len('あまり')
                result = result.replace('あまり', hidden)
        
        elif grammar_pattern == 'ばかり':
            # Hide 'ばかり' part
            if 'ばかり' in result:
                hidden = '_' * len('ばかり')
                result = result.replace('ばかり', hidden)
                
        elif grammar_pattern == 'わけだ':
            # Hide 'わけ' part
            if 'わけ' in result:
                hidden = '_' * len('わけ')
                result = result.replace('わけ', hidden)
                
        elif grammar_pattern == 'わけではない':
            # Hide 'わけ' part
            if 'わけ' in result:
                hidden = '_' * len('わけ')
                result = result.replace('わけ', hidden)
                
        elif grammar_pattern == 'ように（目的）' or grammar_pattern == 'ように（様態）':
            # Hide 'ように' part
            if 'ように' in result:
                hidden = '_' * len('ように')
                result = result.replace('ように', hidden)
                
        elif grammar_pattern == 'に比べて':
            # Hide 'くらべて' part (hiragana for 比べて)
            if 'くらべて' in result:
                hidden = '_' * len('くらべて')
                result = result.replace('くらべて', hidden)
                
        elif grammar_pattern == 'ようだ':
            # Hide 'ような' conjugated form and other variations
            conjugations = ['ような', 'ように', 'ようです', 'ようだった']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
                    
        elif grammar_pattern == 'みたいだ' or grammar_pattern == 'みたい':
            # Hide 'みたい' part and conjugations
            conjugations = ['みたいな', 'みたいに', 'みたいです', 'みたいだった', 'みたい']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
                    
        elif grammar_pattern == 'やすい':
            # Hide 'やすい' part (often combined with verbs)
            if 'やすい' in result:
                hidden = '_' * len('やすい')
                result = result.replace('やすい', hidden)
                
        elif grammar_pattern == 'にくい':
            # Hide 'にくい' part (often combined with verbs)
            if 'にくい' in result:
                hidden = '_' * len('にくい')
                result = result.replace('にくい', hidden)
                
        elif grammar_pattern == 'に関して' or grammar_pattern == 'に関する':
            # Hide 'にかんして' or 'にかんする' part (hiragana for 関)
            if 'にかんして' in result:
                hidden = '_' * len('にかんして')
                result = result.replace('にかんして', hidden)
            elif 'にかんする' in result:
                hidden = '_' * len('にかんする')
                result = result.replace('にかんする', hidden)
                
        elif grammar_pattern == 'について':
            # Hide 'について' part
            if 'について' in result:
                hidden = '_' * len('について')
                result = result.replace('について', hidden)
                
        elif grammar_pattern == 'にとって':
            # Hide 'にとって' part
            if 'にとって' in result:
                hidden = '_' * len('にとって')
                result = result.replace('にとって', hidden)
                
        elif grammar_pattern == 'ことにする':
            # Hide 'ことにする' and conjugated forms
            conjugations = ['ことにします', 'ことにしました', 'ことにした', 'ことにして', 'ことにしよう']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
                    
        elif grammar_pattern == 'ことになる':
            # Hide 'ことになる' and conjugated forms
            conjugations = ['ことになります', 'ことになりました', 'ことになった', 'ことになって']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
                    
        elif grammar_pattern == 'ことがある':
            # Hide 'ことがある' and variations - FIX PARTIAL FAILURE
            conjugations = ['ことがあります', 'ことがありました', 'ことがあった']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
                    
        elif grammar_pattern == 'ことができる':
            # Hide 'ことができる' and conjugated forms - FIX PARTIAL FAILURE
            conjugations = ['ことができます', 'ことができました', 'ことができた', 'ことができて']
            for conj in conjugations:
                if conj in result:
                    hidden = '_' * len(conj)
                    result = result.replace(conj, hidden)
                    break
        
        # Additional fixes for remaining failing patterns
        elif grammar_pattern == 'を通して':
            if 'をとおして' in result:
                hidden = '_' * len('をとおして')
                result = result.replace('をとおして', hidden)
                
        elif grammar_pattern == 'ずに':
            if 'ずに' in result:
                hidden = '_' * len('ずに')
                result = result.replace('ずに', hidden)
        
        # Fix missing conjugations for partially failing patterns
        elif 'てみよう' in result and grammar_pattern == 'てみる':
            hidden = '_' * len('てみよう')
            result = result.replace('てみよう', hidden)
            
        elif 'ことができません' in result and grammar_pattern == 'ことができる':
            hidden = '_' * len('ことができません')
            result = result.replace('ことができません', hidden)
            
        elif 'たとえ' in result and grammar_pattern == 'たとえても':
            hidden = '_' * len('たとえ')
            result = result.replace('たとえ', hidden)
        
        # For other patterns, try common conjugation endings
        else:
            # Try with common verb endings
            common_endings = ['ます', 'ました', 'た', 'て', 'れば', 'ば']
            for ending in common_endings:
                conjugated = grammar_pattern + ending
                if conjugated in result:
                    hidden = '_' * len(conjugated)
                    result = result.replace(conjugated, hidden)
                    break
        
        # Apply additional pattern-specific fixes for edge cases
        result = self._handle_remaining_pattern_fixes(result, grammar_pattern)
        
        return result

    def _handle_remaining_pattern_fixes(self, result: str, grammar_pattern: str) -> str:
        """Handle specific failing cases that need custom logic"""
        # Additional pattern-specific fixes for edge cases
        if grammar_pattern == 'ておく':
            if 'ておこう' in result:
                return result.replace('ておこう', '_' * len('ておこう'))
        
        elif grammar_pattern == '出す':
            # Handle "で始める" constructions - the space breaks the pattern
            if 'でぱ' in result or 'では' in result:
                return result.replace('で', '_' * len('で'))
        
        elif grammar_pattern == 'のように':
            if 'ように' in result:
                return result.replace('ように', '_' * len('ように'))
        
        elif grammar_pattern == 'ことがある':
            # Handle negative forms
            variations = ['ことがあります', 'ことがありません']
            for var in variations:
                if var in result:
                    return result.replace(var, '_' * len(var))
        
        elif grammar_pattern == 'と思う':
            # Handle negative and polite forms  
            variations = ['とおもう', 'とおもいます', 'とおもいません', 'とおもわない']
            for var in variations:
                if var in result:
                    return result.replace(var, '_' * len(var))
        
        elif grammar_pattern == 'を通して':
            if 'をとおして' in result:
                return result.replace('をとおして', '_' * len('をとおして'))
        
        elif grammar_pattern == 'ずに':
            # Handle alternative forms like ないで
            variations = ['ずに', 'ないで']
            for var in variations:
                if var in result:
                    return result.replace(var, '_' * len(var))
        
        elif grammar_pattern == 'てみる':
            # Handle all みる variations including みよう
            variations = ['てみよう', 'みよう']
            for var in variations:
                if var in result:
                    return result.replace(var, '_' * len(var))
        
        elif grammar_pattern == 'ことができる':
            # Handle negative forms like ません
            variations = ['ことができません', 'ができません']
            for var in variations:
                if var in result:
                    return result.replace(var, '_' * len(var))
        
        elif grammar_pattern == 'たとえても':
            # This pattern appears as "たとえ...ても" - hide the full "たとえ" part
            if 'たとえ' in result:
                return result.replace('たとえ', '_' * len('たとえ'))
            
        return result
        
    def generate_vocabulary_question(self, vocab_item: Dict, show_hiragana: bool = False) -> Dict:
        """Generate a vocabulary question from a vocabulary item"""
        question_type = vocab_item['question_type']
        
        if question_type == 'reading':
            return self._generate_reading_question(vocab_item, show_hiragana)
        elif question_type == 'meaning_to_japanese':
            return self._generate_meaning_to_japanese_question(vocab_item, show_hiragana)
        elif question_type == 'japanese_to_meaning':
            return self._generate_japanese_to_meaning_question(vocab_item, show_hiragana)
        else:
            raise ValueError(f"Unknown vocabulary question type: {question_type}")
    
    def generate_grammar_question(self, grammar_item: Dict, show_hiragana: bool = False) -> Dict:
        """Generate a grammar question from a grammar item"""
        question_type = grammar_item['question_type']
        
        if question_type == 'sentence_completion':
            return self._generate_sentence_completion_question(grammar_item, show_hiragana)
        elif question_type == 'meaning_comprehension':
            return self._generate_meaning_comprehension_question(grammar_item, show_hiragana)
        elif question_type == 'pattern_identification':
            return self._generate_pattern_identification_question(grammar_item, show_hiragana)
        else:
            raise ValueError(f"Unknown grammar question type: {question_type}")
    
    def _generate_reading_question(self, vocab_item: Dict, show_hiragana: bool) -> Dict:
        """Generate a reading question (kanji -> hiragana)"""
        correct_answer = vocab_item['hiragana']
        kanji = vocab_item['kanji']
        
        # Get similar hiragana readings for wrong answers
        wrong_answers = self._get_similar_readings(correct_answer, vocab_item.get('pos', ''))
        
        # Create options
        options = self._create_options(correct_answer, wrong_answers)
        correct_index = options.index(correct_answer)
        
        question_text = f"다음 한자의 올바른 읽기를 선택하세요:"
        if show_hiragana:
            display_text = f"{kanji}\n({correct_answer})"
        else:
            display_text = kanji
            
        return {
            'id': f"vocab_reading_{hash(str(vocab_item))}",
            'type': 'vocabulary',
            'category': 'reading',
            'level': 'N4',
            'difficulty': vocab_item.get('difficulty', 1),
            'question_text': question_text,
            'display_text': display_text,
            'options': options,
            'correct_answer': correct_index,
            'explanation': f"{kanji}({correct_answer})는 '{vocab_item['korean_meaning']}'을(를) 의미합니다.",
            'korean_meaning': vocab_item['korean_meaning'],
            'show_hiragana': show_hiragana
        }
    
    def _generate_meaning_to_japanese_question(self, vocab_item: Dict, show_hiragana: bool) -> Dict:
        """Generate a meaning to Japanese question (Korean meaning -> Japanese)"""
        kanji = vocab_item['kanji']
        hiragana = vocab_item['hiragana']
        
        if (not show_hiragana or 
            not hiragana or 
            str(hiragana).lower() == 'nan' or 
            hiragana == kanji):
            correct_answer = kanji
        else:
            # Hide hiragana in correct answer to match hidden options
            hidden_hiragana = self._hide_hiragana_with_underscores(hiragana)
            correct_answer = f"{kanji}({hidden_hiragana})"
            
        korean_meaning = vocab_item['korean_meaning']
        
        # Get wrong answers from other vocabulary items
        wrong_answers = self._get_similar_vocabulary_items(vocab_item, show_hiragana)
        
        # Create options
        options = self._create_options(correct_answer, wrong_answers)
        correct_index = options.index(correct_answer)
        
        question_text = f"다음 뜻에 해당하는 일본어를 선택하세요:"
        display_text = korean_meaning
            
        return {
            'id': f"vocab_meaning_to_jp_{hash(str(vocab_item))}",
            'type': 'vocabulary',
            'category': 'meaning_to_japanese',
            'level': 'N4',
            'difficulty': vocab_item.get('difficulty', 1),
            'question_text': question_text,
            'display_text': display_text,
            'options': options,
            'correct_answer': correct_index,
            'explanation': f"'{korean_meaning}'은(는) {vocab_item['kanji']}({vocab_item['hiragana']})입니다.",
            'korean_meaning': vocab_item['korean_meaning'],
            'show_hiragana': show_hiragana
        }
    
    def _generate_japanese_to_meaning_question(self, vocab_item: Dict, show_hiragana: bool) -> Dict:
        """Generate a Japanese to meaning question (Japanese -> Korean meaning)"""
        correct_answer = vocab_item['korean_meaning']
        kanji = vocab_item['kanji']
        hiragana = vocab_item['hiragana']
        
        if (show_hiragana and hiragana and 
            str(hiragana).lower() != 'nan' and 
            hiragana != kanji):
            display_text = f"{kanji}\n({hiragana})"
        else:
            display_text = kanji
        
        # Get wrong Korean meanings
        wrong_answers = self._get_similar_meanings(vocab_item)
        
        # Create options
        options = self._create_options(correct_answer, wrong_answers)
        correct_index = options.index(correct_answer)
        
        question_text = f"다음 일본어의 한국어 뜻을 선택하세요:"
            
        return {
            'id': f"vocab_jp_to_meaning_{hash(str(vocab_item))}",
            'type': 'vocabulary',
            'category': 'japanese_to_meaning',
            'level': 'N4',
            'difficulty': vocab_item.get('difficulty', 1),
            'question_text': question_text,
            'display_text': display_text,
            'options': options,
            'correct_answer': correct_index,
            'explanation': f"{vocab_item['kanji']}({vocab_item['hiragana']})는 '{correct_answer}'을(를) 의미합니다.",
            'korean_meaning': vocab_item['korean_meaning'],
            'show_hiragana': show_hiragana
        }
    
    def _generate_sentence_completion_question(self, grammar_item: Dict, show_hiragana: bool) -> Dict:
        """Generate a sentence completion question"""
        sentence = grammar_item['japanese_sentence']
        pattern = grammar_item['grammar_pattern']
        korean_translation = grammar_item['korean_translation']
        
        # Create a sentence with blank where the pattern should be
        sentence_with_blank = sentence.replace(pattern, '____')
        
        # Get wrong grammar patterns
        wrong_answers = self._get_similar_grammar_patterns(grammar_item)
        
        # Create options
        options = self._create_options(pattern, wrong_answers)
        correct_index = options.index(pattern)
        
        question_text = f"다음 문장의 빈 칸에 들어갈 알맞은 문법을 선택하세요:"
        
        if show_hiragana:
            hiragana_reading = grammar_item.get('hiragana_reading', '')
            # Hide the grammar pattern in the hiragana reading
            hidden_hiragana_reading = self._hide_grammar_pattern_in_hiragana(hiragana_reading, pattern)
            display_text = f"{sentence_with_blank}\n({hidden_hiragana_reading})"
        else:
            display_text = sentence_with_blank
            
        return {
            'id': f"grammar_completion_{hash(str(grammar_item))}",
            'type': 'grammar',
            'category': 'sentence_completion',
            'level': 'N4',
            'difficulty': grammar_item.get('difficulty', 1),
            'question_text': question_text,
            'display_text': display_text,
            'options': options,
            'correct_answer': correct_index,
            'explanation': f"정답은 '{pattern}'입니다. 전체 문장: {sentence}\n의미: {korean_translation}",
            'korean_meaning': korean_translation,
            'show_hiragana': show_hiragana
        }
    
    def _generate_meaning_comprehension_question(self, grammar_item: Dict, show_hiragana: bool) -> Dict:
        """Generate a meaning comprehension question"""
        sentence = grammar_item['japanese_sentence']
        correct_answer = grammar_item['korean_translation']
        
        # Get wrong translations
        wrong_answers = self._get_similar_translations(grammar_item)
        
        # Create options
        options = self._create_options(correct_answer, wrong_answers)
        correct_index = options.index(correct_answer)
        
        question_text = f"다음 일본어 문장의 올바른 한국어 뜻을 선택하세요:"
        
        if show_hiragana:
            hiragana_reading = grammar_item.get('hiragana_reading', '')
            # For meaning comprehension, DON'T hide the pattern - it doesn't reveal the answer
            display_text = f"{sentence}\n({hiragana_reading})"
        else:
            display_text = sentence
            
        return {
            'id': f"grammar_meaning_{hash(str(grammar_item))}",
            'type': 'grammar',
            'category': 'meaning_comprehension',
            'level': 'N4',
            'difficulty': grammar_item.get('difficulty', 1),
            'question_text': question_text,
            'display_text': display_text,
            'options': options,
            'correct_answer': correct_index,
            'explanation': f"'{sentence}'는 '{correct_answer}'을(를) 의미합니다.",
            'korean_meaning': correct_answer,
            'show_hiragana': show_hiragana
        }
    
    def _generate_pattern_identification_question(self, grammar_item: Dict, show_hiragana: bool) -> Dict:
        """Generate a pattern identification question"""
        sentence = grammar_item['japanese_sentence']
        correct_pattern = grammar_item['grammar_pattern']
        korean_translation = grammar_item['korean_translation']
        
        # Get wrong grammar patterns
        wrong_answers = self._get_similar_grammar_patterns(grammar_item)
        
        # Create options
        options = self._create_options(correct_pattern, wrong_answers)
        correct_index = options.index(correct_pattern)
        
        question_text = f"다음 문장에서 사용된 문법 패턴을 선택하세요:"
        
        if show_hiragana:
            hiragana_reading = grammar_item.get('hiragana_reading', '')
            # Hide grammar pattern if it exists in the hiragana reading
            if correct_pattern:
                hidden_hiragana_reading = self._hide_grammar_pattern_in_hiragana(hiragana_reading, correct_pattern)
                display_text = f"{sentence}\n({hidden_hiragana_reading})"
            else:
                display_text = f"{sentence}\n({hiragana_reading})"
        else:
            display_text = sentence
            
        return {
            'id': f"grammar_pattern_{hash(str(grammar_item))}",
            'type': 'grammar',
            'category': 'pattern_identification',
            'level': 'N4',
            'difficulty': grammar_item.get('difficulty', 1),
            'question_text': question_text,
            'display_text': display_text,
            'options': options,
            'correct_answer': correct_index,
            'explanation': f"문장에서 사용된 문법은 '{correct_pattern}'입니다.\n의미: {korean_translation}",
            'korean_meaning': korean_translation,
            'show_hiragana': show_hiragana
        }
    
    def _get_similar_readings(self, correct_reading: str, pos: str) -> List[str]:
        """Get similar hiragana readings for wrong options"""
        # This is a simplified version - in a real implementation, 
        # you'd want more sophisticated logic
        similar_readings = [
            'あい', 'こい', 'めい', 'らい', 'きょう', 'じょう', 'せい', 'かい',
            'だん', 'ぜん', 'しん', 'きん', 'ほん', 'にち', 'がつ', 'つき'
        ]
        
        # Remove the correct reading and return 3 random ones
        available = [r for r in similar_readings if r != correct_reading]
        return random.sample(available, min(3, len(available)))
    
    def _get_similar_vocabulary_items(self, vocab_item: Dict, show_hiragana: bool) -> List[str]:
        """Get similar vocabulary items for wrong options"""
        try:
            all_vocab = self.csv_loader.load_vocabulary('N4')
            # Get items with same part of speech but different meaning
            similar_items = [
                item for item in all_vocab 
                if item.get('pos') == vocab_item.get('pos') 
                and item['kanji'] != vocab_item['kanji']
            ]
            
            if len(similar_items) < 3:
                # If not enough similar items, use any different items
                similar_items = [
                    item for item in all_vocab 
                    if item['kanji'] != vocab_item['kanji']
                ]
            
            selected = random.sample(similar_items, min(3, len(similar_items)))
            
            if show_hiragana:
                result = []
                for item in selected:
                    hiragana = item['hiragana']
                    # Skip hiragana display if it's empty, NaN, or same as kanji
                    if (not hiragana or 
                        str(hiragana).lower() == 'nan' or 
                        hiragana == item['kanji']):
                        result.append(item['kanji'])
                    else:
                        # Hide hiragana with underscores in answer choices
                        hidden_hiragana = self._hide_hiragana_with_underscores(hiragana)
                        result.append(f"{item['kanji']}({hidden_hiragana})")
                return result
            else:
                return [item['kanji'] for item in selected]
                
        except Exception:
            # Fallback to generic options
            if show_hiragana:
                return ['愛(___)', '相手(____)', '間(___)']
            else:
                return ['愛', '相手', '間']
    
    def _get_similar_meanings(self, vocab_item: Dict) -> List[str]:
        """Get similar Korean meanings for wrong options"""
        try:
            all_vocab = self.csv_loader.load_vocabulary('N4')
            different_meanings = [
                item['korean_meaning'] for item in all_vocab 
                if item['korean_meaning'] != vocab_item['korean_meaning']
            ]
            
            return random.sample(different_meanings, min(3, len(different_meanings)))
        except Exception:
            # Fallback to generic meanings
            return ['사랑', '상대방', '시간', '친구']
    
    def _get_similar_grammar_patterns(self, grammar_item: Dict) -> List[str]:
        """Get similar grammar patterns for wrong options"""
        # Common N4 grammar patterns
        patterns = [
            'てしまう', 'ている', 'た', 'てある', 'てみる', 'てくる', 'ていく',
            'たことがある', 'たり', 'ながら', 'とき', 'まえに', 'あとで'
        ]
        
        correct_pattern = grammar_item['grammar_pattern']
        available = [p for p in patterns if p != correct_pattern]
        return random.sample(available, min(3, len(available)))
    
    def _get_similar_translations(self, grammar_item: Dict) -> List[str]:
        """Get similar Korean translations for wrong options"""
        try:
            all_grammar = self.csv_loader.load_grammar('N4')
            different_translations = [
                item['korean_translation'] for item in all_grammar 
                if item['korean_translation'] != grammar_item['korean_translation']
            ]
            
            return random.sample(different_translations, min(3, len(different_translations)))
        except Exception:
            # Fallback translations
            return [
                '사랑을 잃어버렸습니다.',
                '친구를 만났습니다.',
                '학교에 갔습니다.',
                '음식을 먹었습니다.'
            ]
    
    def _create_options(self, correct_answer: str, wrong_answers: List[str]) -> List[str]:
        """Create shuffled multiple choice options"""
        # Ensure we have exactly 3 wrong answers
        while len(wrong_answers) < 3:
            wrong_answers.append(f"옵션 {len(wrong_answers) + 1}")
        
        wrong_answers = wrong_answers[:3]  # Take only first 3
        
        # Combine and shuffle
        all_options = [correct_answer] + wrong_answers
        random.shuffle(all_options)
        
        return all_options