import matplotlib.pyplot as plt

x=[0,1,2,3,4,5,6,7,8,9]
y=[0,1,4,9,16,25,36,49,64,81]


plt.plot(x,y,'-or',label='y=x^2',)
plt.title("Example Plot Using Matplotlib Library")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()

plt.show()

