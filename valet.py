import importlib
import os
import sys


def is_match(string, parrentstring):
    return string in parrentstring


def fetch_command(subcommand):
    commands = os.listdir(os.path.join(os.path.dirname(__file__), 'commands'))
    assert is_match('.'.join([subcommand, 'py']), commands), "{} not matched".format(subcommand)
    module = importlib.import_module('commands.{}'.format(subcommand))
    return module.Command()


def main():
    try:
        subcommand = sys.argv[1]
    except IndexError:
        subcommand = 'help'

    command = fetch_command(subcommand)  # type:BaseCommand
    command.run(sys.argv)


if __name__ == '__main__':
    main()
