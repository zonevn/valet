import os
import sys

if __name__ == '__main__':
    commands = os.listdir(os.path.join(os.path.dirname(__file__), 'commands'))
    commands = [each.replace('.py', '') for each in commands]
    print(commands.__contains__('newfile'))
