from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax1 = plt.axes(projection='3d')
ax2 = Axes3D(fig)
import numpy as np
z = np.linspace(0,13,1000)
x = 5*np.sin(z)
y = 5*np.cos(z)
zd = 13*np.random.random(100)
xd = 5*np.sin(zd)
yd = 5*np.cos(zd)
ax1.scatter3D(xd,yd,zd, color='green')
ax1.plot3D(x,y,z,color ='grey')
plt.show()