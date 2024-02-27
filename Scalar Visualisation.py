import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.DataFrame({'x': np.random.randn(100), 'y': np.random.randn(100), 'value': np.random.randn(100)})

cmap="viridis"
alpha=1

plt.figure(figsize=(6,6))
plt.scatter(data["x"],data["y"],c=data["value"],cmap=cmap,alpha=alpha)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('scatterplot with color map')
plt.colorbar(label='value')
plt.show()

data=pd.DataFrame(np.random.rand(10,10))

plt.figure(figsize=(8,6))
plt.contourf(data.values)
plt.show()

from mpl_toolkits.mplot3d import Axes3D

data=pd.DataFrame(np.random.rand(10,10))

x=np.arange(data.shape[0])
y=np.arange(data.shape[1])
x,y=np.meshgrid(x,y)
fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,data.values,cmap='viridis')
plt.show()
