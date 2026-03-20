import matplotlib.pyplot as plt

plt.plot(x,y)    # Plot Graph using axis x and y
plt.show()       # Dsiplay Graph
plt.subplot()    # Plotting multiple things inside graph

#Markers

plt.plot(x,y,'-or')    # RED Solid Line with Circles
plt.plot(x,y,':*b')    # BLUE Dotted Line with Star
plt.plot(x,y,'--xg')   # GREEN Line with X
plt.plot(x,y,'-.sk')   # BLACK Dashed/Dotted Line with Square

# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline

#Code for printing wave {Sine Wave}
xrange=range(0,36)
ax=[]
ay=[]
stepsize=2*(math.pi)/len(xrange)
for i in range(36):
    yval=math.sin(i*stepsize)
    ay.append(yval)
    ax.append(i)

plt.plot(ax,ay,'ro',label="sin(x)")  #ro prints only dots, NO Line
#Since range is continous, It prints a wave