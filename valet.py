import argparse
import importlib

from library import DataSet, InputOption
from settings import ACTIONS


def main():
    # try:
        parser = argparse.ArgumentParser(prog='tutorial')
        parser.add_argument('command', help='Command helper', choices=ACTIONS)
        parser.add_argument('-d', '--data', help='data helper', nargs='*')
        parser.add_argument('-r', '--remember', action='store_true', help='data helper')
        args = parser.parse_args()

        dataset = DataSet()
        dataset.load()

        ins = InputOption()
        ins.setup(args.data)

        module = importlib.import_module('actions')
        action = getattr(module, args.command)
        action()

        if args.remember:
            dataset.save()

    # except Exception as e:
    #     print('Error: ', e)
    #     parser.print_help()


if __name__ == '__main__':
    main()
