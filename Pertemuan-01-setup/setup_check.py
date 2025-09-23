import sys, numpy as np, pandas as pd, sklearn, skfuzzy, cv2
print("Python:", sys.version)
print("Numpy:", np.__version__)
print("pandas:", pd.__version__)
print("sklearn:", sklearn.__version__)
print("opencv:", cv2.__version__)


import matplotlib.pyplot as plt
plt.plot([1,2,3],[1,4,9])
plt.title("Test plot")
plt.show()


from sklearn.datasets import load_iris
X,y = load_iris(return_X_y=True)
print("Iris shape:", X.shape)