#!/usr/bin/env python

import time
from threading import Thread

from code.Camera import Camera
from code.Configuration import Configuration
from code.UserInterface import UserInterface


def main(threadName, *args):
    Configuration.set_up(with_gpio=False, with_pygame=True)
    UserInterface.display_image(file=Configuration.EVENT_IMAGE)
    while True:
        Camera.wait_for_event()
        UserInterface.display_image(file=Configuration.EVENT_IMAGE)
        time.sleep(0.2)
        Camera.take_picture()


# launch the main thread
Thread(target=main, args=('Main', 1)).start()
