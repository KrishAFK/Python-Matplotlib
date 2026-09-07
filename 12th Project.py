import math
import csv
import random
import mysql.connector
import os

#Manager Interface
#{Key:[Cost, Members, Checkin Date, Checkout date, Duration]}
def address():
    print('''We are glad you tried to reach out to us. You can contact us 24/7 at the links given below
--------------------------------------------------------------------------------------------------------------
Phone: +971 50 7654321
Email: sunshinehotel@gmail.com
Website: www.sunshinehotel.ae
Location:  Airport Street, Opp. ENBD Bank, Dubai, U.A.E
-------------------------------------------------------------------------
Feel free to reach out to us anytime...Thank you''')

def rooms():
    print('''------------------------------
~Type 1-Standard room
Cost: AED 550 per night
View: Downtown view
Layout: 1 room with window
Perks: Gym, Pool.
------------------------------
~Type 2-Deluxe room
Cost: AED 750 per night
View: Sea view
Layout: 2 rooms with balcony
Perks: Gym, Pool, Breakfast.
------------------------------
~Type 3-Luxury suite
Cost: AED 1450 per night
View: Sea view
Layout: 3 rooms with balcony
Perks: Gym, Pool, Breakfast, Beach access.
------------------------------''')

def cost(t):
    global cst
    if t.lower()=='standard':
        x=550
    if t.lower()=='deluxe':
        x=750
    if t.lower()=='luxury':
        x=1450
    cst=x*dur
    fcst=math.ceil(cst)
    print('Your Final amount is AED ',fcst,'/=')
                    
def login(username, password):
    conn = mysql.connector.connect(host='localhost',user='root',passwd='krish252007',database='project')  
    cursor = conn.cursor()
    cursor.execute("select * from loginpage")
    result = cursor.fetchall()
    for i in result:
        if i[0]==username:
            if i[1]==password:
                print('Login Successfull')
                return True
                break
            else:
                print('Incorrect password')
    else:
        print('Username not in server')

    conn.close()  

print('Welcome to our Hotel')
a=input('Choose your interface:')
if a.lower()=='manager':

# Example usage:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if (login(username, password))==True:

        while True:
            print('Press 1 to Check Empty rooms:')
            print('Press 2 to Search for a guest')
            print('Press 3 to Access the Database')
            print('Press 4 to Exit')
            choice=int(input('Enter your choice:'))
            if choice==1 :
                f=open('database.csv','r')
                fileobj=csv.reader(f)
                l=[]
                print('The empty rooms are:')
                for i in fileobj:
                    if i[-1]=='0':
                        print(i[0])
                        l.append(i[0])
                room=int(input('Enter room no.: '))
                if str(room) in l:
                    print('Room selected')
                else:
                    print('Room occupied, Try again')
            if choice==2:
                room=int(input('Enter the room no.:'))
                f=open('database.csv','r')
                fileobj=csv.reader(f)
                for i in fileobj:
                    if i[0]==str(room):
                        print('The Cost of the room: AED',i[1])
                        print('No. of members:',i[2],'person(s)')
                        print('Check in date:',i[3])
                        print('Check out date:',i[4])
                        print('Duration of stay:',i[5],'day(s)')
                        print('Thank you')
            if choice==3:
                print('[Room no, Cost, Members, Checkin Date, Checkout date, Duration]')
                f=open('database.csv','r')
                fileobj=csv.reader(f)
                for i in fileobj:
                    print(i)
            if choice==4:
                print('Thank you for using this software')
                break

if a.lower()=='guest':
    d={}
    if a.lower()=='guest':
        print('Hello and Welcome to the online portal of  ~The Sunshine Hotel~')
        print('Select the tabs to explore and enjoy your browsing.')
        print('Press 1 to Explore our room options:')
        print('Press 2 to Book a room online')
        print('Press 3 to Complete Payment online')
        print('Press 4 to Contact us')
        print('Press 5 to Exit the server')
        while True:
            ch=int(input('Enter your selected choice:'))
            if ch==1:
                print('Here are our room options:')
                rooms()
            if ch==2:
                nm=input('Enter your name: ')
                typ=input('Type of room: ')
                dur=int(input('Duration of stay (days): '))
                cost(typ)
                t=random.randrange(1111,10000)
                print('''-----------------------------------------------------------------
Your electronically generated token number is ''',t)
                print('You can use it to complete the payment process')
                d[t]=cst
            if ch==3:
                    mode=input('How would you like to complete your payment?: ')
                    if mode.lower()=='cash':
                        print('You can pay by cash directly at our reception when you arrive, Thank you')
                    if mode.lower()=='card':
                        print('''You are about to enter the Net banking portal
--------------------------------------------------------''')
                        cno=int(input('Enter the Card Number: '))
                        cname=input('Enter the name on the Card: ')
                        cvv=input('Enter your CVV: ')
                        tkn=int(input('Enter the token number (if any) else type 0000: '))
                        if tkn==0000:
                            pass
                        else:
                            print('Amount to be paid: AED',d[tkn])
                        a=random.randrange(1111,10000)
                        print('Your one time password is ',a)
                        otp=int(input('Enter the 4 digit OTP:'))
                        if otp==a:
                            print('''-----------------------------------------------------------------
The transaction was carried out successfully. Thank you''')
                        else:
                            print('The OTP was WRONG. Pls try again later')
            if ch==4:
                address()
            if ch==5:
                print('We hope your queries have been resolved. We wish to see you again :)')
                break
       
                    
                    
                
    


    
                
    
    





