import logging
import os

import RPi.GPIO as GPIO
import pygame


class Configuration():
    """
    Class for the global configuration of the SelfPiBox
    """
    # Path used
    SCRIPT_PATH = "/opt/SelfPiBox"
    IMAGE_FOLDER = 'selfies'
    EVENT_FOLDER = 'event'
    EVENT_IMAGE = '/opt/SelfPiBox/assets/background/event.png'
    LOG_FOLDER = 'logs/'

    # PIN button for your I/O commands
    BUTTON_PIN = 26
    LED_PIN = 13
    NIGHT_MODE_PIN = 21

    # Screen spec
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080

    # Image Spec
    IMAGE_WIDTH = 4056
    IMAGE_HEIGHT = 3040
    SCALE_WIDTH = 1440

    screen = None

    @classmethod
    def set_up(cls, with_gpio: bool = True, with_pygame: bool = True):
        """
        Create an inital configuration for the selfpiboy
        """
        # Setup Logging
        logging.basicConfig(filename=cls.LOG_FOLDER + 'SelfPiBox.log', level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)s %(message)s')

        logging.info('Starting SelfPiBox')
        logging.info('Begin the configuration')

        # Setup GPIO (Input/Output of the Raspberry PI)
        if with_gpio:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(cls.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(cls.LED_PIN, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(cls.NIGHT_MODE_PIN, GPIO.OUT, initial=GPIO.LOW)
            logging.info('GPIO configured')
        else:
            logging.info('GPIO configuration skipped')

        if with_pygame:
            # Setup PyGame (
            pygame.init()
            cls.screen = pygame.display.set_mode((cls.SCREEN_WIDTH, cls.SCREEN_HEIGHT), pygame.FULLSCREEN)
            pygame.mouse.set_visible(0)
            logging.info('pygame configured')
        else:
            logging.info('pygame configuration skipped')

        # check if the Image and Event folders exist and create one if they don't
        image_path = os.path.join(cls.SCRIPT_PATH, cls.IMAGE_FOLDER)
        if not os.path.isdir(image_path):
            os.makedirs(cls.IMAGE_FOLDER)

        event_path = os.path.join(image_path, cls.EVENT_FOLDER)
        if not os.path.isdir(event_path):
            os.makedirs(event_path)

        logging.info('Folder ' + event_path + ' ready.')
        logging.info('Configuration done')

    @classmethod
    def shutdown(cls):
        """
        Call this method for shutting down the SelfPiBox in a clean way
        """
        GPIO.cleanup()
        logging.debug('SelfPiBox stopped')
        exit()
