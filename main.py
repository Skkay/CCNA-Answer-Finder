import requests
from src.dumper.itexamanswers import Itexamanswers

def get_html_from_url(url):
    res = requests.get(url)
    return res.content

def get_html_from_file(path):
    with open(path) as f:
        return f.read()

def main():
    # html = get_html_from_url('https://itexamanswers.net/ccna-2-v7-0-final-exam-answers-full-switching-routing-and-wireless-essentials.html')
    html = get_html_from_file('./page.html')
    itexamanswers_dumper = Itexamanswers(html)
    itexamanswers_dumper.parse()
    itexamanswers_dumper.save_in('./dump/itexamansers_ccna-2-v7-0.json')


if __name__ == '__main__':
    main()
