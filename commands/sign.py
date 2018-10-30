import argparse
import os
import subprocess

import pyautogui as robot
from base import BaseCommand
from settings import APP_DIRS, FILE_DIRS


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        list_file = [f for f in os.listdir(FILE_DIRS['checkparams']) if
                     os.path.isfile(os.path.join(FILE_DIRS['checkparams'], f))]
        try:
            for f in list_file:
                if 'kiem_tra' in f:
                    self.sign_pdf(f)
        except KeyboardInterrupt as e:
            print('Interrupted.')
            exit()

    def sign_pdf(self, filename, delay=robot.MINIMUM_SLEEP):
        subprocess.call([APP_DIRS['pdf'], os.path.join(FILE_DIRS['checkparams'], filename)])
        robot.hotkey('ctrl', 'e', pause=delay)
        robot.mouseDown(x=600, y=510, pause=delay)
        robot.moveRel(300, 80, pause=delay)
        robot.mouseUp()
        robot.press('del', pause=delay)
        robot.hotkey('ctrl', 'u', pause=delay)
        robot.click(x=672, y=492, pause=delay)
        robot.click(x=772, y=584, clicks=2, interval=0.25)
        robot.hotkey('ctrl', 's', pause=delay)
        robot.hotkey('ctrl', 'w', pause=delay)
