import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense


(xtrain, ytrain), (_, _) = keras.datasets.mnist.load_data(path="mnist.npz")
xtrain = xtrain.astype('float32')

xtrain = xtrain/255

xtrain = xtrain.reshape(list(xtrain.shape) + [1])    # (60000, 28, 28, 1)

model = Sequential()
model.add(Conv2D(32,(5,5),activation="relu",input_shape=xtrain.shape[1:],padding="same"))
model.add(Conv2D(64,(5,5),activation="relu",padding="same"))
model.add(keras.layers.MaxPooling2D((2,2)))

model.add(Conv2D(64,(4,4),activation="relu",padding="same"))
model.add(Conv2D(128,(4,4),activation="relu",padding="same"))
model.add(keras.layers.MaxPooling2D((2,2)))

model.add(Conv2D(128,(3,3),activation="relu",padding="same"))
model.add(keras.layers.MaxPooling2D((2,2)))

model.add(Flatten())
model.add(Dense(128,activation="sigmoid"))
model.add(Dense(64,activation="relu"))
model.add(Dense(10,activation="softmax"))

model.compile(optimizer='adamax',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
model.fit(xtrain, ytrain, epochs=3)

model.save('ready.h5')

