"""
#Program1
keys=eval(input('Enter the list of keys:'))
values=eval(input('Enter the list of values:'))
d=dict(zip(keys,values))
print(d)

#Program2
K=[]
V=[]
n=int(input('How many items:'))
for i in range(n):
    k=input('Enter the key:')
    v=input('Enter the value:')
    K.append(k)
    V.append(v)
print(K)
print(V)
d=dict(zip(K,V))
print(d)

#Program 2 Alternative
n=int(input('How many items:'))
d={}
for i in range(n):
    k=input('Enter the key:')
    v=input('Enter the value:')
    d[k]=v
print(d)

#Program3
n=int(input('Enter no of students:'))
K=()
V=()
for i in range(n):
    k=input('Enter name:')
    K=K+(k,)
    v=input('Enter value:')
    V=V+(v,)
d={}
d=dict(zip(K,V))
print(d)
x=input('Enter the key:')
print(d[x])

#Program 4
a=input('Enter a sentence:')
d={}
l=a.split()
for i in l:
    c=l.count(i)
    d[i]=c
print(d)

#Program5
n=int(input('Enter no of students:'))
K=()
V=()
for i in range(n):
    k=input('Enter name:')
    K=K+(k,)
    V=V+(2500,)
d={}
d=dict(zip(K,V))
print(d)


#Program6
K=()
V=()
n=int(input('No of items:'))
for i in range(n):
    k=input('Enter key:')
    v=input('Enter price:')
    K=K+(k,)
    V=V+(v,)
d=dict(zip(K,V))
print(d)
print('1-Display item price')
print('2-Add new item')
print('3-Update existing item')
print('4-Delete an item')
print('5-Display the dictionary')
print('6-Exit')
while True:
    choice=int(input('Enter your choice:'))
    if choice==1:
        x=input('Enter the key:')
        print(d[x])
    if choice==2:
        k=input('Enter key:')
        v=input('Enter price:')
        K=K+(k,)
        V=V+(v,)
        d=dict(zip(K,V))
        print(d)
    if choice==3:
        x=input('Enter the key:')
        y=input('Update value:')
        d[x]=y
        print(d)
    if choice==4:
        x=input('Enter the key:')
        del d[x]
        print(d)
    if choice==5:
        print(d)
    if choice==6:
        break

#Program7
n=int(input('Enter the no of students:'))
d={}
K=()
M=[]
for i in range(n):
    marks=[]
    k=input('Enter the name of student:')
    cs=int(input('Enter marks:'))
    chem=int(input('Enter marks:'))
    math=int(input('Enter marks:'))
    phy=int(input('Enter marks:'))
    eng=int(input('Enter marks:'))
    marks=[cs,chem,math,phy,eng]
    K=K+(k,)
    M.append(marks)
d=dict(zip(K,M))
print(d)

for i in d:
    print(i,end='-')
    v=list(d.values())
    for j in v:
        print(max(j))

#Program8
n=int(input('Enter the no of trains:'))
d={}
K=()
M=[]
for i in range(n):
    marks=[]
    k=input('Enter the name of train:')
    stops=eval(input('Enter the list of stops:'))
    M.append(stops)
    K=K+(k,)
d=dict(zip(K,M))
print(d)
v=list(d.items())
print(v)
for i in range(n):
    if 'Chennai' in v[i][1]:
        print(v[i][0])

#Program9
n=int(input('Enter the no of items:'))
d={}
K=()
M=()
for i in range(n):
    marks=[]
    k=input('Enter the name of item:')
    cp=int(input('Enter Cost price:'))
    sp=int(input('Enter Selling price:'))
    price=(cp,sp)
    K=K+(k,)
    M=M+(price,)
d=dict(zip(K,M))
print(d)
c=[]
s=[]
largesp=0
smallcp=100000
namecp=''
namesp=''
v=list(d.items())
print(v)
for i in range(n):
    if (v[i][1][1])>largesp:
        largesp=(v[i][1][1])
        namesp=(v[i][0])
    if (v[i][1][0])<smallcp:
        smallcp=(v[i][1][0])
        namecp=(v[i][0])
print('Minimum CP:',namecp,'-',smallcp)
print('Maximum SP:',namesp,'-',largesp)

#Program10
n=int(input('Enter the no of students:'))
d={}
for i in range(n):
    name=input('Enter the name of student:')
    cs=int(input('Enter marks:'))
    chem=int(input('Enter marks:'))
    math=int(input('Enter marks:'))
    phy=int(input('Enter marks:'))
    eng=int(input('Enter marks:'))
    marks=[cs,chem,math,phy,eng]
    d[name]=marks
for i in d:
    d[i]=sorted(d[i])
print(d)


#Program11
n=int(input("Enter No. of students:"))
d={}
for i in range(n):
    roll=int(input("enter Roll no:"))
    name=input("Enter name:")
    cl=int(input("Enter class:"))
    gen=input("Enter Gender:")
    d1={"name": name,"class":cl,"gender":gen}
    d[roll]=d1
for i in d:
    if d[i]["class"]==11:
        print(i,d[i])
    else:
        continue

#Program12
n=int(input('Enter No. of students:'))
D={}
for i in range(n):
    d={}
    roll=int(input('Enter roll no.:'))
    name=input('Enter name:')
    cs=int(input('Enter marks:'))
    chem=int(input('Enter marks:'))
    math=int(input('Enter marks:'))
    phy=int(input('Enter marks:'))
    eng=int(input('Enter marks:'))
    marks=[cs,chem,math,phy,eng]
    d={'name':name,'marks':marks}
    D[roll]=d
print(D)

large=0
name=''
for i in D:
    if (sum(list(D[i].values())[1]))>large:
        large=(sum(list(D[i].values())[1]))
        name=(list(D[i].values())[0])
print(name)


#Program13
d={}
C=[]
for i in range(3):
    roll=int(input('Enter Roll No.:'))
    name=input('Enter name:')
    d[roll]=name
    C.append(roll)
print(d)
n=int(input('No. of remaining students:'))
V=[]
for i in range(n):
    vote=int(input('Cast your vote as roll no.:'))
    V.append(vote)
large=0
for i in C:
    if V.count(i)>large:
        large=V.count(i)
        name=i
print('The winner is',d[i])


#Program14
d={}
n=int(input('No of students:'))
for i in range(n):
    name=input('Enter name:')
    resno=input('Enter residence no.:')
    d[name]=resno

V=(list(d.values()))
for i in d:
    if d[i].startswith('06'):
       print(i)
"""
#Program15
D={}
n=int(input('Enter no. of entries:'))
for i in range(n):
    d={}
    e={}
    ecode=int(input('Enter Ecode:'))
    name=input('Enter name:')
    date=int(input('Enter date of birth:'))
    month=int(input('Enter month of birth:'))
    year=int(input('Enter year of birth:'))
    e['dd']=date
    e['mm']=month
    e['yyyy']=year
    print(e)
    d['name']=name
    d['dob']=e
    D[ecode]=d
