import logging
import os

import RPi.GPIO as GPIO

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


class GpioConfig:
    """
    Gpio configuration for the SelfyBox
    """
    BUTTON_PIN = int(os.getenv('BUTTON_PIN'))
    LED_PIN = int(os.getenv('LED_PIN'))

    @classmethod
    def set_up(cls):
        """
        Create an inital configuration for the selfpiboy
        """
        logging.info('Begin GPIO configuration')
        # Setup GPIO (Input/Output of the Raspberry PI)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(cls.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(cls.LED_PIN, GPIO.OUT, initial=GPIO.LOW)
        logging.info('GPIO configured')
