# Code Challenge - Pure/Impure Rotation Matrices

import numpy as np
import math
import matplotlib.pyplot as plt

# 2D input vector
v = np.array([ 3, -2 ])

x = []
y = []
for i in range(57):
    th = i*np.pi/28
    A = np.array([ [math.cos(th),-math.sin(th)], [2*math.sin(th),math.cos(th)] ])

    # output vector is Av (convert v to column)
    w = A@np.matrix.transpose(v)
    mag = np.linalg.norm(w)
    x.append(th)
    y.append(mag)

plt.plot(x,y)

plt.xlabel("Angle in Radians")
plt.ylabel("Magnitude")
plt.show()
