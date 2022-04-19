Get question's answer from dumps without leaving your page.

## Install
- Install requirements:
	`python -m pip install -r requirements.txt`

## How to use
### Dumper
Get your dump file before you start using. E.g.:
```
python main.py \
	--get-dump \
	--from-url \
	--site itexamanswers \
	--url "https://itexamanswers.net/ccna-1-v7-0-final-exam-answers-full-introduction-to-networks.html" \
	--output-path "D:\itexamansers_ccna-2-v7-0.json"
```

**Notes:**
- Only ITExamsAnswers is supported.
- Some questions or answers may be skipped or incomplete. Feel free to check your output and fill missing by hand.

### Run
Run script with selected dump. E.g.:
```
python main.py \
	--start \
	--dump-path "D:\itexamansers_ccna-2-v7-0.json"
```
Script will now listen your key. 
- Select and copy the question
- Hit <kbd>S</kbd> key to search
  - Answer is set to your clipboard
  - Or multiple answers is set to your clipboard, separated with "//"
  - Or your clipboard is set with "*No result found*"
  - Or your clipboard is set with "*No answer found*"
  - Or your clipboard is set with "*Too many results found*"
- Exit with <kbd>F10</kbd>

#### Example
Select question > <kbd>Ctrl+C</kbd> > <kbd>S</kbd> > <kbd>Ctrl+F</kbd> > <kbd>Ctrl+V</kbd>
![example](https://i.imgur.com/DLx48Kc.gif)
