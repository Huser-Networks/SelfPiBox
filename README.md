# SelfPiBox
PhotoBooth for Party selfies with a Raspberry Pi and RPi Camera written in Python

## Prerequisite

`sudo apt install python3 python-is-python3 libsdl2-image-2.0-0`

## Installation
On a fresh new Raspberry Pi Os updated & upgraded no package installation is required. 

You have to activate Camera Interface running 

`sudo raspi-config`

Just clone the repo in the opt folder :

`cd /opt`

`sudo git clone https://github.com/R-Men/SelfPiBox.git`

Navigate into SelfPiBox folder freshly created and launch the script : 

`cd SelfPiBox`

`pip install -r requirements.txt`

`python main`

You can use the startup script to launch it at boot.

## Hardware 
A screen must be attached to the HDMI output

You will need a button on RPi Pin #26 and if wanted a LED on PIN #13

## Testing without screen attached
You can use `tightvncserver`as a virtual screen. Your screen must have a resolution of 1920x1080.

`tightvncserver -geometry 1920x1080`

## Testing on ssh with screen attached
Get the value of `echo $DISPLAY` on the raspberry (not from ssh)

On SSH type `export DISPLAY=<value>` and replace <value> with value of `echo $DISPLAY`

Launch `python main.py`

## Testing camera
You can test the camera by typing :
```python
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.stop_preview()
```
The camera will show the image for 10 seconds.

### Default Event Image 
[Original Flickr image](https://flic.kr/p/LhSZBG) of [event.png](assets/background/event.png) that was resized in 4:3. 
