from decorator import singleton
from helper import load_data, save_data, parse
from settings import DATABASE


@singleton
class DataSet:
    def __init__(self):
        self.data = {}

    def load(self):
        self.data = load_data(DATABASE)

    def save(self):
        save_data(self.data, self.source)


@singleton
class InputOption:
    def setup(self, args):
        attrs = parse(args)
        self.__dict__.update(attrs)
