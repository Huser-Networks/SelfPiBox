#!/usr/bin/env python

import picamera
import os
import time
import PIL.Image
import RPi.GPIO as GPIO
import logging
import pygame

from threading import Thread
from time import sleep
from PIL import Image, ImageDraw
from datetime import datetime

scriptPath = "/opt/SelfPiBox"
imageFolder = 'selfies'

logFolder = 'logs/'

countdown0 = '/opt/SelfPiBox/assets/countdown/0.png'
countdown1 = '/opt/SelfPiBox/assets/countdown/1.png'
countdown2 = '/opt/SelfPiBox/assets/countdown/2.png'
countdown3 = '/opt/SelfPiBox/assets/countdown/3.png'

eventFolder = 'event'
eventImage = '/opt/SelfPiBox/assets/background/event.png'

BUTTON_PIN = 26
LED_PIN = 13
NIGHTMODE_PIN = 21

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

IMAGE_WIDTH = 4056
IMAGE_HEIGHT = 3040

SCALE_WIDTH = 1440

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(NIGHTMODE_PIN, GPIO.OUT, initial=GPIO.LOW)

# logging
logging.basicConfig(filename=logFolder + 'SelfPiBox.log', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s')

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.mouse.set_visible(0)


def DisplayImage(file):
    img = pygame.image.load(file)
    img = pygame.transform.smoothscale(img, (SCALE_WIDTH, SCREEN_HEIGHT))
    screen.blit(img, ((SCREEN_WIDTH - SCALE_WIDTH) / 2, 0))
    pygame.display.flip()


def InitFolder():
    # check image folder existing, create if not exists
    imagePath = os.path.join(scriptPath, imageFolder)
    if not os.path.isdir(imagePath):
        os.makedirs(imageFolder)

    eventPath = os.path.join(imagePath, eventFolder)
    if not os.path.isdir(eventPath):
        os.makedirs(eventPath)

    logging.info('Folder ' + eventPath + ' ready.')


def WaitForEvent():
    global pygame
    NotEvent = True
    while NotEvent:
        input_state = GPIO.input(BUTTON_PIN)
        if input_state == False:
            NotEvent = False
            return
        time.sleep(1)


def TakePicture():
    try:
        ### Camera Start ###
        GPIO.output(LED_PIN, GPIO.HIGH)
        camera = picamera.PiCamera()

        # Initialise the camera object
        camera.resolution = (IMAGE_WIDTH, IMAGE_HEIGHT)
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

        GPIO.output(LED_PIN, GPIO.LOW)
        ### END - Camera Start ###

        # generate filename
        timeStamp = time.time()
        imagePath = os.path.join(scriptPath, imageFolder, eventFolder, str(datetime.fromtimestamp(timeStamp)) + ".jpeg")

        # blink 3 times and take picture
        GPIO.output(LED_PIN, GPIO.HIGH)
        DisplayImage(countdown3)
        sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(0.5)
        GPIO.output(LED_PIN, GPIO.HIGH)
        DisplayImage(countdown2)
        sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(0.5)
        GPIO.output(LED_PIN, GPIO.HIGH)
        DisplayImage(countdown1)
        sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(0.5)
        camera.start_preview(fullscreen=True)
        DisplayImage(countdown0)
        camera.capture(imagePath, format='jpeg', quality=100, thumbnail=(64, 48, 35))
        camera.stop_preview()
        camera.close()
        # display image
        DisplayImage(imagePath)

    finally:

        # logging.info(datetime.fromtimestamp(timestamp))
        logging.info('Picture taken!')
        logging.info(imagePath)


def main(threadName, *args):
    logging.debug('Starting SelfPiBox')
    InitFolder()
    DisplayImage(eventImage)
    while True:
        WaitForEvent()
        DisplayImage(eventImage)
        time.sleep(0.2)
        TakePicture()
    GPIO.cleanup()
    logging.debug('SelfPiBox stopped')


# launch the main thread
Thread(target=main, args=('Main', 1)).start()
