import pyperclip
from pynput import keyboard
from src.searcher import Searcher

class Shortcut:
    def __init__(self, searcher: Searcher) -> None:
        self.searcher = searcher

        self.exit_key = keyboard.Key.f10
        self.search_key = keyboard.KeyCode.from_char('s')
        print(f'Exit key: {self.exit_key}. Search key: {self.search_key}')

        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()
    
    def on_release(self, key):
        if key == self.exit_key:
            return False
        
        if key == self.search_key:
            self.search()
    
    def search(self):
        clip = pyperclip.paste()
        results = self.searcher.search(clip)

        if len(results) == 0:
            self.set_clipboard('No result found')
        
        elif len(results) == 1:
            result = results[0]
            if len(result['corrects']) == 0:
                self.set_clipboard('No answer found')
            elif len(result['corrects']) == 1:
                self.set_clipboard(result['corrects'][0])
            else:
                self.set_clipboard(' // '.join(result['corrects']) + f' ({len(result["corrects"])})')
        
        else:
            self.set_clipboard('Too many results found')

    def set_clipboard(self, value):
        print(str(value))
        pyperclip.copy(str(value))
