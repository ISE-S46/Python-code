import matplotlib.pyplot as plt
import numpy as np
from random import randint

# Define the constants (arbitrary values)
c1 = randint(1, 7)
c2 = randint(1, 7)
c3 = randint(1, 7)
c4 = randint(1, 7)
c5 = randint(1, 7)
c6 = randint(1, 7)
c7 = randint(1, 7)

# Define the range of input sizes
n_values = np.arange(1, 51)

# Best case: t_best(n)
t_best = (c2 + c3 + c4 + c1 + c7) * n_values - (c2 + c3 + c4 + c7)

# Average case: t_avg(n)
t_avg = ((c4 + c5 + c6) / 4) * n_values**2 + (c1 + c2 + c3 + (c4 - c5 - c6) / 4 + c7) * n_values - (c2 + c3 + c4 + c7)

# Worst case: t_worst(n)
t_worst = ((c4 + c5 + c6) / 2) * n_values**2 + (c1 + c2 + c3 + (c4 - c5 - c6) / 2 + c7) * n_values - (c2 + c3 + c4 + c7)

# Plotting the graphs
plt.plot(n_values, t_best, label='Best Case: O(n)', color='g')
plt.plot(n_values, t_avg, label='Average Case: O(n^2)', color='b')
plt.plot(n_values, t_worst, label='Worst Case: O(n^2)', color='r')
plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity')
plt.title('Time Complexity of Insertion Sort')
plt.legend()
plt.grid(True)
plt.show()