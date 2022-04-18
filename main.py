import requests
import argparse

from src.dumper.itexamanswers import Itexamanswers

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


if __name__ == '__main__':
    main()
