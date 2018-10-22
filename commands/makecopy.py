import argparse
import os

from base import BaseCommand
from helper import find_path


class Command(BaseCommand):
    def add_args(self, parser: argparse.ArgumentParser):
        parser.add_argument('-name', '--filename')
        parser.add_argument('origin')
        parser.add_argument('-at', '--path', default='')

    def handle(self, *args, **kwargs):
        clone = kwargs.pop('filename')
        origin = kwargs.pop('origin')
        pkg = kwargs.pop('path')

        path = find_path(pkg)
        assert os.path.join(path, origin), 'Original file not found at {}'.format(origin)

        scripts = self.read_scripts(os.path.join(path, origin))
        self.write_scripts(os.path.join(path, clone), scripts)

    def read_scripts(self, db):
        fopen = open(db, 'r')
        scripts = fopen.readlines()
        fopen.close()
        return scripts

    def write_scripts(self, db, scripts):
        fopen = open(db, 'w')
        fopen.writelines(scripts)
        fopen.close()
