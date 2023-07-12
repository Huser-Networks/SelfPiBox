import logging

import RPi.GPIO as GPIO
import picamera

from .screen import Screen
from ..config.camera_config import CameraConfig
from ..config.gpio_config import GpioConfig
from ..config.selfy_config import SelfyConfig


class Camera:
    """
    Class containing all the function related to the SelfyBox Camera
    """
    @classmethod
    def start_camera(cls):
        """
        We create the camera instance for preparing taking the picture
        :return:
        """
        camera = picamera.PiCamera()

        # Initialise the camera object
        camera.resolution = (CameraConfig.IMAGE_WIDTH, CameraConfig.IMAGE_HEIGHT)
        camera.rotation = 0
        camera.vflip = False
        camera.hflip = False
        camera.awb_mode = 'auto'
        GPIO.output(GpioConfig.LED_PIN, GPIO.LOW)

        return camera

    @classmethod
    def take_picture(cls):
        """
        Full process for taking the picture
        """
        logging.debug("Taking picture")
        try:
            camera = cls.start_camera()
            Screen.start_countdown()

            image_path = SelfyConfig.generate_image_path()

            GPIO.output(GpioConfig.LED_PIN, GPIO.HIGH)
            camera.start_preview(fullscreen=True)

            camera.capture(image_path, format='jpeg', quality=100, thumbnail=(64, 48, 35))
            GPIO.output(GpioConfig.LED_PIN, GPIO.LOW)
            camera.stop_preview()
            camera.close()

            # display image
            Screen.display_image(image_path)
            logging.info("Picture Taken")
            logging.info(image_path)

        except Exception as e:
            logging.error("Picture was not taken due to some error")
            logging.error(e)
