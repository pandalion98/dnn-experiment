# Model construction
from keras import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=393, input_dim=784, activation='relu'))
model.add(Dense(units=196, activation='relu'))
model.add(Dense(units=98, activation='relu'))
model.add(Dense(units=49, activation='relu'))
model.add(Dense(units=1))

model.summary()