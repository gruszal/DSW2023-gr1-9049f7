import numpy as np

a = np.array([[10, 11], [2, 3], [5, 8]])
print(a, '\n')

a2 = np.delete(a, -1, axis=0)
print(a2, '\n')

a3 = np.delete(a, -1, axis=1)
print(a3, '\n')
