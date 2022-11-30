import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes([0.2, 0.2, 0.7, 0.6])
x = np.linspace(0,10,100)                  
ax.plot(x,np.sin(x))
ax.plot(x,-1*np.sin(x))
ax.plot(x,np.cos(x))
ax.plot(x,-1*np.cos(x))
plt.xticks([])
plt.show()