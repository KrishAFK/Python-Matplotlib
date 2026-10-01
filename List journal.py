"""#Program 16
m=int(input('Enter the number of rows:'))
n=int(input('Enter the number of columns:'))
A=[]
for i in range(m):
    L=[]
    for j in range(n):
        x=int(input('Enter the element:'))
        L.append(x)
    A.append(L)
print(A)
#Matrix
sum=0
for i in A:
    for j in i:
        print(j,end=' ')
    print()
   

#Program16

for i in range(m):
    for j in A[i]:
        sum+=j
    print('The sum of',i+1,'row is',sum)
    sum=0

#Program17  
for i in range(m):
    for j in range(n):
        sum+=A[j][i]
    print('The sum of',i+1,'column is',sum)
    sum=0
  
#Program18
l=0
for i in range(len(A)):
    print(A[i][l])
    sum+=A[i][l]
    l+=1
print(sum)

#Program19
for b in range(m):
    for a in range(b+1):
        print(A[b][a],end=' ')
    print()

#Program20
for i in range(3):
    for j in range(m):
        print(A[j][i],end=' ')
    print()

#Program21
n=int(input('How many names do you want?:'))
L=[]
for i in range(n):
    x=input('Enter name:')
    L.append(x)
print(L)
name=input('Search name:')
print(L.index(name))

#Program22
n=int(input('How many names do you want?:'))
L=[]
for i in range(n):
    x=input('Enter name:')
    L.append(x)
print(L)
for i in L:
    if i[0].lower()=='a':
        print(i)

#Program23
n=int(input('How many names do you want?:'))
L=[]
for i in range(n):
    x=input('Enter name:')
    L.append(x)
print(L)
for i in L:
    if 'b' in i.lower() or 'v' in i.lower():
        print(i)

#Program24
sen=input('Enter a sentence:')
sen=sen.split(' ')
print(sen)
for i in sen:
    if i[0].lower()=='a':
        print(i)
"""
#q30
n=int(input("Enter the number of students :"))
A=[]
for i in range(n):
        L=[]
        name=input("Enter your name:")
        prac=int(input(("Enter Practical marks:")))
        theory=int(input(("Enter theory marks:")))
        total=prac+theory
        L.append(name)
        L.append(prac)
        L.append(theory)
        L.append(total)
        A.append(L)
print(A)
x=0
for i in range(len(A)):
    if A[i][3]>x:
         x=A[i][3]
    else:
        continue
print('Highest marks:',x)
for j in A:
    if x==j[3]:
        print("Student with most marks:",j[0])
        break
    else:
        continue
"""
#q31
n=int(input("Enter the number of students :"))
a=[]
for i in range(n):
        d=[]
        grn=int(input('Enter GR NO:'))
        name=input("enter  name:")
        perc=int(input('Enter percentage:'))
        d.append(name)
        d.append(grn)
        d.append(perc)
        a.append(d)
a.sort()
print(a)
"""









    
