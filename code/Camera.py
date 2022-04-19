import logging
import os
import time
from datetime import datetime

import RPi.GPIO as GPIO
import picamera

from .Configuration import Configuration
from .UserInterface import UserInterface


class Camera():

    COUNTDOWN_TIMER = [
        '/opt/SelfPiBox/assets/countdown/0.png',
        '/opt/SelfPiBox/assets/countdown/0.png',
        '/opt/SelfPiBox/assets/countdown/0.png',
        '/opt/SelfPiBox/assets/countdown/0.png'
    ]

    @classmethod
    def wait_for_event(cls):
        global pygame

        NotEvent = True
        while NotEvent:
            input_state = GPIO.input(Configuration.BUTTON_PIN)
            if input_state == False:
                NotEvent = False
                return
            time.sleep(1)

    @classmethod
    def take_picture(cls):
        try:
            ### Camera Start ###
            GPIO.output(Configuration.LED_PIN, GPIO.HIGH)
            camera = picamera.PiCamera()

            # Initialise the camera object
            camera.resolution = (Configuration.IMAGE_WIDTH, Configuration.IMAGE_HEIGHT)
            camera.rotation = 0
            camera.vflip = False
            camera.hflip = False
            # camera.brightness            = 50
            # camera.iso                   = 1500
            camera.awb_mode = 'auto'
            # camera.annotate_text         = 'Test Selfybox'
            # camera.annotate_foreground   = picamera.Color(y=128, u=0, v=0)
            # camera.annotate_background   = True
            # camera.annotate_text_size    = 32

            #        time.sleep(1) # Camera warm-up time

            GPIO.output(Configuration.LED_PIN, GPIO.LOW)
            ### END - Camera Start ###

            # generate filename
            time_stamp = time.time()
            image_path = os.path.join(Configuration.SCRIPT_PATH, Configuration.IMAGE_FOLDER, Configuration.EVENT_FOLDER,
                                     str(datetime.fromtimestamp(time_stamp)) + ".jpeg")

            # blink 3 times and take picture
            GPIO.output(Configuration.LED_PIN, GPIO.HIGH)
            UserInterface.display_image(cls.COUNTDOWN_TIMER[3])
            time.sleep(0.5)
            GPIO.output(Configuration.LED_PIN, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(Configuration.LED_PIN, GPIO.HIGH)
            UserInterface.display_image(cls.COUNTDOWN_TIMER[2])
            time.sleep(0.5)
            GPIO.output(Configuration.LED_PIN, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(Configuration.LED_PIN, GPIO.HIGH)
            UserInterface.display_image(cls.COUNTDOWN_TIMER[1])
            time.sleep(0.5)
            GPIO.output(Configuration.LED_PIN, GPIO.LOW)
            time.sleep(0.5)
            camera.start_preview(fullscreen=True)
            UserInterface.display_image(cls.COUNTDOWN_TIMER[0])
            camera.capture(image_path, format='jpeg', quality=100, thumbnail=(64, 48, 35))
            camera.stop_preview()
            camera.close()
            # display image
            UserInterface.display_image(image_path)

        finally:

            # logging.info(datetime.fromtimestamp(timestamp))
            logging.info('Picture taken!')
            logging.info(image_path)
