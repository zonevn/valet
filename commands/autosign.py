import argparse
import os
import subprocess
import sys

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

    def sign_pdf(self, filename):
        try:
            proc = subprocess.Popen([APP_DIRS['pdf'], os.path.join(FILE_DIRS['checkparams'], filename)])
            proc.wait(10)
        finally:
            self._autorun(0.5)

    def _autorun(self, delay=robot.MINIMUM_SLEEP):
        robot.hotkey('ctrl', 'e', pause=delay)
        robot.mouseDown(x=600, y=540, pause=delay)
        robot.moveRel(300, 80, pause=delay)
        robot.mouseUp()
        robot.press('del', pause=delay)
        robot.hotkey('ctrl', 'u', pause=delay)
        robot.click(x=652, y=472, pause=delay)
        robot.click(x=772, y=584, clicks=2, interval=0.25)
        robot.hotkey('ctrl', 's', pause=delay)
        robot.hotkey('ctrl', 'w', pause=delay)
