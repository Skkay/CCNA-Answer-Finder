import json

class Searcher:
    def __init__(self, dump_path) -> None:
        self.dump_path = dump_path

    def load_dump(self) -> None:
        with open(self.dump_path) as f:
            self.dump = json.load(f)

    def search(self, question) -> list:
        found = []
        for object in self.dump:
            if isinstance(object['question'], str) and question in object['question']:
                found.append(object)
        
        return found
