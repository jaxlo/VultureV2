import numpy as np
import glob
import pickle
import os
from PIL import Image
import sys

#TODO anything related to loading or manipulating the images is done in this program


def loadImgs(filepath):
	
	train_imgs = np.array([])
	train_ans = []
	test_imgs = np.array([])
	test_ans = []
		
	imageFilepathSections = ('/forward', '/test')
	imageDirectoryFilepath = filepath
	appendCountTrain = 0
	appendCountTest = 0

	for folder in imageFilepathSections:
		currentFileFolder = (imageDirectoryFilepath+folder)#loops through each folder
		for pic in glob.glob(currentFileFolder+'/*.jpg'):
			loadImg = Image.open(pic)
			pixels = np.array(loadImg, dtype=np.float32)
			pixels /= 255 #makes it 0-1 and it is faster
			if folder != ('/test'):
				if appendCountTrain != 0:
					train_imgs = np.append(train_imgs, pixels)
				else:
					train_imgs = pixels
				if folder == '/forward': 
					train_ans += [0]
				elif folder == '/left': 
					train_ans += [1]
				appendCountTrain += 1

			if folder == ('/test'):
				if appendCountTest != 0:
					test_imgs = np.append(test_imgs, pixels)
				else:
					test_imgs = pixels
				if pic.find('forward') >= 0:
					test_ans += [0]
				elif pic.find('left') >= 0  or pic.find('Left') >= 0:
					test_ans += [1]
				appendCountTest += 1
				#put similar code here when finished with the train
		print('Loaded: '+folder.strip('/') +' Images')

	train_imgs.shape = (-1, 320, 180, 1)
	test_imgs.shape = (-1, 320, 180, 1)

	return train_imgs, train_ans, test_imgs, test_ans

def convertImg():
	filepathToConvert = '/run/media/jax/DualOS/CompSci/finalCar/mlTrain11-4-17/all/turnLeft/'
	filepathEnd = '/home/jax/Documents/BluescaleImages/turnLeft/'
	img_width, img_height = 180, 320

	os.chdir("/run/media/jax/DualOS/CompSci/finalCar/mlTrain11-4-17/all/turnLeft/")
	for file in glob.glob('*.jpg'):
		print(file)
		currentImg = (str(filepathToConvert)+str(file))
		loadImg = Image.open(currentImg)
		cropImg = loadImg.crop((0, 140, 320, 320))
		pixels = np.array(cropImg.getdata(band=1), dtype=np.uint8)#only gets the red band of the image
		pixels.resize(img_width, img_height)#makes it a 2D array
		im = Image.fromarray(pixels)
		im.save(filepathEnd+'blue'+file)
		print('One image converted')


def takeImg(filepath):
	imgCounter = 0
	img_width, img_height = 180, 320
	imgCounter += 1

	currentImg = str(filepath)+str(imgCounter)+'.jpg'#adds image number and filepath
	picam.capture(currentImg)
	loadImg = Image.open(currentImg)
	cropImg = loadImg.crop((0, 140, 320, 320))
	pixels = np.array(cropImg.getdata(band=1), dtype=np.uint8)#only gets the red band of the image
	pixels.resize(img_width, img_height)#makes it a 2D array

	return pixels


def startPi():

    import math
    import time
    from aiy.vision.leds import Leds
    from aiy.vision.leds import Pattern
    from aiy.vision.leds import PrivacyLed
    from aiy.vision.leds import RgbLeds

    RED = (0xFF, 0x00, 0x00)
    GREEN = (0x00, 0xFF, 0x00)
    BLUE = (0x00, 0x00, 0xFF)

    leds.update(Leds.rgb_on(BLUE))
    print('Starting...\n\n')

    while True:
        print('Taking a picture...')
        imageArray = takeImg('/home/pi/runningImages')
        ans = predict(imageArray, 320, 320)
        if ans == '':#TODO add values
            leds.update(Leds.rgb_on(RED))
            print('Stop sign found')
        elif == '':
            leds.update(Leds.rgb_on(RED))
            print('Stop sign found')
