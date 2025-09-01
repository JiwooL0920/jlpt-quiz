"""Settings management for JLPT Quiz Application"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

class Settings:
    """Manages persistent user settings for JLPT Quiz"""
    
    def __init__(self):
        self.config_dir = Path.home() / '.jlpt-quiz'
        self.config_file = self.config_dir / 'settings.json'
        self._settings = self._load_settings()
    
    def _load_settings(self) -> Dict[str, Any]:
        """Load settings from file or return defaults"""
        default_settings = {
            'level': 'N4',
            'hiragana_display': True,  # True = kanji + hiragana, False = kanji only
            'feedback_mode': 'immediate',  # 'immediate' or 'deferred'
        }
        
        if not self.config_file.exists():
            return default_settings
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                loaded_settings = json.load(f)
                # Merge with defaults to ensure all keys exist
                return {**default_settings, **loaded_settings}
        except (json.JSONDecodeError, IOError):
            return default_settings
    
    def _save_settings(self):
        """Save settings to file"""
        # Ensure config directory exists
        self.config_dir.mkdir(exist_ok=True)
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self._settings, f, indent=2, ensure_ascii=False)
        except IOError:
            pass  # Fail silently if can't save
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value"""
        return self._settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set setting value and save"""
        self._settings[key] = value
        self._save_settings()
    
    def get_level(self) -> str:
        """Get current JLPT level"""
        return self._settings['level']
    
    def set_level(self, level: str):
        """Set JLPT level"""
        self.set('level', level)
    
    def get_hiragana_display(self) -> bool:
        """Get hiragana display preference"""
        return self._settings['hiragana_display']
    
    def set_hiragana_display(self, show_hiragana: bool):
        """Set hiragana display preference"""
        self.set('hiragana_display', show_hiragana)
    
    def get_feedback_mode(self) -> str:
        """Get feedback mode preference"""
        return self._settings['feedback_mode']
    
    def set_feedback_mode(self, mode: str):
        """Set feedback mode preference ('immediate' or 'deferred')"""
        if mode in ['immediate', 'deferred']:
            self.set('feedback_mode', mode)
    
    def get_hiragana_display_text(self) -> str:
        """Get human-readable hiragana display setting"""
        return "한자 + 히라가나" if self._settings['hiragana_display'] else "한자만"
    
    def get_feedback_mode_text(self) -> str:
        """Get human-readable feedback mode setting"""
        return "즉시 피드백" if self._settings['feedback_mode'] == 'immediate' else "마지막에 일괄 피드백"