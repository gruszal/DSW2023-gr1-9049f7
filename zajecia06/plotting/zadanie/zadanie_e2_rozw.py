import numpy as np
import matplotlib.pyplot as plt

dane = np.loadtxt('oceny.txt', delimiter=',', dtype=str)
oceny = np.array(dane[:, 1:], dtype=np.float64)
uczniowie = np.array(dane[:, :1]).flatten()  # Uwaga!

wagi_ocen = (0.5, 1, 0.5, 0.5, 1, 1)

# https://numpy.org/doc/stable/reference/generated/numpy.average.html
srednie = np.average(oceny, axis=1, weights=wagi_ocen).round(2)

plt.figure(figsize=(9, 3))

plt.subplot(1, 2, 1)
plt.plot(oceny.T)

plt.subplot(1, 2, 2)
plt.bar(uczniowie, srednie)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()
