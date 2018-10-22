import argparse
import os

from base import BaseCommand
from helper import find_path


class Command(BaseCommand):
    def add_args(self, parser: argparse.ArgumentParser):
        parser.add_argument('filename')
        parser.add_argument('-at', '--path', default='')

    def handle(self, *args, **kwargs):
        filename = kwargs.pop('filename')
        package = kwargs.pop('path')
        path = find_path(package)

        open(os.path.join(path, filename), 'w').close()
