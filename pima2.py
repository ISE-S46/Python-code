4# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:46:13 2024

@author: S
"""

from pandas import read_csv
import numpy as np
data = "pima-indians-diabetes.csv"
dataset = np.loadtxt(data, delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(11, input_shape=(8,), activation= 'relu' ))
model.add(Dense(18, activation= 'relu' ))
model.add(Dense(1, activation= 'sigmoid' ))

model.compile(loss= 'binary_crossentropy' , optimizer= 'adam' , metrics=[ 'accuracy' ])

model.fit(X, Y, epochs = 1000, batch_size = 10)

_, accuracy = model.evaluate(X,Y)
print('Accuracy: %.2f'%(accuracy*100))

predictions = model.predict(X)
rounded = [round(x[0]) for x in predictions]
predictions = (model.predict(X) > 0.5).astype(int)
for i in range(5):
    print('%s => %d (expected %d)' %(X[i].tolist(),predictions[i],Y[i]))