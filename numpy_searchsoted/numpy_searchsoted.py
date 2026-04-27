import numpy as np

a = np.array([1, 3, 5, 7])

np.searchsorted(a, 4)
# 2
np.searchsorted(a, [0, 2, 6, 8])
# array([0, 1, 3, 4])
np.searchsorted(a, 5, side='right')
# 3
