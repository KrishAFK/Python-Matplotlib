import matplotlib.pyplot as plt
import math

xrange=range(0,36)
ax=[]
ay=[]
stepsize=2*(math.pi)/len(xrange)
for i in range(36):
    yval=math.sin(i*stepsize)
    ay.append(yval)
    ax.append(i)

plt.plot(ax,ay,'ro',label="sin(x)")
plt.legend()
plt.show()
