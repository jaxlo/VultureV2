from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np
import h5py
import image_manipulation as im

def main(train_imgs, train_ans, test_imgs, test_ans):
	'''
	#setup.... have imported from other program that deals with images
	train_imgs = np.array([])
	train_ans = []
	test_imgs = np.array([])
	test_ans = []
	'''
	#converts list of integers to binary class matrix
	train_ans = keras.utils.to_categorical(train_ans, num_classes = 4)#need to change num classes
	test_ans = keras.utils.to_categorical(test_ans, num_classes = 4)

	#model....
	classifier = Sequential()

	#hidden layers (change input shape)-------------------------------
	classifier.add(Conv2D(32, (3, 3), activation = 'relu', input_shape = (64, 64, 3)))#3 means RGB, 1 for black and white
	classifier.add(MaxPooling2D(pool_size = (2,2)))
	model.add(Dropout(0.25))classifier.add(Conv2D(64, (3,3), activation = 'relu'))
	classifier.add(MaxPooling2D(pool_size = (2,2)))
	model.add(Dropout(0.25))

	classifier.add(Conv2D(128, (3,3), activation = 'relu'))
	classifier.add(MaxPooling2D(pool_size = (2,2)))
	model.add(Dropout(0.25))

	classifier.add(Conv2D(256, (3,3), activation = 'relu'))
	classifier.add(MaxPooling2D(pool_size = (2,2)))
	model.add(Dropout(0.25))
	#-----------------------------------------------------------------

	classifier.add(Flatten())
	classifier.add(Dense(1024, activation = 'relu'))
	classifier.add(Dense(units = 1, activation = 'sigmoid'))#change units to number of outputs

	#compile
	classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

	print(model.evaluate(x_test, y_test, batch_size=batch_size))

	classifer.save('trained_CNN_2020.h5')#will overwrite each time
