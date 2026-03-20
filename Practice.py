import matplotlib.pyplot as plt
import math
x=[]
y=[]
for i in range(1,20):
    x.append(i)
    y.append(math.exp(i))

print(x)
print(y)


plt.plot(x,y)
plt.show()
