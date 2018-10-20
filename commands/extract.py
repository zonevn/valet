import argparse

import requests
from lxml import html

from base import BaseCommand


class Command(BaseCommand):
    desc = ''

    def add_args(self, parser: argparse.ArgumentParser):
        parser.add_argument('url')
        parser.add_argument('-attr', '--attribute')

    def handle(self, *args, **kwargs):
        url = kwargs.pop('url')
        attr = kwargs.pop('attribute')
        response = requests.get(url)
        tree = html.fromstring(response.content)

        extracts = tree.xpath(attr)
        for line in extracts:
            print(line)
