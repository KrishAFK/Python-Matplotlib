#Finding the roots of a quadratic equation
import math
print("To solve a quadratic equation, Enter the equation...")
op=int(input("Press 1 for +ve and 2 for -ve:"))
if op==2: 
    a=-1*(int(input("Enter the value of x^2:")))
else:
    a=int(input("Enter the value of x^2:"))
op=int(input("Press 1 for +ve and 2 for -ve:"))
if op==2: 
    b=-1*int(input("Enter the value of x:"))
else:
    b=int(input("Enter the value of x:"))
op=int(input("Press 1 for +ve and 2 for -ve:"))
if op==2: 
    c=-1*int(input("Enter the value of  the constant:"))
else:
    c=int(input("Enter the value of  the constant:"))

#Solving using Quadratic Formula

D=(b**2)-4*a*c
#Root 1
Root1=((-1*b)+(math.sqrt(D)))/2*a

#Root 2
Root2=((-1*b)-(math.sqrt(D)))/2*a

print('The 2 roots are:')
print(Root1,'and', Root2)













