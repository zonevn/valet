import importlib
import os
import sys


def is_match(command, list_commands):
    return command in list_commands


def fetch_command(command):
    commands = os.listdir(os.path.join(os.path.dirname(__file__), 'commands'))
    assert is_match('.'.join([command, 'py']), commands), "{} not matched".format(command)
    module = importlib.import_module('commands.{}'.format(command))
    return module.Command()


def main():
    try:
        sub_command = sys.argv[1]
    except IndexError:
        sub_command = 'help'

    command = fetch_command(sub_command)  # type:BaseCommand
    command.run(sys.argv)


if __name__ == '__main__':
    main()
