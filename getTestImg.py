#I don't think this version ran on the pi so you might have to deal with my sintax errors if you run it

try:
	from picamera import PiCamera
	picam = PiCamera()
	picam.resolution = (320,320)#run now to give it time to load
	camSupport = True
	print('Pi Camera Enabled')
except ImportError:
	camSupport = False
	print('Pi Camera Disabled')

import math
import time

from aiy.vision.leds import Leds
from aiy.vision.leds import Pattern
from aiy.vision.leds import PrivacyLed
from aiy.vision.leds import RgbLeds

RED = (0xFF, 0x00, 0x00)
GREEN = (0x00, 0xFF, 0x00)
YELLOW = (0xFF, 0xFF, 0x00)
BLUE = (0x00, 0x00, 0xFF)
PURPLE = (0xFF, 0x00, 0xFF)
CYAN = (0x00, 0xFF, 0xFF)
WHITE = (0xFF, 0xFF, 0xFF)

try:
    import aiy.toneplayer
    player = aiy.toneplayer.TonePlayer(22)#GPIO setup
except ImportError:
    buzzSupoort = False
    print('Buzzer Disabled')


def piCam(filepath, imgCounter):#filepath = None if it should make a random picture -- Example: piCam('/run/someDirectionForAName') -- (do not add .jpg)
	if filepath != None:
		currentImg = str(filepath)+str(imgCounter)+'.jpg'#adds image number and filepath
		picam.capture(currentImg)
		player.play('Be')
		print('Image :'+str(imgCounter)+' taken.')
		loadImg = Image.open(currentImg)
		cropImg = loadImg.crop((0, 140, 320, 320))
		pixels = np.array(cropImg.getdata(band=2), dtype=np.uint8)#only gets the blue band of the image
		pixels.resize(180,320)#makes it a 2D array
	else:
		print('Using a random image')
		pixels = np.random.rand(180,320)
		time.sleep(.5)#make it act more like the cam in speed
		print('Image :'+str(imgCounter)+' made.')
	return pixels



	def main():
		print('Starting (Blue)')
		leds.update(Leds.rgb_on(BLUE))
		name = input('Name: ')
		counter = 0
		while True:
			piCam(name, counter)
			count += 1



main()
