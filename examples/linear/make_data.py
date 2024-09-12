import numpy as np
import math

npoint = 1001
xmin = -2.0*math.pi
xmax = 2.0*math.pi

x = np.linspace(xmin,xmax,npoint)

data = np.array([x,np.sin(x)])
np.savetxt("sin.dat",data.T)


data = np.array([x,np.cos(x)])
np.savetxt("cos.dat",data.T)

