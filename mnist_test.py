import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
from matplotlib import pyplot

image_data = open('train-images.idx3-ubyte', 'rb')
label_data = open('train-labels.idx1-ubyte', 'rb')

# Load label data
label_data.read(4)  # Skip first 4 bytes (magic number)
num_labels = int.from_bytes(label_data.read(4), 'big')
label_list = []
curLabel = 0
while curLabel < num_labels:
    label_list.append(int.from_bytes(label_data.read(1), 'big'))
    curLabel += 1
label_data.close()
label_array = np.array(label_list).reshape(-1, 1)
print("Label data loaded")

# Load image data
image_data.read(4)  # Skip first 4 bytes (magic number)
num_images = int.from_bytes(image_data.read(4), 'big')
image_rows = int.from_bytes(image_data.read(4), 'big')
image_cols = int.from_bytes(image_data.read(4), 'big')
image_list = []
curImage = 0
while curImage < num_images:
    curImageByte = 0
    curImageList = []
    while curImageByte < (image_rows * image_cols):
        curImageList.append(int.from_bytes(image_data.read(1), 'big'))
        curImageByte += 1
    image_list.append(curImageList)
    if curImage % 100 == 0:
        print("Current image: ", curImage)
    curImage += 1

image_data.close()
image_array = np.array(image_list)
print("Image data loaded")

# plt.imshow(image_array[0].reshape(28, 28))
# plt.show()

# Model construction
model = Sequential()
model.add(Dense(units=393, input_dim=784, activation='relu'))
model.add(Dense(units=196, activation='relu'))
model.add(Dense(units=98, activation='relu'))
model.add(Dense(units=49, activation='relu'))
model.add(Dense(units=1))

# Model compilation
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# checkpoint
filepath = "checkpoints/mnist-100b-relu-chkpt-{epoch:02d}-{acc:.5f}.h5"
checkpoint = ModelCheckpoint(filepath, monitor='acc', verbose=1, save_best_only=True, mode='max')

# Fit model!
history = model.fit(x=image_array, y=label_array, batch_size=100, epochs=100, verbose=1, callbacks=[checkpoint])

# Plot loss and accuracy
pyplot.subplot(2, 1, 1)
pyplot.title('Cross Entropy Loss')
pyplot.plot(history.history['loss'], color='blue', label='train')
pyplot.subplot(2, 1, 2)
pyplot.title('Classification Accuracy')
pyplot.plot(history.history['acc'], color='blue', label='train')
pyplot.show()
