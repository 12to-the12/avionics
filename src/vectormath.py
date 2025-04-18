import numpy as np
from math import acos

lambda x: np.sqrt(np.dot(x,x))

def magnitude(vector) -> float:
    return np.sqrt(np.dot(vector,vector))

def norm(vector): return vector/magnitude(vector)

# angle between two vectors in radians
def angle(a,b):
    dotp = np.dot(a,b)/(magnitude(a)*magnitude(b))
    return acos(dotp)
