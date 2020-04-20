from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# loading the dataset
dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')
# splitting into input (X) and output (Y) vars
X = dataset[:,0:8] # gets everything from 0 to 7
y = dataset[:,8] # gets everything from 8 to 8

# defining the keras model
model = Sequential()
# 1st hidden layer with 12 nodes (with 8 input nodes for the model):
model.add(Dense(12, input_dim=8, activation='relu'))
# 2nd hidden layer with 8 nodes:
model.add(Dense(8, activation='relu'))
# output:
model.add(Dense(1, activation='sigmoid')) # sigmoid squashes the result between 0 and 1

# compiling the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fitting the model on the dataset
model.fit(X, y, epochs=500, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
