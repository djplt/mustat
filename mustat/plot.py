'''
Matplotlib graph plotter wrapper functions.
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from heapq import nlargest
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

def histogram(data, x_label = "", y_label = "", title = ""):
  bins = np.arange(0, max(data) + 1.5) - 0.5
  _, ax = plt.subplots()
  ax.set_ylabel(y_label)
  ax.set_xlabel(x_label)
  ax.set_title(title)
  ax.set_xticks(bins + 0.5)
  ax.hist(data, bins)
  plt.xlim(0, int(max(data)*1.1))

def wordBarPlot(words, x_label = "", y_label = "", title = ""):
  _, ax = plt.subplots()
  ax.set_ylabel(y_label)
  ax.set_xlabel(x_label)
  ax.set_title(title)

  # Strip out "stop" words that don't tell us very much information about a given text.
  words = [word for word in words if word not in stopwords.words('english')]
  count = Counter(words)
  wordsLargest = nlargest(10, count.keys(), key=count.get) 

  ax.bar(wordsLargest, [count[word]for word in wordsLargest])

def show():
  plt.show()