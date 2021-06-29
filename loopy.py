#
# loopy.py - read in ten numbers, plot and print stats
#
import numpy as np
import matplotlib.pyplot as plt

size = 10

values = np.zeros(size)

for i in range(size):
    values[i] = int(input("Enter value [" + str(i) + "] : "))

print("\nMinimum is: ", values.min())
print("Maximum is: ", values.max())
print("Mean is: ", values.mean())
print("Sum is: ", values.sum())

plt.plot(values)
plt.title(str(size) + " Values in Array")
plt.show()
