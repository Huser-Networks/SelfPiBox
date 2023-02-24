import logging
import os
import time
from datetime import datetime

from src.config.gpio_config import GpioConfig
from src.config.screen_config import ScreenConfig
from src.handlers.wlan import Wlan


class SelfyConfig:
    """
    Class for the global configuration of the SelfyBox
    """
    # Path used
    SCRIPT_PATH = str(os.getcwd())
    IMAGE_FOLDER = 'selfies'
    EVENT_FOLDER = 'event'
    EVENT_IMAGE = SCRIPT_PATH + '/assets/background/event.png'
    LOG_FOLDER = 'logs/'

    @classmethod
    def set_up(cls, with_gpio: bool = True, with_pygame: bool = True):
        """
        Create an initial configuration for the selfpiboy
        """
        # Setup Logging
        logging.basicConfig(filename=cls.LOG_FOLDER + 'SelfPiBox.log', level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s')

        logging.info('Starting SelfPiBox')
        logging.info('Begin the configuration')

        # configure the WLAN by setting up an AP if no WLAN connection exists
        Wlan.configure_wlan()

        # Setup GPIO (Input/Output of the Raspberry PI)
        if with_gpio:
            GpioConfig.set_up()

        # Setup PyGame (
        if with_pygame:
            ScreenConfig.set_up()

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
    def generate_image_path(cls):
        """
        static method to generate the path to the newly created image
        :return str: the new image path
        """
        return os.path.join(
            cls.SCRIPT_PATH,
            cls.IMAGE_FOLDER,
            cls.EVENT_FOLDER,
            str(datetime.fromtimestamp(time.time())) + ".jpeg"
        )
