"""
#Program1
def even(a):
            if a%2==0:
                return True
            else:
                return False
def prime(a):
            for i in range(2,a):
                if a%i==0:
                    return False
            else:
                return True
print('Press 1 to check whether a number is even or not;\
          Press 2 to check whether the number is prime or not;\
          Press 3 to Exit')
while True:
    ch=int(input('Enter your choice:'))
    if ch==1:
        num=int(input('Enter a number:'))
        print(even(num))
    if ch==2:
        num=int(input('Enter a number:'))
        print(prime(num))
    if ch==3:
        print('Thank you')
        break

#Program 2
def pow(a,b):
    res=1
    for i in range(b):
        res*=a
    return res
num1=int(input('Enter a number:'))
num2=int(input('Enter the power:'))
print(pow(num1,num2))


#Program3
def fact(a):
    res=1
    for i in range(1,a+1):
        res*=i
    return res
num=int(input('Enter a number:'))
print(fact(num))


#Program4
def series(x,n):
    sum=1
    for i in range(1,n+1):
        sum+=x**i
    return sum
a=int(input('Enter value of x:'))
b=int(input('Enter value of n:'))
print('The sum is',series(a,b))


#Program5
def findbig(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input('Enter a number:'))
num2=int(input('Enter a number:'))
print('The bigger number is',findbig(num1,num2))


#Program6
def sum(*n):
    s=0
    for i in n:
        s+=i
    return s
print('The sum is',sum(10,20,30,40))


#Program7
import math
def series(x,n):
    sum=1
    for i in range(1,n+1):
        sum+=((x**i)/math.factorial(i))
    return sum
a=int(input('Enter value of x:'))
b=int(input('Enter value of n:'))
print(series(a,b))


#Program8
def count(*n):
    even=0
    odd=0
    for i in n:
        if i%2==0:
            even+=1 
        else:
            odd+=1
    return even,odd
a,b=count(10,15,20,25)
print('No. of even numbers:',a)
print('No. of odd numbers:',b)

#Program9
def search(a,b):
    for i in range(len(a)):
        if a[i]==b:
            print('Present at index',i)
            break
    else:
        print('Not found')
l=eval(input('Enter a list of numbers:'))
num=int(input('Enter the no. to search:'))
search(l,num)

#Program10
def swap(a):
    l=[]
    for i in range(0,len(a),2):
        l.append(a[i+1])
        l.append(a[i])
    print(l)
li=eval(input('Enter a list of numbers:'))
if (len(li)%2)!=0:
    print('Enter even no. of elements.')
else:
    swap(li)

"""
#Program11
def move(a):
    for i in a:
        if i%5==0:
            a.remove(i)
            a.append(i)
    print(a)
l=eval(input('Enter a list of numbers:'))
move(l)

















