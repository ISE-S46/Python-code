# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:31:22 2024

@author: S
"""
from keras.models import Sequential
from keras.layers import Dense
from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import numpy as np
# Function to create model, required for KerasClassifier
def create_model(optimizer = 'rmsprop', init = 'glorot_uniform'):
# create model
    model = Sequential()
    model.add(Dense(11, input_dim=8,kernel_initializer = init, activation= 'relu' ))
    model.add(Dense(18,kernel_initializer = init, activation= 'relu' ))
    model.add(Dense(1,kernel_initializer = init, activation= 'sigmoid'))
    # Compile model
    model.compile(loss= 'binary_crossentropy' , optimizer=optimizer , metrics=[ 'accuracy' ])
    return model
# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
# load pima indians dataset
data = "pima-indians-diabetes.csv"
dataset = np.loadtxt(data, delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = KerasClassifier(model = create_model, verbose = 0)
print(model.get_params().keys())

optimizers = ['rmsprop','adam']
init = ['glorot_uniform','normal','uniform']
epochs = [50,100,150]
batches = [5,10,20]
param_grid = dict(optimizer=optimizers, epochs = epochs, batch_size=batches, model__init=init)
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid_result = grid.fit(X, Y)

print("best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means,stds,params):
    print("%f (%f) with: %r"% (mean,stdev,param))