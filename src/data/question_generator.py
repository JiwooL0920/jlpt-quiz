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
        
        # Add missing critical patterns that were causing failures
        elif grammar_pattern == 'に対して':
            if 'にたいして' in result:
                hidden = '_' * len('にたいして')
                result = result.replace('にたいして', hidden)
                
        elif grammar_pattern == 'が必要':
            if 'がひつよう' in result:
                hidden = '_' * len('がひつよう')
                result = result.replace('がひつよう', hidden)
                
        elif grammar_pattern == 'というのは':
            if 'というのは' in result:
                hidden = '_' * len('というのは')
                result = result.replace('というのは', hidden)
                
        elif grammar_pattern == 'によって':
            if 'によって' in result:
                hidden = '_' * len('によって')
                result = result.replace('によって', hidden)
                
        elif grammar_pattern == 'について':
            if 'について' in result:
                hidden = '_' * len('について')
                result = result.replace('について', hidden)
        
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

    def _hide_grammar_pattern_in_kanji(self, japanese_sentence: str, grammar_pattern: str) -> str:
        """Hide the grammar pattern within Japanese sentence with underscores"""
        if not japanese_sentence or not grammar_pattern:
            return japanese_sentence
            
        # First try direct replacement
        if grammar_pattern in japanese_sentence:
            pattern_hidden = '____'
            return japanese_sentence.replace(grammar_pattern, pattern_hidden)
        
        result = japanese_sentence
        
        # Handle common pattern mappings between pattern name and actual kanji/hiragana in sentence
        
        # Direct hiragana patterns
        hiragana_patterns = {
            'てしまう': ['てしまいます', 'てしまいました', 'てしまった', 'てしまって', 'てしまう'],
            'ておく': ['ておきます', 'ておきました', 'ておいた', 'ておいて', 'ておく', 'ておこう'],
            'てみる': ['てみます', 'てみました', 'てみた', 'てみて', 'てみる', 'てみよう'],
            'てくる': ['てきます', 'てきました', 'てきた', 'てきて', 'てくる'],
            'ていく': ['ていきます', 'ていきました', 'ていった', 'ていって', 'ていく'],
            'てある': ['てあります', 'てありました', 'てあった', 'てあって', 'てある'],
            'ていた': ['ています', 'ていました', 'ていた', 'ていて'],
            'がする': ['がします', 'がしました', 'がした', 'がして', 'がする'],
            'がる': ['がります', 'がりました', 'がった', 'がって', 'がる'],
            'すぎる': ['すぎます', 'すぎました', 'すぎた', 'すぎて', 'すぎる'],
            'やすい': ['やすい'],
            'にくい': ['にくい'],
            'らしい': ['らしい', 'らしく', 'らしかった'],
            'みたいだ': ['みたい', 'みたいな', 'みたいに', 'みたいです', 'みたいだった'],
            'ようだ': ['ような', 'ように', 'ようです', 'ようだった'],
            'そうだ（様態）': ['そう', 'そうな', 'そうに', 'そうです', 'そうだった'],
            'そうだ（推測）': ['そう', 'そうです', 'そうだった'],
            'だろう': ['だろう', 'でしょう'],
            'かもしれない': ['かもしれない', 'かもしれません'],
            'はずだ': ['はず', 'はずです', 'はずだった'],
            'つもりだ': ['つもり', 'つもりです', 'つもりだった'],
            'べきだ': ['べき', 'べきです', 'べきだった'],
            'なら': ['なら', 'ならば'],
            'でも': ['でも'],
            'ながら': ['ながら'],
            'だけで': ['だけで'],
            'しかない': ['しかない', 'しかありません'],
            'てほしい': ['てほしい', 'てほしがる'],
            'とき': ['とき', 'ときは', 'ときに'],
            'のに（逆接）': ['のに'],
            'によって': ['によって', 'により'],
            'ずに': ['ずに', 'ないで'],
            'なる': ['なります', 'なりました', 'なった', 'なって', 'なる'],
            'たとえても': ['たとえ'],
        }
        
        # Kanji-based patterns that need special handling
        kanji_patterns = {
            'ために（目的）': ['ために'],
            'ために（原因）': ['ために'],
            'について': ['について'],  
            'にとって': ['にとって'],
            'に関して': ['に関して'],
            'に関する': ['に関する'],
            'に比べて': ['に比べて'],
            'を通して': ['を通して'],
            'ように（目的）': ['ように'],
            'ように（様態）': ['ように'],
            'のように': ['のように', 'ように'],
            'と思う': ['と思う', 'と思います', 'と思った', 'と思って'],
            'と言う': ['と言う', 'と言います', 'と言った', 'と言って', 'という'],
            'ことにする': ['ことにする', 'ことにします', 'ことにした'],
            'ことになる': ['ことになる', 'ことになります', 'ことになった'],
            'ことがある': ['ことがある', 'ことがあります', 'ことがあった'],
            'ことができる': ['ことができる', 'ことができます', 'ことができた', 'ことができません'],
            'ものだ': ['もの', 'ものです', 'ものだった'],
            'わけだ': ['わけ', 'わけです', 'わけだった'],
            'わけではない': ['わけではない', 'わけじゃない', 'わけではありません', 'わけじゃありません'],
            'はずだ': ['はず', 'はずです', 'はずだった'],
            'あまりない': ['あまり'],
            'ばかり': ['ばかり'],
            '予定だ': ['予定', '予定です', '予定だった'],
            'ようになる': ['ようになる', 'ようになります', 'ようになった'],
            '始める': ['始める', '始めます', '始めた', '始めて'],
            '終わる': ['終わる', '終わります', '終わった', '終わって'],
            '続ける': ['続ける', '続けます', '続けた', '続けて'],
            '出す': ['出す', '出します', '出した', '出して'],
            'ば（仮定）': ['ば', 'れば', 'せば', 'けば', 'げば', 'べば', 'めば', 'てば', 'ねば', 'えば'],
        }
        
        # Try hiragana patterns first
        if grammar_pattern in hiragana_patterns:
            for variant in hiragana_patterns[grammar_pattern]:
                if variant in result:
                    result = result.replace(variant, '____')
                    break
        
        # Try kanji patterns
        elif grammar_pattern in kanji_patterns:
            for variant in kanji_patterns[grammar_pattern]:
                if variant in result:
                    result = result.replace(variant, '____')
                    break
        
        # If no direct match found, try the pattern itself
        elif grammar_pattern in result:
            result = result.replace(grammar_pattern, '____')
        
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
    
    def _detect_and_fix_corrupted_data(self, grammar_item: Dict) -> Dict:
        """Detect and fix corrupted data where Korean text is in Japanese field"""
        import re
        
        def contains_korean(text):
            """Check if text contains Korean characters"""
            if not text:
                return False
            korean_pattern = re.compile(r'[\uac00-\ud7af]')
            return bool(korean_pattern.search(str(text)))
        
        def convert_hiragana_to_kanji_sentence(hiragana_text):
            """Convert hiragana text to a basic Japanese sentence format
            This is a fallback when the Japanese field is corrupted"""
            if not hiragana_text:
                return hiragana_text
            
            # For now, just return the hiragana as-is since we can't reliably convert to kanji
            # In a real fix, we'd need a proper hiragana-to-kanji conversion dictionary
            return hiragana_text
        
        # Create a copy to avoid modifying the original
        fixed_item = grammar_item.copy()
        
        japanese_sentence = fixed_item.get('japanese_sentence', '')
        hiragana_reading = fixed_item.get('hiragana_reading', '')
        
        # Check if Japanese sentence field contains Korean
        if contains_korean(japanese_sentence):
            # The hiragana field usually contains the correct Japanese text
            if hiragana_reading and not contains_korean(hiragana_reading):
                # Use the hiragana as the Japanese sentence
                # This is better than showing Korean text
                fixed_item['japanese_sentence'] = convert_hiragana_to_kanji_sentence(hiragana_reading)
                
                # Log the fix for debugging
                # print(f"Fixed corrupted entry: {grammar_item.get('grammar_pattern', '')} - replaced Korean with hiragana")
            else:
                # Both fields are corrupted or hiragana is missing
                # As a last resort, generate a placeholder
                pattern = fixed_item.get('grammar_pattern', '')
                fixed_item['japanese_sentence'] = f"[Example with {pattern}]"
                fixed_item['hiragana_reading'] = f"[Example with {pattern}]"
        
        return fixed_item

    def generate_grammar_question(self, grammar_item: Dict, show_hiragana: bool = False) -> Dict:
        """Generate a grammar question from a grammar item"""
        # Fix corrupted data before processing
        grammar_item = self._detect_and_fix_corrupted_data(grammar_item)
        
        question_type = grammar_item['question_type']
        
        # ONLY ALLOW meaning_comprehension questions for reading comprehension
        # Remove both sentence_completion AND pattern_identification (they both show blanks)
        if question_type == 'meaning_comprehension':
            return self._generate_meaning_comprehension_question(grammar_item, show_hiragana)
        else:
            # Skip sentence_completion, pattern_identification, and any other types
            raise ValueError(f"Question type {question_type} is not supported (only meaning comprehension allowed)")
    
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
            
        # For reading questions, get Korean meanings for each hiragana option
        option_translations = []
        all_vocab = self.csv_loader.load_vocabulary('N4')
        
        # First pass: collect all translation data
        translation_data = []
        for option in options:
            # Find the Korean meaning for this hiragana reading
            for vocab_item_lookup in all_vocab:
                if vocab_item_lookup['hiragana'] == option:
                    # Format as: kanji (hiragana) - korean
                    translation_data.append((vocab_item_lookup['kanji'], option, vocab_item_lookup['korean_meaning']))
                    break
            else:
                # Fallback if not found
                translation_data.append(('', option, ''))
        
        # Second pass: format with proper alignment
        option_translations = self._format_aligned_translations(translation_data)

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
            'show_hiragana': show_hiragana,
            'option_translations': option_translations  # Add translations for all options
        }
    
    def _align_kanji_hiragana_options(self, options_data: List[tuple]) -> List[str]:
        """Align kanji-hiragana options with consistent parentheses positioning using proper Japanese character display width
        
        Args:
            options_data: List of tuples [(kanji, hiragana), ...]
        
        Returns:
            List of formatted strings with aligned parentheses
        """
        if not options_data:
            return []
            
        # Find the maximum display width for kanji column (with safety check)
        kanji_widths = [self._get_display_width(kanji) for kanji, _ in options_data if kanji]
        max_kanji_display_width = max(kanji_widths) if kanji_widths else 0
        
        # Format each option with proper alignment
        aligned_options = []
        for kanji, hiragana in options_data:
            if not hiragana or hiragana.strip() == '':  # Handle empty hiragana
                aligned_options.append(kanji)
            else:
                # Calculate spaces needed to align kanji column
                kanji_display_width = self._get_display_width(kanji)
                kanji_padding = max_kanji_display_width - kanji_display_width
                
                # Format: "kanji  (hiragana)" with proper spacing
                kanji_part = kanji + " " * (kanji_padding + 2)  # +2 for base spacing
                aligned_options.append(f"{kanji_part}({hiragana})")
        
        return aligned_options

    def _get_display_width(self, text: str) -> int:
        """Calculate the display width of text considering Japanese characters
        
        Japanese characters (kanji, hiragana, katakana) typically take 2 character widths
        in monospace fonts, while ASCII characters take 1 character width.
        """
        if not text:
            return 0
            
        width = 0
        for char in text:
            # Check if character is Japanese (kanji, hiragana, katakana)
            if '\u3040' <= char <= '\u309F' or '\u30A0' <= char <= '\u30FF' or '\u4E00' <= char <= '\u9FAF':
                width += 2  # Japanese characters are double-width
            else:
                width += 1  # ASCII and other characters are single-width
        return width

    def _format_aligned_translations(self, translation_data: List[tuple]) -> List[str]:
        """Format vocabulary translations with proper column alignment
        
        Args:
            translation_data: List of tuples [(kanji, hiragana, korean), ...]
        
        Returns:
            List of formatted strings with aligned columns for kanji, hiragana, and korean
        """
        if not translation_data:
            return []
            
        # Find maximum display widths for each column (with safety checks)
        kanji_widths = [self._get_display_width(kanji) for kanji, _, _ in translation_data if kanji]
        hiragana_widths = [self._get_display_width(hiragana) for _, hiragana, _ in translation_data if hiragana]
        
        max_kanji_display_width = max(kanji_widths) if kanji_widths else 0
        max_hiragana_display_width = max(hiragana_widths) if hiragana_widths else 0
        
        # Format each translation with proper alignment
        aligned_translations = []
        for kanji, hiragana, korean in translation_data:
            # Skip entries with critical missing data
            if not kanji or not korean:
                continue
                
            # Build the formatted string with proper spacing (no dash, even spacing)
            if hiragana:
                # Calculate spaces needed to align kanji column
                kanji_display_width = self._get_display_width(kanji)
                kanji_padding = max_kanji_display_width - kanji_display_width
                
                # Calculate spaces needed to align hiragana column  
                hiragana_with_parens = f"({hiragana})"
                hiragana_display_width = self._get_display_width(hiragana_with_parens)
                hiragana_padding = max_hiragana_display_width + 2 - hiragana_display_width  # +2 for parentheses
                
                # Format: "kanji    (hiragana)    korean" (no dash, even spacing)
                kanji_part = kanji + " " * (kanji_padding + 4)  # +4 for base spacing
                hiragana_part = hiragana_with_parens + " " * (hiragana_padding + 4)  # +4 for spacing before korean
                formatted_line = f"{kanji_part}{hiragana_part}{korean}"
            else:
                # Format: "kanji                  korean" (no hiragana, no dash)
                kanji_display_width = self._get_display_width(kanji)
                kanji_padding = max_kanji_display_width - kanji_display_width
                # Add spacing equivalent to hiragana column width + spacing
                total_spacing = kanji_padding + 4 + max_hiragana_display_width + 2 + 4  # kanji_pad + base + hiragana + parens + korean_spacing
                formatted_line = f"{kanji}" + " " * total_spacing + f"{korean}"
            
            aligned_translations.append(formatted_line)
        
        return aligned_translations

    def _format_reading_comprehension_translations(self, translation_data: List[tuple]) -> List[str]:
        """Format reading comprehension translations with 3-line layout per option
        
        Args:
            translation_data: List of tuples [(korean_translation, japanese_sentence, hiragana_reading), ...]
        
        Returns:
            List of formatted strings with 3-line layout:
            • japanese_sentence
              hiragana_reading
              korean_translation
        """
        if not translation_data:
            return []
            
        formatted_translations = []
        for korean_translation, japanese_sentence, hiragana_reading in translation_data:
            if not korean_translation or not japanese_sentence:
                continue
                
            # Format each option as 3 lines:
            # Line 1: • japanese_sentence  
            # Line 2:     hiragana_reading (indented to align under japanese text, not bullet)
            # Line 3:     korean_translation (same indentation as hiragana)
            
            lines = []
            lines.append(f"• {japanese_sentence}")
            
            if hiragana_reading and hiragana_reading.strip():
                lines.append(f"    {hiragana_reading}")  # 4 spaces to align under japanese text
            else:
                lines.append("    ")  # Empty line to maintain spacing
                
            lines.append(f"    {korean_translation}")  # 4 spaces to match hiragana indentation
            
            # Join the 3 lines for this option
            formatted_translations.append("\n".join(lines))
        
        return formatted_translations

    def _generate_meaning_to_japanese_question(self, vocab_item: Dict, show_hiragana: bool) -> Dict:
        """Generate a meaning to Japanese question (Korean meaning -> Japanese)"""
        kanji = vocab_item['kanji']
        hiragana = vocab_item['hiragana']
        korean_meaning = vocab_item['korean_meaning']
        
        if (not show_hiragana or 
            not hiragana or 
            str(hiragana).lower() == 'nan' or 
            hiragana == kanji):
            # Kanji only mode
            correct_answer = kanji
            wrong_answers = self._get_similar_vocabulary_items(vocab_item, show_hiragana)
            options = self._create_options(correct_answer, wrong_answers)
            correct_index = options.index(correct_answer)
        else:
            # Kanji + hiragana mode with alignment
            # Get wrong answer data (kanji, hiragana pairs)
            wrong_answers_data = self._get_similar_vocabulary_items_data(vocab_item)
            
            # Prepare all options data for alignment
            all_options_data = [(kanji, hiragana)] + wrong_answers_data
            
            # Create aligned options
            aligned_options = self._align_kanji_hiragana_options(all_options_data)
            
            # Shuffle and find correct index
            correct_answer = aligned_options[0]  # First one is the correct answer
            wrong_answers = aligned_options[1:]   # Rest are wrong answers
            options = self._create_options(correct_answer, wrong_answers)
            correct_index = options.index(correct_answer)
        
        question_text = f"다음 뜻에 해당하는 일본어를 선택하세요:"
        display_text = korean_meaning
            
        # For meaning-to-Japanese questions, generate translations for the actual Japanese options
        option_translations = []
        all_vocab = self.csv_loader.load_vocabulary('N4')
        
        # First pass: collect all translation data
        translation_data = []
        for option in options:
            # Extract the kanji part from options like "食べる(たべる)" -> "食べる"
            if '(' in option and ')' in option:
                kanji_part = option.split('(')[0].strip()
                # Extract hiragana from parentheses
                hiragana_part = option.split('(')[1].split(')')[0].strip()
            else:
                kanji_part = option.strip()
                hiragana_part = None
                
            # Find the Korean meaning for this Japanese term
            for vocab_item_lookup in all_vocab:
                if vocab_item_lookup['kanji'] == kanji_part:
                    # Use the hiragana from the option if available, otherwise from lookup
                    if hiragana_part:
                        translation_data.append((kanji_part, hiragana_part, vocab_item_lookup['korean_meaning']))
                    elif vocab_item_lookup.get('hiragana') and str(vocab_item_lookup['hiragana']).lower() != 'nan':
                        translation_data.append((kanji_part, vocab_item_lookup['hiragana'], vocab_item_lookup['korean_meaning']))
                    else:
                        translation_data.append((kanji_part, '', vocab_item_lookup['korean_meaning']))
                    break
            else:
                # Fallback if not found
                translation_data.append((option, '', ''))
        
        # Second pass: format with proper alignment
        option_translations = self._format_aligned_translations(translation_data)

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
            'show_hiragana': show_hiragana,
            'option_translations': option_translations  # Add translations for all options
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
        
        # For Japanese-to-meaning questions, get the Japanese terms for each Korean meaning option
        # This will be used to show all translations in feedback
        option_translations = []
        all_vocab = self.csv_loader.load_vocabulary('N4')
        
        # First pass: collect all translation data
        translation_data = []
        for option in options:
            # Find the Japanese term that corresponds to this Korean meaning
            for vocab_item_lookup in all_vocab:
                if vocab_item_lookup['korean_meaning'] == option:
                    # Format as: kanji (hiragana) - korean
                    hiragana_display = vocab_item_lookup.get('hiragana', '')
                    if hiragana_display and str(hiragana_display).lower() != 'nan':
                        translation_data.append((vocab_item_lookup['kanji'], hiragana_display, vocab_item_lookup['korean_meaning']))
                    else:
                        translation_data.append((vocab_item_lookup['kanji'], '', vocab_item_lookup['korean_meaning']))
                    break
            else:
                # Fallback if not found
                translation_data.append(('', '', option))
        
        # Second pass: format with proper alignment
        option_translations = self._format_aligned_translations(translation_data)
        
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
            'show_hiragana': show_hiragana,
            'option_translations': option_translations  # Add translations for all options
        }
    
    def _force_add_blanks_if_missing(self, sentence: str, pattern: str, hiragana: str = None) -> tuple:
        """Emergency fallback to ensure blanks are added when pattern hiding fails"""
        
        def add_emergency_blanks(text, target_pattern):
            """Add blanks using multiple strategies"""
            if not text or not target_pattern:
                return text
            
            # Strategy 1: Direct pattern replacement 
            if target_pattern in text:
                return text.replace(target_pattern, '____')
            
            # Strategy 2: Look for pattern parts in compound words/conjugations
            if len(target_pattern) >= 2:
                # For patterns like 始める, look for 始め in compounds like 咲き始めました
                pattern_stem = target_pattern[:-1] if target_pattern.endswith('る') else target_pattern[:2]
                if pattern_stem in text:
                    # Find the full word containing this stem
                    import re
                    # Look for the pattern stem plus some characters
                    match = re.search(f'{pattern_stem}[^。、\\s]*', text)
                    if match:
                        return text.replace(match.group(), '____')
            
            # Strategy 3: If pattern appears in hiragana but not kanji, use positional replacement
            if hiragana and target_pattern not in text:
                # Find approximate position in sentence
                words = text.split()
                if len(words) >= 2:
                    # Replace middle part as fallback
                    middle_idx = len(words) // 2
                    words[middle_idx] = '____'
                    return ''.join(words)
            
            return text
        
        # Check if blanks already exist
        if '____' in sentence or '___' in sentence:
            kanji_result = sentence
        else:
            kanji_result = add_emergency_blanks(sentence, pattern)
        
        # Handle hiragana if provided
        hiragana_result = hiragana
        if hiragana:
            if '____' not in hiragana and '___' not in hiragana and '_' not in hiragana:
                hiragana_result = add_emergency_blanks(hiragana, pattern)
        
        return kanji_result, hiragana_result

    def _generate_sentence_completion_question(self, grammar_item: Dict, show_hiragana: bool) -> Dict:
        """Generate a sentence completion question with guaranteed blanks"""
        sentence = grammar_item['japanese_sentence']
        pattern = grammar_item['grammar_pattern']
        korean_translation = grammar_item['korean_translation']
        hiragana_reading = grammar_item.get('hiragana_reading', '')
        
        # PATTERN REPLACEMENT WITH CONJUGATIONS: Handle common conjugated forms
        def add_blanks_with_conjugations(text, target_pattern):
            """Replace pattern accounting for common conjugations"""
            if not text or not target_pattern:
                return text
            
            # Method 1: Direct replacement (59% of cases)
            if target_pattern in text:
                return text.replace(target_pattern, '____')
            
            # Method 2: Try common conjugations for the remaining 41%
            import re
            conjugations = []
            
            # Common conjugation patterns with more comprehensive coverage
            if target_pattern.endswith('う'):
                # てしまう -> てしまいます, てしまった, てしまいました
                base = target_pattern[:-1]
                conjugations.extend([
                    base + 'います', base + 'いました', base + 'った', 
                    base + 'って', base + 'わない', base + 'おう'
                ])
            elif target_pattern.endswith('く'):
                # ておく -> ておきます, ておきました, ておいた, ておいて
                base = target_pattern[:-1]
                conjugations.extend([
                    base + 'きます', base + 'きました', base + 'いた', 
                    base + 'いて', base + 'かない', base + 'こう'
                ])
            elif target_pattern.endswith('る'):
                # 始める -> 始めます, 始めました, 始めた, 始めて
                # てみる -> てみます, てみました, てみた, てみて
                # 終わる -> 終わります, 終わりました, 終わった, 終わって
                base = target_pattern[:-1] 
                conjugations.extend([
                    base + 'ます', base + 'ました', base + 'た', 
                    base + 'て', base + 'ない', base + 'よう'
                ])
            elif target_pattern.endswith('だ'):
                # 予定だ -> 予定です, 予定でした, 予定の
                base = target_pattern[:-1]
                conjugations.extend([
                    base + 'です', base + 'でした', base + 'だった',
                    base + 'の', base + 'な'
                ])
            
            # Try each standard conjugation first
            for conj in conjugations:
                if conj in text:
                    return text.replace(conj, '____')
            
            # Handle special compound patterns that need precise targeting
            # Use more specific matching to avoid over-blanking
            if target_pattern == 'あまりない':
                # Look for あまり followed by negative forms
                patterns_to_try = [
                    'あまり.*?ません', 'あまり.*?ないです', 'あまり.*?くない', 'あまり.*?くありません'
                ]
                for pattern in patterns_to_try:
                    matches = list(re.finditer(pattern, text))
                    if matches:
                        match = matches[0]  # Take first match
                        start, end = match.span()
                        return text[:start] + '____' + text[end:]
            
            elif target_pattern in ['そうだ（推測）', 'そうだ（様態）']:
                # Look for そうです/そうだ at the end
                if text.endswith('そうです。'):
                    return text.replace('そうです', '____')
                elif text.endswith('そうですね。'):
                    return text.replace('そうですね', '____')
                elif text.endswith('そうだ。'):
                    return text.replace('そうだ', '____')
                # Look for そう + adjective pattern
                elif 'そうです' in text:
                    return text.replace('そうです', '____')
                elif 'そうだ' in text:
                    return text.replace('そうだ', '____')
            
            elif target_pattern == 'みたいだ':
                if text.endswith('みたいです。'):
                    return text.replace('みたいです', '____')
                elif text.endswith('みたいですね。'):
                    return text.replace('みたいですね', '____')
                elif 'みたいに' in text:
                    return text.replace('みたいに', '____')
                elif 'みたいな' in text:
                    return text.replace('みたいな', '____')
                elif 'みたいです' in text:
                    return text.replace('みたいです', '____')
            
            elif target_pattern == 'かもしれない':
                if text.endswith('かもしれません。'):
                    return text.replace('かもしれません', '____')
                elif text.endswith('かもしれない。'):
                    return text.replace('かもしれない', '____')
                elif 'かもしれません' in text:
                    return text.replace('かもしれません', '____')
                elif 'かもしれない' in text:
                    return text.replace('かもしれない', '____')
            
            elif target_pattern in ['ために（目的）', 'ために（原因）']:
                if 'ために' in text:
                    return text.replace('ために', '____')
                elif 'ため' in text:
                    return text.replace('ため', '____')
            
            elif target_pattern in ['ように（目的）', 'ように（様態）']:
                if 'ように' in text:
                    return text.replace('ように', '____')
                elif 'よう' in text and ('に' in text or 'な' in text):
                    # More precise matching for よう patterns
                    if 'ような' in text:
                        return text.replace('ような', '____')
                    elif 'ように' in text:
                        return text.replace('ように', '____')
            
            elif target_pattern == 'ことができる':
                if 'ことができます' in text:
                    return text.replace('ことができます', '____')
                elif 'ことができません' in text:
                    return text.replace('ことができません', '____')
                elif 'ことが出来る' in text:
                    return text.replace('ことが出来る', '____')
                elif 'ことができる' in text:
                    return text.replace('ことができる', '____')
            
            elif target_pattern == 'ことにする':
                if 'ことにしました' in text:
                    return text.replace('ことにしました', '____')
                elif 'ことにします' in text:
                    return text.replace('ことにします', '____')
                elif 'ことにしています' in text:
                    return text.replace('ことにしています', '____')
                elif 'ことにする' in text:
                    return text.replace('ことにする', '____')
            
            elif target_pattern == 'ことになる':
                if 'ことになりました' in text:
                    return text.replace('ことになりました', '____')
                elif 'ことになります' in text:
                    return text.replace('ことになります', '____')
                elif 'ことになる' in text:
                    return text.replace('ことになる', '____')
            
            elif target_pattern == 'ことがある':
                if 'ことがあります' in text:
                    return text.replace('ことがあります', '____')
                elif 'ことがありません' in text:
                    return text.replace('ことがありません', '____')
                elif 'ことがある' in text:
                    return text.replace('ことがある', '____')
            
            elif target_pattern == 'わけではない':
                if 'わけではありません' in text:
                    return text.replace('わけではありません', '____')
                elif 'わけではない' in text:
                    return text.replace('わけではない', '____')
                elif '訳ではない' in text:
                    return text.replace('訳ではない', '____')
            
            elif target_pattern == 'と思う':
                if 'と思います' in text:
                    return text.replace('と思います', '____')
                elif 'と思いません' in text:
                    return text.replace('と思いません', '____')
                elif 'と思う' in text:
                    return text.replace('と思う', '____')
            
            elif target_pattern == 'たとえても':
                # Look for たとえ...ても pattern
                match = re.search(r'たとえ.+?ても', text)
                if match:
                    start, end = match.span()
                    return text[:start] + '____' + text[end:]
                match = re.search(r'たとえ.+?でも', text)
                if match:
                    start, end = match.span()
                    return text[:start] + '____' + text[end:]
            
            elif target_pattern == 'しかない':
                if 'しかありません' in text:
                    return text.replace('しかありません', '____')
                elif 'しかない' in text:
                    return text.replace('しかない', '____')
                elif 'するしか' in text:
                    return text.replace('するしか', '____')
                # Look for ...するしか pattern
                match = re.search(r'.+?するしか', text)
                if match:
                    start, end = match.span()
                    return text[:start] + '____' + text[end:]
            
            elif target_pattern == 'ようになる':
                if 'ようになりました' in text:
                    return text.replace('ようになりました', '____')
                elif 'ようになります' in text:
                    return text.replace('ようになります', '____')
                elif 'ようになる' in text:
                    return text.replace('ようになる', '____')
            
            elif target_pattern == 'によって':
                if 'によって' in text:
                    return text.replace('によって', '____')
                elif 'による' in text:
                    return text.replace('による', '____')
                elif 'により' in text:
                    return text.replace('により', '____')
            
            elif target_pattern == 'でしょう':
                if 'でしょう' in text:
                    return text.replace('でしょう', '____')
            
            elif target_pattern == 'が必要':
                if 'が必要' in text:
                    return text.replace('が必要', '____')
            
            # Method 3: Smart partial matching for compound words
            if target_pattern:
                # For patterns like 始める, 終わる, look for the base in compound verbs
                if target_pattern.endswith('る'):
                    base_verb = target_pattern[:-1]
                    # Look for compounds like 読み終わる, 食べ終わる
                    compound_pattern = f'.+?{base_verb}[^。]*?'
                    matches = list(re.finditer(compound_pattern, text))
                    if matches:
                        match = matches[0]  # Take first match
                        matched_text = match.group()
                        # Replace just the compound verb part
                        verb_start = matched_text.find(base_verb)
                        if verb_start >= 0:
                            before = text[:match.start() + verb_start]
                            # Find a good ending point (not too much)
                            after_start = match.start() + verb_start + len(base_verb)
                            # Look for next 2-3 characters or until punctuation
                            end_pos = min(after_start + 3, len(text))
                            for i in range(after_start, min(after_start + 6, len(text))):
                                if text[i] in '。、！？':
                                    end_pos = i
                                    break
                            after = text[end_pos:]
                            return before + '____' + after
                
                # Try exact substring matching with context preservation
                for i in range(len(target_pattern), 1, -1):
                    pattern_part = target_pattern[:i]
                    if pattern_part in text and len(pattern_part) >= 2:
                        # Find the position and replace with context
                        idx = text.find(pattern_part)
                        if idx >= 0:
                            # Preserve some surrounding context
                            start = max(0, idx - 1) if idx > 0 else idx
                            end = min(len(text), idx + len(pattern_part) + 2)
                            # Make sure we don't replace the entire sentence
                            if end - start < len(text) * 0.6:  # Don't replace more than 60% of sentence
                                return text[:start] + '____' + text[end:]
            
            # Final fallback: ONLY replace a small middle section if no pattern found
            # This prevents complete sentence blanking
            if len(text) > 12:
                # Replace a small portion in the middle (max 25% of sentence)
                max_replacement = min(len(text) // 4, 5)
                middle_start = len(text) // 2 - max_replacement // 2
                middle_end = middle_start + max_replacement
                return text[:middle_start] + '____' + text[middle_end:]
            elif len(text) > 6:
                # For medium sentences, replace just 2-3 characters in middle
                middle = len(text) // 2
                return text[:middle-1] + '____' + text[middle+2:]
            
            # If text is short, just add blanks at the end
            return text[:-1] + '____'
        
        # Process kanji sentence
        sentence_with_blank = add_blanks_with_conjugations(sentence, pattern)
        
        # Process hiragana if needed
        hidden_hiragana_reading = ''
        if show_hiragana and hiragana_reading:
            hidden_hiragana_reading = add_blanks_with_conjugations(hiragana_reading, pattern)
        
        # Get wrong grammar patterns
        wrong_answers = self._get_similar_grammar_patterns(grammar_item)
        
        # Create options
        options = self._create_options(pattern, wrong_answers)
        correct_index = options.index(pattern)
        
        question_text = f"다음 문장의 빈 칸에 들어갈 알맞은 문법을 선택하세요:"
        
        if show_hiragana:
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
        
        # For reading comprehension questions, get the Japanese sentences for each Korean translation option
        option_translations = []
        all_grammar = self.csv_loader.load_grammar('N4')
        
        # First pass: collect all translation data
        translation_data = []
        for option in options:
            # Find the Japanese sentence that corresponds to this Korean translation
            for grammar_item_lookup in all_grammar:
                if grammar_item_lookup['korean_translation'] == option:
                    japanese_sentence = grammar_item_lookup['japanese_sentence']
                    hiragana_reading_lookup = grammar_item_lookup.get('hiragana_reading', '')
                    
                    # Store data as tuple: (korean_translation, japanese_sentence, hiragana_reading)
                    translation_data.append((option, japanese_sentence, hiragana_reading_lookup))
                    break
            else:
                # Fallback if not found - skip this option
                translation_data.append((option, '', ''))
        
        # Second pass: format with 3-line layout
        option_translations = self._format_reading_comprehension_translations(translation_data)
            
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
            'show_hiragana': show_hiragana,
            'option_translations': option_translations  # Add translations for all options
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
    
    def _get_similar_vocabulary_items_data(self, vocab_item: Dict) -> List[tuple]:
        """Get similar vocabulary items as (kanji, hiragana) tuples for alignment"""
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
            
            result = []
            for item in selected:
                hiragana = item['hiragana']
                # Skip hiragana display if it's empty, NaN, or same as kanji
                if (not hiragana or 
                    str(hiragana).lower() == 'nan' or 
                    hiragana == item['kanji']):
                    result.append((item['kanji'], ''))  # Empty hiragana will be handled
                else:
                    result.append((item['kanji'], hiragana))
            return result
                
        except Exception:
            # Fallback to generic options
            return [('相手', 'あいて'), ('間', 'ま'), ('愛', 'あい')]

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
                        # Note: This method is kept for backward compatibility
                        # New alignment logic is in _get_similar_vocabulary_items_data
                        result.append(f"{item['kanji']}({hiragana})")
                return result
            else:
                return [item['kanji'] for item in selected]
                
        except Exception:
            # Fallback to generic options
            if show_hiragana:
                return ["愛(あい)", "相手(あいて)", "間(ま)"]
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