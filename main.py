import requests
import argparse

from src.dumper.itexamanswers import Itexamanswers
from src.searcher import Searcher
from src.shortcut import Shortcut

def get_html_from_url(url):
    res = requests.get(url)
    return res.content

def get_html_from_file(path):
    with open(path) as f:
        return f.read()

def main():
    description = 'Read the question from the clipboard and replace it with the answer.'
    usage = '%(prog)s [-h] [[--get-dump] [[--from-url] [--site SITE] [--url] [--output-path PATH] | [--from-file] [--path PATH] [--site SITE] [--output-path PATH]]] | [[--start] [--dump PATH]]'
    argparser = argparse.ArgumentParser(description=description, usage=usage)

    argparser.add_argument('--get-dump', action='store_true', help='Read and scrape HTML content, save formatted questions/answers to a JSON file')
    argparser.add_argument('--from-url', action='store_true')
    argparser.add_argument('--site', help='supported site name: [itexamanswers]')
    argparser.add_argument('--url', help='URL to the questions/answers page')
    argparser.add_argument('--from-file', action='store_true')
    argparser.add_argument('--path', help='path to the file where HTML content is stored')
    argparser.add_argument('--output-path', help='Path where to save JSON output')

    argparser.add_argument('--start', action='store_true')
    argparser.add_argument('--dump-path', help='path to the JSON file')


    args = argparser.parse_args()
    if args.get_dump == True:
        if args.from_url == True:
            if args.site == 'itexamanswers':
                html = get_html_from_url(args.url)
                itexamanswers_dumper = Itexamanswers(html)
                itexamanswers_dumper.parse()
                itexamanswers_dumper.save_in(args.output_path)
        
        elif args.from_file == True:
            if args.site == 'itexamanswers':
                html = get_html_from_file(args.path)
                itexamanswers_dumper = Itexamanswers(html)
                itexamanswers_dumper.parse()
                itexamanswers_dumper.save_in(args.output_path)

    elif args.start == True:
        searcher = Searcher(args.dump_path)
        searcher.load_dump()
        Shortcut(searcher)


if __name__ == '__main__':
    main()
