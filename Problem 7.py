#Eoin Scanlon D15124581

#MATH 9975 Lab Assignment
#Problem 5

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector import curl, divergence

R = ReferenceFrame('R')

VecF = R[1]**2 * R[2] * R.x - R[0]*R[1] * R.y + R[2]**2 * R.z

print(VecF)

Figure = plt.figure()
ax = Figure.gca(projection = '3d')

x, y, z = np.meshgrid(np.arange(-1, 1, 0.2),
                      np.arange(-1, 1, 0.2),
                      np.arange(-1, 1, 0.2))

u = 2*x*y
v = x**2 + 2*z
w = y + 1

ax.quiver3D(x,y,z,u,v,w,length =0.1)

plt.show()

# Calculate the Divergence
F = divergence(VecF,R)
F

# Calculate the Curl
G = curl(VecF,R)
G
