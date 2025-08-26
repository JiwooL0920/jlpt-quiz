#!/bin/bash
# Simple Stream Deck launcher for JLPT Quiz

cd "/Users/jiwoolee/Project/jlpt-quiz/release"

osascript -e '
tell application "iTerm"
    activate
    create window with default profile
    tell current session of current window
        write text "clear && echo \"🎌 JLPT Quiz - Stream Deck Launch\" && echo \"\" && \"/Users/jiwoolee/Project/jlpt-quiz/release/JLPT-Quiz\""
    end tell
end tell
'