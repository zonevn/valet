import argparse
import os
import subprocess

import requests
from lxml import html

from base import BaseCommand
from settings import ROOT_DIR


class Command(BaseCommand):

    def add_args(self, parser: argparse.ArgumentParser):
        parser.add_argument('url')
        parser.add_argument('-a', '--attr')
        parser.add_argument('-o', '--outfile')

    def handle(self, *args, **kwargs):
        url = kwargs.pop('url')
        attr = kwargs.pop('attr')
        outfile = kwargs.pop('outfile')

        response = requests.get(url)
        tree = html.fromstring(response.content)

        extracts = tree.xpath(attr)

        # remove break line in list
        extracts = map(lambda s: s.strip(), extracts)

        # remove empty elements in list
        extracts = filter(None, extracts)

        # save to outfile
        outfile = '/'.join([ROOT_DIR, 'download', outfile])
        fopen = open(outfile, 'w', encoding='utf-8')
        fopen.writelines([each + '\n' for each in extracts])
        fopen.close()

        # open notepad++ with outfile
        subprocess.run(["C:/Program Files (x86)/Notepad++/notepad++.exe", outfile])