print(D)
m=int(input('Given month:'))
for i in D.items():
    ecode,a=i
    if a["dob"]["mm"]==m:
        print(ecode, "-", a['name'])

"""
#Program16
sen=input('Enter a sentence:')
d={}
for i in sen:
    c=sen.count(i)
    d[i]=c
print(d)


#Program17
n=int(input('Enter no. of teams:'))
d={}
for i in range(n):
    L=[]
    team=input('Enter team name:')
    win=int(input('Enter no. of wins:'))
    loss=int(input('Enter no. of losses:'))
    L.append(win)
    L.append(loss)
    d[team]=L
print(d)
for i in d:
    if d[i][0]>d[i][1]:
        print(i)


#Program18
D={}
n=int(input('Enter no. of entries:'))
for i in range(n):
    d={}
    e=[]
    app=int(input('Enter Application number:'))
    name=input('Enter name:')
    date=int(input('Enter date of birth:'))
    month=int(input('Enter month of birth:'))
    year=int(input('Enter year of birth:'))
    mark=int(input('Enter the mark:'))
    e.append(date)
    e.append(month)
    e.append(year)
    d['name']=name
    d['dob']=e
    d['mark']=mark
    D[app]=d
print(D)
for i in D:
    if D[i]['dob'][2]>=2016 and D[i]['dob'][2]<=2017 and D[i]['mark']>50:
        print(D[i]['name'])
   
"""        











    
