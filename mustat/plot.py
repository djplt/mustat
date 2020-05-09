'''
Matplotlib graph plotter wrapper functions.
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def histogram(data, x_label = "", y_label = "", title = ""):
  bins = np.arange(0, max(data) + 1.5) - 0.5
  _, ax = plt.subplots()
  ax.set_ylabel(y_label)
  ax.set_xlabel(x_label)
  ax.set_title(title)
  ax.set_xticks(bins + 0.5)
  ax.hist(data, bins)
  plt.xlim(0, int(max(data)*1.1))
  plt.show()
