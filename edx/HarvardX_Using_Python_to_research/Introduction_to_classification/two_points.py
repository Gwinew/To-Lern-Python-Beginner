import numpy as np

def distance(p1, p2):
    """Find the distance between points p1 and p2."""
    return np.sqrt(sum(np.power(p1-p2, 2)))


p1 = np.array([1,1])
p2 = np.array([4,4])
print(distance(p1,p2))
