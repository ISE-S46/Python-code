import math
import numpy as np
import matplotlib.pyplot as plt

def graph(func, x_range):
   x = np.arange(*x_range)
   y = func(x)
   plt.plot(x, y)

graph(lambda x: 100*(np.power(0.8, x)), (0,100))