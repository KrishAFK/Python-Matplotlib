#Program1
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='krish252007')

if con.is_connected():
    print('Works')
mycur=con.cursor()
mycur.execute('create database if not exists jrnl2')
mycur.execute('use jrnl2')
"""
mycur.execute('create table if not exists club (code int, name varchar(15), age int, doa date, coachname varchar(10))')
mycur.execute("insert into club values (101,'AAA',17,'2024-12-25','Kartik')")
mycur.execute("insert into club values (102,'BBB',17,'2024-01-02','Ranveer')")
mycur.execute("insert into club values (103,'CCC',17,'2024-04-07','Virat')")
mycur.execute("insert into club values (104,'DDD',17,'2024-07-12','Vicky')")
con.commit()
"""
print('Press 1 to Dsiplay record where coach starts with K')
print('Press 2 to Display all records in desc order of DoA')
print('Press 3 to Display all records where age b/w 15 and 25')
print('Press 4 to Exit')
ch=int(input('Enter your choice: '))
if ch==1:
    mycur.execute('select code,name,coachname from club where coachname like "K%"')
    a=mycur.fetchall()
    for i in a:
        print(i)

