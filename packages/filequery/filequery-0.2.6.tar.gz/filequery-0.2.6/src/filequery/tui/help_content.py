help_md = """\
# Help

controls

|key|action|
|---|------|
|ctrl+c|quit|
|f2|toggle help screen|
|f9|execute SQL in the editor|
|ctrl+q|save editor content|
|ctrl+r|save result|
|ctrl+p|close all open dialogs (help screen, save file dialogs)|
|ctrl+n|open a new tab|
|ctrl+shift+arrow keys|navigate panes|
|left or right arrow|switch tabs (must have the tab section focused to use this, i.e. press `ctrl+shift+up` until the tab section at the top of the screen is focused)|

---

editor controls

|key|action|
|---|------|
|escape|focus on the next item|
|up|move the cursor up|
|down|move the cursor down|
|left|move the cursor left|
|ctrl+left|move the cursor to the start of the word|
|ctrl+shift+left|move the cursor to the start of the word and select|
|right|move the cursor right|
|ctrl+right|move the cursor to the end of the word|
|ctrl+shift+right|move the cursor to the end of the word and select|
|home,ctrl+a|move the cursor to the start of the line|
|end,ctrl+e|move the cursor to the end of the line|
|shift+home|move the cursor to the start of the line and select|
|shift+end|move the cursor to the end of the line and select|
|pageup|move the cursor one page up|
|pagedown|move the cursor one page down|
|shift+up|select while moving the cursor up|
|shift+down|select while moving the cursor down|
|shift+left|select while moving the cursor left|
|shift+right|select while moving the cursor right|
|backspace|delete character to the left of cursor|
|ctrl+w|delete from cursor to start of the word|
|delete,ctrl+d|delete character to the right of cursor|
|ctrl+f|delete from cursor to end of the word|
|ctrl+x|delete the current line|
|ctrl+u|delete from cursor to the start of the line|
|ctrl+k|delete from cursor to the end of the line|
|f6|select the current line|
|f7|select all text in the document|

---

When you navigate to the table list on the left side, press `space` or `enter` to expand/collapse table columns.

---

helpful SQL statements

```sql
show tables; # list tables in the database
describe table <table name>; # get information about the columns in a table
```
"""
