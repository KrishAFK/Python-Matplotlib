"""
#Program1
import pickle
def create():
    f=open('employee.dat','wb')
    n=int(input('How many employees:'))
    for i in range(n):
        d=eval(input('Enter a dict of id,name,designation,salary:'))
        pickle.dump(d,f)
    f.close()
def search():
    idn=int(input('Enter the id no. to search:'))
    f=open('employee.dat','ab+')
    f.seek(0)
    try:
        while True:
            a=pickle.load(f)
            if a['ID']==idn:
                print(a)
                if a['salary']<20000:
                    a['salary']+=2000                    
                    b=a
                    pickle.dump(b,f)
                    print(b)
                    f.close()
                    break
                else:
                    break
            else:
                print("The employee hasn't been found")
                break
    except:
        f.close()
create()
search()


#Program2
import pickle
def insert():
    f=open('employee.dat','ab+')
    data=input('Enter the data to enter:')
    pickle.dump(data,f)
    print('The data has been appended at the end of the file')
    f.close()
insert()


#Program3
import pickle
f=open('employee.dat','wb')
n=int(input('How many employees:'))
for i in range(n):
    l=eval(input('Enter a list of id,name,designation,salary:'))
    pickle.dump(l,f)
f.close()
def manager():
    f=open('employee.dat','rb')
    file1=open('manager.dat','wb')
    f.seek(0)
    try:
        while True:
            a=pickle.load(f)
            if a['Designation'].lower()=='manager':
                pickle.dump(a,file1)
    except:
        f.close()
        file1.close()
def acc():
    f=open('employee.dat','rb')
    file2=open('acc.dat','wb')
    f.seek(0)
    try:
        while True:
            a=pickle.load(f)
            if a['Designation'].lower()=='accountant':
                pickle.dump(a,file2)
    except:
        f.close()
        file2.close()
manager()
acc()
print('Checking if Data is inserted or not')
print('File 1')
f=open('manager.dat','rb')
try:
    while True:
        a=pickle.load(f)
        print(a)
except:
    f.close()
print('File 2')
f=open('acc.dat','rb')
try:
    while True:
        b=pickle.load(f)
        print(b)
except:
    f.close()
    
"""
#Program4
import pickle
def create():
    f=open('student.dat','wb')
    n=int(input('How many students:'))
    for i in range(n):
        d=eval(input('Enter a list of roll,name,marks,house:'))
        pickle.dump(d,f)
    f.close()
def display():
    f=open('student.dat','rb')
    try:
        while True:
            a=pickle.load(f)
            print(a)
    except:
        f.close()
def searchname():
    f=open('student.dat','rb')
    name=input('Enter the name of student:')
    try:
        while True:
            a=pickle.load(f)
            if a[1]==name:
                print(a)
    except:
        f.close()
def searchid():
    f=open('student.dat','rb')
    roll=int(input('Enter the roll no:'))
    try:
        while True:
            a=pickle.load(f)
            if a[0]==roll:
                print(a)
    except:
        f.close()
def append():
    f=open('student.dat','ab')
    x=int(input('No. of additional records:'))
    for i in range(x):
        d=eval(input('Enter a list of roll,name,marks,house:'))
        pickle.dump(d,f)
    f.close()
def count():
    f=open('student.dat','rb')
    count=0
    s=0
    try:
        while True:
            a=pickle.load(f)
            count+=1
            s+=a[2]
    except:
        f.close()
    avg=s/count
    return count,avg
def highest():
    f=open('student.dat','rb')
    file=open('high.dat','wb')
    try:
        while True:
            a=pickle.load(f)
            if a[2]>=90:
                pickle.dump(a,file)
            else:
                continue
    except:
        f.close()
        file.close()
def modify():
    f=open('student.dat','rb')
    global l
    l=[]
    try:
        while True:
            a=pickle.load(f)
            if a[2]<23:
                a[2]+=10
                l.append(a)
            else:
                l.append(a)
    except:
        f.close()
    file=open('student.dat','wb')
    for i in l:
        pickle.dump(i,file)
f=open('student.dat','rb')
try:
    while True:
        a=pickle.load(f)
        print(a)
except:
    f.close()
def delete():
    global l
    l=[]
    f=open('student.dat','rb')
    try:
        while True:
            a=pickle.load(f)
            if a[3].lower()=='emerald':
                continue
            else:
                l.append(a)
    except:
        f.close()
    file=open('student.dat','wb')
    for i in l:
        pickle.dump(i,file)

def deleteroll():
    global l
    l=[]
    f=open('student.dat','rb')
    roll=int(input('Enter the roll to delete:'))
    try:
        while True:
            a=pickle.load(f)
            if a[0]==roll:
                continue
            else:
                l.append(a)
    except:
        f.close()
    file=open('student.dat','wb')
    for i in l:
        pickle.dump(i,file)
print('Welcome to the program')
print('Press 1 to Create a database, Press 2 to Display the data, Press 3 to Search via name, \
Press 4 to Search via ID, Press 5 to Append more data, Press 6 to Count the records, Press 7 to Copy \
the highest marked records, Press 8 to Modify records, Press 9 to Delete via house, Press 10 to Delete via roll, Press 11 to Exit')
while True:
    ch=int(input('Enter choice:'))
    if ch==1:
        create()
    if ch==2:
        display()
    if ch==3:
        searchname()
    if ch==4:
        searchid()
    if ch==5:
        append()
        print('The data has been appended')
    if ch==6:
        a,b=count()
        print('No. of records:',a)
        print('Average marks:',b)
    if ch==7:
        highest()
        print('The data has been copied')
    if ch==8:
        modify()
        print('The data has been modified')
    if ch==9:
        delete()
        print('The data with house as emerald has been deleted')
    if ch==10:
        deleteroll()
    if ch==11:
        print('Thank you')
        break
    














            
                








