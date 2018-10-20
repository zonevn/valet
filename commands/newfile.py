import argparse

from base import BaseCommand


class Command(BaseCommand):
    def add_args(self, parser: argparse.ArgumentParser):
        parser.add_argument('file')

    def handle(self, *args, **kwargs):
        print("args: ", args, "kwargs: ", kwargs)
