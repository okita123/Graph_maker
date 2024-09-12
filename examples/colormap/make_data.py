import numpy as np
import math

npoint =  201
xmin   = -2.0
xmax   =  2.0
ymin   = -2.0
ymax   =  2.0

x = np.linspace(xmin,xmax,npoint)
y = np.linspace(ymin,ymax,npoint)

X,Y = np.meshgrid(x,y)

Z = np.exp(-((X-1.0)**2 +(Y-1.0)**2)/2.0) \
   -np.exp(-((X+1.0)**2 +(Y+1.0)**2)/2.0)

with open("test.dat",mode="w") as f:
  for i in range(npoint):
    for j in range(npoint):
      line="{:15.7f}".format(x[i])+" "+"{:15.7f}".format(y[j])+" "+"{:15.7f}".format(Z[j][i])+"\n"
      f.write(line)
    line="\n"
    f.write(line)
