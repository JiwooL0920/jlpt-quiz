# 🎌 JLPT Quiz - Stream Deck Setup Guide

## 📱 Adding JLPT Quiz to Stream Deck

### Method 1: Open App Action
1. **Open Stream Deck software**
2. **Drag "Open" action** from the System category to an empty key
3. **Browse for app**: Click "Choose App" 
4. **Navigate to**: `release/JLPT_QUIZ.app`
5. **Select the app** and click "Choose"
6. **Customize**:
   - Title: `JLPT Quiz`
   - Icon: Use the default or upload custom icon
7. **Click "OK"** to save

### Method 2: System App Action  
1. **Drag "System" action** to Stream Deck key
2. **Set Action**: "Open Application"
3. **Choose App**: Browse to `JLPT Quiz.app`
4. **Configure title and icon**

## 🎯 Quick Launch Options

### Launch Modes:
- **Default**: `JLPT Quiz.app` (opens main menu)
- **Quick Demo**: Add terminal action with `cd /path/to/project && make demo`
- **Validation**: Add terminal action with `./JLPT\ Quiz.app/Contents/MacOS/JLPT\ Quiz --validate`

## 🔧 Troubleshooting

**App won't launch from Stream Deck:**
1. Right-click the app → "Open" (first time security approval)
2. Go to System Preferences → Security & Privacy → "Allow Anyway"
3. Try launching from Stream Deck again

**App not found:**
- Make sure `JLPT Quiz.app` is in the Applications folder or accessible path
- Use full path: `/Users/[username]/path/to/JLPT Quiz.app`

## 🎨 Custom Icon Ideas
- Japanese flag (🇯🇵)
- Kanji character (日)
- Quiz/education icon
- Custom image (512x512px recommended)

## 📍 App Location
```
/Users/jiwoolee/Project/jlpt-quiz/release/JLPT Quiz.app
```

Move to `/Applications/` for easier access:
```bash
cp -r "release/JLPT Quiz.app" /Applications/
```