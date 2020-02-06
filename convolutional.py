from keras import Sequential
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.datasets import mnist
from keras.layers import *
from keras.utils import to_categorical
from matplotlib import pyplot
from time import time

(trainX, trainY), (testX, testY) = mnist.load_data()

# Reshape model as as prep for convolutional layer ingest
# Also, normalize it for some reason I'm about to find out
trainX = trainX.astype('float32') / 255.0
trainX = trainX.reshape(trainX.shape[0], 28, 28, 1)

testX = testX.astype('float32') / 255.0
testX = testX.reshape(testX.shape[0], 28, 28, 1)

# Transform output into categoricals (regression was a bad idea)
trainY = to_categorical(trainY)
testY = to_categorical(testY)

# Define model
model = Sequential()
model.add(Dropout(rate=0.2, input_shape=(28, 28, 1)))
model.add(Conv2D(filters=64, kernel_size=(2, 2), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(rate=0.2))
model.add(Dense(100, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

# Checkpoint procedure
filepath = "checkpoints/conv/mnist-dropout-{epoch:02d}-{acc:.5f}-" + str(time()) + ".h5"
callback_checkpoint = ModelCheckpoint(filepath, monitor='acc', verbose=1, save_best_only=True, mode='max')
callback_tensorboard = TensorBoard(log_dir='./tensorboard_logs/{}'.format(time()))

# Cross validation
# kfold = KFold(5, shuffle=True, random_state=1)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit
history = model.fit(x=trainX, y=trainY, batch_size=10000, epochs=200, validation_data=(testX, testY),
                    callbacks=[callback_checkpoint, callback_tensorboard])

# Plot loss and accuracy
pyplot.subplot(2, 1, 1)
pyplot.title('Cross Entropy Loss')
pyplot.plot(history.history['loss'], color='blue', label='train')
pyplot.subplot(2, 1, 2)
pyplot.title('Classification Accuracy')
pyplot.plot(history.history['acc'], color='blue', label='train')
pyplot.show()
