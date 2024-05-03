import numpy as np
import matplotlib.pyplot as plt

tab = []

with open('wynik.txt', 'r') as f:
 for i in f:
  tab.append(int(i))

histogram, bins = np.histogram(tab, bins=256, density=True)
histogram = histogram / histogram.sum()

entropy = -np.sum(histogram * np.log2(histogram + 1e-10))

plt.figure(figsize=(10, 5))
plt.bar(np.arange(len(histogram)),histogram, color='darkblue', width=1.0)
plt.title(f'Histogram Liczb')
plt.xlabel('Wartość Liczbowa')
plt.ylabel('Częstotliwość')
plt.grid(True)
plt.show()
print("Entropia = "+str(entropy))