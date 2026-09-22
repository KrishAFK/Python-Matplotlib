import csv
def Add_Employee():
    f=open('employee.csv','w',newline='')
    w=csv.writer(f)
    w.writerow(['Employee ID','Employee name','Salary'])
    n=int(input('Enter no. of employees:'))
    for i in range(n):
        l=eval(input('Enter a list of ID, Name, Salary:'))
        w.writerow(l)
    f.close()
def Update_employee():
    f=open('employee.csv','r',newline='\n')
    a=csv.reader(f)
    m=[]
    for i in a:
        if i[0]=='Employee ID':
            continue
        if int(i[2])<20000:
            i[2]=int(i[2])+2000
            m.append(i)
        else:
            m.append(i)
    f.close()
    f=open('employee.csv','w',newline='')
    w=csv.writer(f)
    w.writerows(m)
    f.close()
Update_employee()
f=open('employee.csv','r',newline='\n')
b=csv.reader(f)
try:
    while True:
        for i in b:
            print(i)
except:
    f.close()
        
    
