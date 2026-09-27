"""
#Program1
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='krish252007')

if con.is_connected():
    print('Works')
mycur=con.cursor()
mycur.execute('create database if not exists jrnl2')
mycur.execute('use jrnl2')

mycur.execute('create table if not exists club (code int, name varchar(15), age int, doa date\
              , coachname varchar(10))')
mycur.execute("insert into club values (101,'AAA',17,'2024-12-25','Kartik')")
mycur.execute("insert into club values (102,'BBB',17,'2024-01-02','Ranveer')")
mycur.execute("insert into club values (103,'CCC',17,'2024-04-07','Virat')")
mycur.execute("insert into club values (104,'DDD',17,'2024-07-12','Vicky')")
con.commit()

print('Press 1 to Dsiplay record where coach starts with K')
print('Press 2 to Display all records in desc order of DoA')
print('Press 3 to Display all records where age b/w 15 and 25')
print('Press 4 to Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        mycur.execute('select code,name,coachname from club where coachname like "K%"')
        a=mycur.fetchall() 
        for i in a:
            print(i)
    if ch==2:
        mycur.execute('select * from club order by doa desc')
        a=mycur.fetchall()
        for i in a:
            print(i)
    if ch==3:
        mycur.execute('select * from club where age between 15 and 25')
        a=mycur.fetchall()
        for i in a:
            print(i)
    if ch==4:
        print('Thank you for using the program')
        break
"""
#Program 2
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='krish252007')

mycur=con.cursor()
mycur.execute('create database if not exists jrnl2')
mycur.execute('use jrnl2')
mycur.execute('create table if not exists student (grn int, name varchar(10), \
                        age int, dob date, class int, tcode1 int, tcode2 int, fees float)')
mycur.execute('create table if not exists teacher (code int, tname varchar(10),\
                        subject varchar(15))')

print('Press 1 to insert values in both tables')
print('Press 2 to delete a record from student')
print('Press 3 to increase fees by 100 if student is in class 12')
print('Press 4 to display no of students in each class')
print('Press 5 to display grn,name,code,teacher_name,subject for code')
print('Press 6 to Exit')

while True:
    ch=int(input('Enter choice:'))
    if ch==1:
        #Taking values for table 1
        print('For Table 1')
        a=int(input('Enter grn: '))
        b=input('Enter name: ')
        c=int(input('Enter age: '))
        d=input('Enter DoB: ')
        e=int(input('Enter class: '))
        f=int(input('Enter tcode1: '))
        g=int(input('Enter tcode2: '))
        h=float(input('Enter fees: '))
        #Taking values for Table 2
        print('For Table 2')
        i=int(input('Enter code: '))
        j=input('Enter name: ')
        k=input('Enter subject: ')
        mycur.execute("insert into student values ({},'{}',{},'{}',{},{},{},{})".format(a,b,c,d,e,f,g,h))
        mycur.execute("insert into teacher values ({},'{}','{}')".format(i,j,k))
        print('The data has been inserted')
        con.commit()
    if ch==2:
        givengrn=int(input('Enter GRN to delete'))
        mycur.execute('delete from student where grn={}'.format(givengrn))
        print('The record has been deleted')
        con.commit()
    if ch==3:
        mycur.execute('update student set fees=fees+100 where class=12')
        print('Change done')
        con.commit()
    if ch==4:
        mycur.execute('select class,count(*) from student group by class')
        rec=mycur.fetchall()
        for v in rec:
            print(v)
    if ch==5:
        co=int(input('Enter code:'))
        mycur.execute('select grn,name,class,code,tname,subject\
        from student,teacher where (tcode1=code or tcode2=code) and code={}'.format(co))
        rec2=mycur.fetchall()
        for x in rec2:
            print(x)
    if ch==6:
        print('Thank you')
        break

    
