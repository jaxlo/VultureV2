from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np
import h5py

def train(train_imgs, train_ans, test_imgs, test_ans):
	batch_size = 50 #MAKE BIGGER (?)
	epochs = 10 #MAKE BIGGER (?)

	#converts list of integers to binary class matrix
	train_ans = keras.utils.to_categorical(train_ans, num_classes = 4)#need to change num classes
	test_ans = keras.utils.to_categorical(test_ans, num_classes = 4)

	#model....
	classifier = Sequential()

	#hidden layers (change input shape)-------------------------------
	classifier.add(Conv2D(32, (3, 3), activation = 'relu', input_shape = (64, 64, 3)))#3 means RGB, 1 for black and white
	classifier.add(MaxPooling2D(pool_size = (2,2)))
	classifier.add(Dropout(0.25))

	classifier.add(Conv2D(64, (3,3), activation = 'relu'))
	classifier.add(MaxPooling2D(pool_size = (2,2)))
	classifier.add(Dropout(0.25))

	classifier.add(Conv2D(128, (3,3), activation = 'relu'))
	classifier.add(MaxPooling2D(pool_size = (2,2)))
	classifier.add(Dropout(0.25))

	classifier.add(Conv2D(256, (3,3), activation = 'relu'))
	classifier.add(MaxPooling2D(pool_size = (2,2)))
	classifier.add(Dropout(0.25))
	#-----------------------------------------------------------------

	classifier.add(Flatten())
	classifier.add(Dense(1024, activation = 'relu'))
	classifier.add(Dense(units = 1, activation = 'sigmoid'))#change units to number of outputs

	#compile
	classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
	classifier.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)
	print(classifier.evaluate(x_test, y_test, batch_size=batch_size))

	classifier.save('trained_CNN_2020.h5')#will overwrite each time


class predict():
	def model():
		classifier = Sequential()

		#layers used to process image, same as training (change input shape)-------------------------------
		classifier.add(Conv2D(32, (3, 3), activation = 'relu', input_shape = (64, 64, 3)))#3 means RGB, 1 for black and white
		classifier.add(MaxPooling2D(pool_size = (2,2)))
		classifier.add(Dropout(0.25))

		classifier.add(Conv2D(64, (3,3), activation = 'relu'))
		classifier.add(MaxPooling2D(pool_size = (2,2)))
		classifier.add(Dropout(0.25))

		classifier.add(Conv2D(128, (3,3), activation = 'relu'))
		classifier.add(MaxPooling2D(pool_size = (2,2)))
		classifier.add(Dropout(0.25))

		classifier.add(Conv2D(256, (3,3), activation = 'relu'))
		classifier.add(MaxPooling2D(pool_size = (2,2)))
		classifier.add(Dropout(0.25))
		#-----------------------------------------------------------------

		classifier.add(Flatten())
		classifier.add(Dense(1024, activation = 'relu'))
		classifier.add(Dense(units = 1, activation = 'sigmoid'))#change units to number of outputs
		
		classifier.summary()
		return classifier

	def predict(img, img_width, img_height, ans = ''):
		img.resize(img_width, img_height)
		classifier = predict.model()
		load_model('.../trained_CNN_2020.h5')#obviously add rest of filepath
		img = np.array(img).reshape((img_width, img_height))
		img.expand_dims(img, axis = 0)
		prediction = classifier.predict(img)
		print(prediction)
		''' #not sure if this is needed or not
		conf = -1
		for i in [0,1]:
			if (prediction[i] > conf):
				ans = int(i)
				conf = prediction[i]
		print(ans)
		return ans
		'''

