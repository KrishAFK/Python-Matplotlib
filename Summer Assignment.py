"""
#Program1
for i in range(1,6):
    if i==1 or i==3 or i==5:
        print('#'*i,end='')
        print()
    if i==2 or i==4:
        print('@'*i,end='')
        print()

#Program2
row=3
for i in range(1,row+1):
    for j in range(1,row+1-i):
        print('  ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()

for i in range(row-1,0,-1):
    for j in range(1,row+1-i):
        print('  ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()

#Program3
row = 4
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Program4
for i in range(1,6):
    if i==1 or i==5:
        print('*'*10)
    else:
        print('*',' '*13,'*')

#Program5
n = 5 
for i in range(n):
    print(' '*(n-i), end='')
    print(11**i)
"""
#Program 6
letter=''  
row=4
for i in range(1,row+1):
    for j in range(1,row+1-i):
        print('  ',end='')
    for j in range(1,i+1):
        if j==1:
            letter='A'
        if j==2:
            letter='B'
        if j==3:
            letter='C'
        if j==4:
            letter='D' 
        print(letter,end='')
    for j in range(i-1,0,-1):
        if j==1:
            letter='A'
        if j==2:
            letter='B'
        if j==3:
            letter='C'
        if j==4:
            letter='D' 
        print(letter,end='')
    print()
    
for i in range(row-1,0,-1):
    for j in range(1,row+1-i):
        print('  ',end='')
    for j in range(1,i+1):
        if j==1:
            letter='A'
        if j==2:
            letter='B'
        if j==3:
            letter='C'
        if j==4:
            letter='D' 
        print(letter,end='')
    for j in range(i-1,0,-1):
        if j==1:
            letter='A'
        if j==2:
            letter='B'
        if j==3:
            letter='C'
        if j==4:
            letter='D' 
        print(letter,end='')
    print()
"""
#Program 7
row = 4
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print('*'*5)

#Program 8
row=4
for i in range(1,row+1):
    for j in range(1,row+1-i):
        print('  ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()

for i in range(row,0,-1):
    for j in range(1,row+1-i):
        print('  ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()

#Program10
word="PYTHON"
for i in range(0,6):
    for j in range(0,i+1):
        print(word[j],end='')
    print()

#Program11
rows=69
for i in range(5,0,-1):
    for j in range(rows,64,-1):
        print(chr(j),end="")
    print()
    rows-=1

#Program 12
space=25
s=20
letter=65
for i in range(1,8,2):
    if letter==65 or letter==71:
        print(' '*space,chr(letter)*i,end='')
        print()
        space-=17
    if letter==67 or letter==69:
        print(' '*s,chr(letter)*i,end='')
        print()
        s-=5
    letter+=2

name=""
while True:
     name= input('enter name:')
     if name=="end":
          break
          print('hi')
     print('hello',name)
else:
     print(' I am out of loop')
     
name=""
while True:
     name= input('enter name:')
     if name=="end":
          pass
          print('hi')
     print('hello',name)
else:
     print(' I am out of loop')

"""
















