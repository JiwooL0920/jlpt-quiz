#!/bin/bash
# Simple launcher that runs 'make run' from project directory

osascript -e '
tell application "iTerm"
    activate
    create window with default profile
    tell current session of current window
        write text "clear && echo \"🎌 JLPT Quiz - Starting...\" && cd \"/Users/jiwoolee/Project/jlpt-quiz\" && make run"
    end tell
end tell
'