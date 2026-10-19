"""
#Program1
A=()
n=int(input('How many numbers:'))
for i in range(n):
    x=int(input('Enter the number:'))
    A=A+(x,)
print(A)
E=()
O=()
for j in A:
    if j%2==0:
        E=E+(j,)
    else:
        O=O+(j,)
print(E)
print(O)


#Program2
A=()
n=int(input('How many numbers:'))
for i in range(n):
    x=int(input('Enter the number:'))
    A=A+(x,)
print(A)
print('The maximum number is:',max(A))
print('The maximum number is:',min(A))

#Program3
A=()
n=int(input('How many names:'))
for i in range(n):
    x=input('Enter the number:')
    A=A+(x,)
print(A)
for i in A:
    if len(i)==5:
        print(i)

#Program4
n=3
A=()
for i in range(n):
    L=()
    for j in range(3):
        sub=int(input('Enter numbers:'))
        L=L+(sub,)
    A=A+(L,)
print(A)
Max=()
for i in A:
    Max=Max+(max(i),)
print(Max)

#Program5
n=int(input('How many subtuples:'))
A=()
for i in range(n):
    L=()
    for j in range(3):
        sub=int(input('Enter numbers:'))
        L=L+(sub,)
    A=A+(L,)
print(A)
T=()
for i in A:
    T=T+(len(i),)
print(T)

#Program6
n=int(input('How many students:'))
A=()
for i in range(n):
    L=()
    name=input('Enter the name:')
    mark1=int(input('Enter the 1st mark:'))
    mark2=int(input('Enter the 2nd mark:'))
    L=L+(name,mark1,mark2)
    A=A+(L,)
print(A)
for j in A:
    print('Name:',j[0],'Sum:',j[1]+j[2])

#Program7
n=int(input('How many students:'))
A=()
for i in range(n):
    L=()
    name=input('Enter the name:')
    mark1=int(input('Enter the 1st mark:'))
    mark2=int(input('Enter the 2nd mark:'))
    L=L+(name,mark1,mark2)
    A=A+(L,)
print(A)
var=0
for j in A:
    if j[1]>var:
        var=j[1]
        name=j[0]
    elif j[2]>var:
        var=j[2]
        name=j[0]
print(name,var)  

#Program8
n=int(input('How many tuples?:'))
A=()
for i in range(n):
    L=()
    name1=input('Enter the name:')
    name2=input('Enter the name:')
    L=L+(name1,name2)
    A=A+(L,)
print(A)
for i in A:
    print(i.count('kerala'))

#Program9
n=int(input('How many students:'))
A=()
for i in range(n):
    L=[]
    name1=input('Enter the name:')
    mark1=int(input('Enter Marks:'))
    mark2=int(input('Enter Marks:'))
    L=L+[name1,mark1,mark2]
    A=A+(L,)
print(A)
name=input('Enter a name:')
num=int(input('Enter mark:'))
for i in A:
    if i[0]==name:
        i.append(num)
print(A)

#Program10
A=()
n=int(input('How many names:'))
for i in range(n):
    x=input('Enter the number:')
    A=A+(x,)
print(A)
B=A[::-1]
print(B)

#Program11
A=()
n=int(input('How many numbers:'))
for i in range(n):
    x=int(input('Enter the number:'))
    A=A+(x,)
print(A)
A=list(A)
print(sum(A))

#Program12
n=int(input('How many students:'))
A=()
for i in range(n):
    email=input('Enter email-id:')
    A=A+(email,)
dom=()
user=()
for i in A:
    a=i.split('@')
    user=user+(a[0],)
    dom=dom+(a[1],)
print(user)
print(dom)

#Program 13

n=int(input('How many terms:'))
a=0
b=1
A=(a,b)

for i in range(n-2):
    c=a+b
    A=A+(c,)
    a=b
    b=c   
print(A)

#Program 14
A=()
n=int(input('How many pairs:'))
for i in range(n):
    L=()
    for i in range(2):
        x=int(input('Enter the number:'))
        L=L+(x,)
    A=A+(L,)
print(A)
for i in A:
        if i[0]%2==0 and i[1]%2==0:
            print(i)

#Program17
A=()
n=int(input('How many numbers:'))
for i in range(n):
    x=int(input('Enter the number:'))
    A=A+(x,)
print(A)
l=0
for i in A:
    if i>l:
        l=i
print('Maximum number is',l)
if (A.count(l))>1:
    print('There are multiple maximum numbers')

#Program18
A=()
n=int(input('How many numbers:'))
for i in range(n):
    x=int(input('Enter the number:'))
    A=A+(x,)
print(A)
l=0
for i in A:
    if i>l:
        l=i
print('Maximum number is',l)
if A[(len(A)//2)]==l:
    print('Number lies in the middle')
"""
#Program19
A=()
n=int(input('How many numbers:'))
for i in range(n):
    x=int(input('Enter the number:'))
    A=A+(x,)
print(A)
a=list(A)
b=sorted(a)
if b==a:
    print('Tuple is sorted')
else:
    print("Tuple isn't sorted")











