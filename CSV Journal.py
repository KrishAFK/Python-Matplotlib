"""
#Program 1
import csv
import os
def create():
    f=open('toys.csv','w',newline='')
    n=int(input('Enter no. of records:'))
    w=csv.writer(f)
    for i in range(n):
        l=eval(input('Enter [Name, Price, Category, Stock]:'))
        w.writerow(l)
    f.close()
def display():
    f=open('toys.csv','r',newline='\n')
    a=csv.reader(f)
    for i in a:
        print(i)
    f.close()
def search():
    name=input('Enter name to search:')
    f=open('toys.csv','r',newline='\n')
    a=csv.reader(f)
    for i in a:
        if i[0]==name:
            print(i)
    f.close()
def append():
    f=open('toys.csv','a',newline='')
    w=csv.writer(f)
    x=int(input('How many records to append:'))
    for i in range(x):
        m=eval(input('Enter [Name, Price, Category, Stock]:'))
        w.writerow(m)
    f.close()
def highest():
    f=open('toys.csv','r',newline='\n')
    nf=open('highest.csv','w',newline='')
    w=csv.writer(nf)
    a=csv.reader(f)
    for i in a:
        if int(i[1])>100:
            print('The data has been copied to the new file.')
            w.writerow(i)   
    f.close()
    nf.close()
def modify():
    f=open('toys.csv','r',newline='\n')
    nf=open('temp.csv','w',newline='')
    w=csv.writer(nf)
    a=csv.reader(f)
    for i in a:
        if int(i[3])<10:
            print('The data has been modified.')
            i[3]=int(i[3])+10
            w.writerow(i)
        else:
            w.writerow(i)
    f.close()
    nf.close()
    os.remove('toys.csv')
    os.rename('temp.csv','toys.csv')
def delete():
    f=open('toys.csv','r',newline='\n')
    nf=open('temp.csv','w',newline='')
    w=csv.writer(nf)
    a=csv.reader(f)
    for i in a:
        if i[2].lower()!='fun':
            print('The record has been deleted.')
            w.writerow(i)
    f.close()
    nf.close()
    os.remove('toys.csv')
    os.rename('temp.csv','toys.csv')

print('Press 1 to Display the data, Press 2 to Search a record,\
Press 3 to Append data, Press 4 to Copy the records where price>100\
Press 5 to Modify the stock, Press 6 to Delete a record where category is "FUN"\
Press 7 to Exit the program')
create()
while True:
    ch=int(input('Enter your choice:'))
    if ch==1:
        display()
    if ch==2:
        search()
    if ch==3:
        append()
    if ch==4:
        highest()
    if ch==5:
        modify()
    if ch==6:
        delete()
    if ch==7:
        print('Thank you for using the program')
        break
        

# Program 2
import os
import csv
def create():
    f=open('student.csv','w',newline='')
    n=int(input('Enter no. of records:'))
    w=csv.writer(f)
    for i in range(n):
        l=eval(input('Enter [Name, Eng Mark, CS Mark, Phy Mark, Chem Mark, Math Mark]:'))
        w.writerow(l)
    f.close()
def display():
    f=open('student.csv','r',newline='\n')
    a=csv.reader(f)
    for i in a:
            print(i)
    f.close()
def search():
    name=input('enter name to search:')
    f=open('student.csv','r',newline='\n')
    a=csv.reader(f)
    for i in a:
        if i[0]==name:
            print(i)
    f.close()
def append():
    f=open('student.csv','a',newline='')
    x=int(input('Enter addtitional no. of records:'))
    w=csv.writer(f)
    for i in range(x):
        l=eval(input('Enter [Name, Eng Mark, CS Mark, Phy Mark, Chem Mark, Math Mark]:'))
        w.writerow(l)
    print('The data has been appended.')
    f.close()
def failure():
    f=open('student.csv','r',newline='\n')
    nf=open('fail.csv','w',newline='')
    w=csv.writer(nf)
    a=csv.reader(f)
    for i in a:
        for j in range(1,6):
            if int(i[j])<36:
                w.writerow(i)
            print(i)
            break
    print('The data has been copied.')
    nf.close()
    f.close()
def modify():
    f=open('student.csv','r',newline='\n')
    nf=open('temp.csv','w',newline='')
    w=csv.writer(nf)
    a=csv.reader(f)
    for i in a:
        for j in range(1,6):
            if int(i[j])<50:
                i[j]=int(i[j])+10
                w.writerow(i)
        print(i)    
    f.close()
    nf.close()
    os.remove('student.csv')
    os.rename('temp.csv','student.csv')
def delete():
    sum=0
    f=open('student.csv','r',newline='\n')
    nf=open('temp.csv','w',newline='')
    w=csv.writer(nf)
    a=csv.reader(f)
    for i in a:
        for j in range(1,6):
            sum=sum +int(i[j])
        avg=sum/6
        if avg<40:
            w.writerow(i)
    print('The data has been modified.')
    nf.close()
    f.close()
    os.remove('student.csv')
    os.rename('temp.csv','student.csv') 
print('Press 1 to Display the data, Press 2 to Search a record,\
Press 3 to Append data, Press 4 to Copy the records where students have failed\
Press 5 to Modify the marks<50, Press 6 to Delete records where avg<40%"\
Press 7 to Exit the program')
create()
while True:
    ch=int(input('Enter your choice:'))
    if ch==1:
        display()
    if ch==2:
        search()
    if ch==3:
        append()
    if ch==4:
        failure()
    if ch==5:
        modify()
    if ch==6:
        delete()
    if ch==7:
        print('Thank you for using the program')
        break







    
