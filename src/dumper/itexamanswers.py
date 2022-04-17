import json
from bs4 import BeautifulSoup

class Itexamanswers():
    def __init__(self, raw_html) -> None:
        self.raw_html = raw_html
        self.parsed_data = []

    def parse(self) -> None:
        soup = BeautifulSoup(self.raw_html, 'html.parser')

        div = soup.find('div', {'class': 'thecontent clearfix'})
        questions_answers = div.find_all(recursive=False)

        question_flag = False
        for element in questions_answers:
            if element.name == 'p' and (element.find('strong') or element.find('b')):
                question_flag = True

                question = element.find('strong') if element.find('strong') else element.find('b')
                # print(question)
                self.parsed_data.append({
                    'question': question.string,
                    'corrects': [],
                    'wrongs': []
                })

            if question_flag and element.name == 'ul':
                question_flag = False

                answers = element.find_all('li')
                for answer_element in answers:
                    if len(answer_element.find_all()) == 0: # Wrong answer
                        self.parsed_data[-1]['wrongs'].append(answer_element.string)

                    else:
                        self.parsed_data[-1]['corrects'].append(answer_element.string)

    def save_in(self, output_path: str, file_mode='w', indent=4) -> None:
        with open(output_path, file_mode) as f:
            json.dump(self.parsed_data, f, indent=indent)
