
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Landsat DN
landsat = np.array([
    [1, 2, 5],
    [3, 4, 5],
    [2, 2, 3]
])
landsat[2, 2]


ref = np.array([
    [0, 0, 1],
    [2, 0, 1],
    [2, 2, 0]
])

mask_ref = ref > 0
mask_ref

# features vector
X = landsat[mask_ref]
X.shape
X
# referece vector
y = ref[mask_ref]

plt.plot(X, y, 'o')

df = pd.DataFrame({'X': X,
          'y': y})
