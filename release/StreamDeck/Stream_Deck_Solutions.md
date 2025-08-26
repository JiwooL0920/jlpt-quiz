# 🎮 Stream Deck Troubleshooting Guide

## If JLPT_QUIZ.app doesn't work in Stream Deck:

### ✅ Solution 1: Use Shell Script
Stream Deck sometimes works better with shell scripts:

1. **In Stream Deck**: Use "Open" action
2. **Choose file**: `release/launch-jlpt-quiz.sh` 
3. **This should work more reliably**

### ✅ Solution 2: Terminal Command
If both apps fail, use "System: Command Line" action:

1. **Action**: System → Command Line
2. **Command**: 
   ```bash
   /Users/jiwoolee/Project/jlpt-quiz/release/launch-jlpt-quiz.sh
   ```

### ✅ Solution 3: AppleScript Direct
Create custom AppleScript action:

1. **Action**: System → AppleScript
2. **Script**:
   ```applescript
   tell application "iTerm"
       activate
       create window with default profile
       tell current session of current window
           write text "clear && '/Users/jiwoolee/Project/jlpt-quiz/release/JLPT-Quiz'"
       end tell
   end tell
   ```

### 🔧 Troubleshooting Permissions

If Stream Deck shows permission errors:

1. **System Preferences** → Security & Privacy → Privacy
2. **Accessibility** → Add Stream Deck app
3. **Automation** → Allow Stream Deck to control iTerm2
4. **Full Disk Access** → Add Stream Deck (if needed)

### 📁 Files to Try (in order):
1. `launch-jlpt-quiz.sh` (recommended)
2. `JLPT_QUIZ.app` 
3. Use AppleScript method above

### 💡 Why This Happens:
- Stream Deck runs in sandbox mode
- AppleScript permissions can be restricted
- Shell scripts often work better than app bundles