import numpy as np
import math

npoint = 1000
x = np.random.randn(npoint)
y = np.random.randn(npoint)

data = np.array([x,y])
np.savetxt("random.dat",data.T)

