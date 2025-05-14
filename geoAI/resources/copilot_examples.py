import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix


a = np.arange(1, 10)
b = np.arange(10, 20)
c = np.add(a, b)
print("a:", a)
print("b:", b)
print("c:", c)