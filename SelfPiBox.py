#!/usr/bin/env python

from threading import Thread

from code.Configuration import Configuration
from code.UserInterface import UserInterface


def main(threadName, *args):
    Configuration.set_up(with_gpio=False, with_pygame=False)
    UserInterface.display_image(file=Configuration.EVENT_IMAGE)
    UserInterface.run_self_pi_box()

# launch the main thread
Thread(target=main, args=('Main', 1)).start()
