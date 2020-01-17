import numpy as np
import nn3 as cnn
import image_manipulation as im

def main():
	#this will run everything in other programs based on user input
	choice = input('1: Train NN/n2: Run NN/nChoice [1/2]: ')

	#To train
	if int(choice) == 1:
		filepath = input('Filepath with training data: ')
		train_imgs, train_ans, test_imgs, test_ans = im.loadImgs(filepath)
		cnn.train(train_imgs, train_ans, test_imgs, test_ans)

	#To run
	elif int(choice) == 2:
		while True:
			img = im.takeImg()
			cnn.predict.pred(img, img_width, img_height)

	#To convert Images
	elif int(choice) == 3:
		im.convertImg()

	else:
		print('Invalid. Choose Again.')
		main()


main()
