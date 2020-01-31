from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset = loadtxt("pima-indians-diabetes.data.csv", delimiter=',')

x = dataset[:, 0:8]
y = dataset[:, 8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x=x, y=y, batch_size=10, epochs=100, verbose=2)

loss, accuracy = model.evaluate(x=x, y=y)

print('Accuracy: %.2f' % (accuracy * 100))

predictions = model.predict(x)
predictionsC = model.predict_classes(x)

print('Accuracy: %.2f' % (accuracy * 100))
