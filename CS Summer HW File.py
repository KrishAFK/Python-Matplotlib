
#Program 1
message=input("Enter a message:")
print("Hello,",message)


#Program 2
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    print("The largest no. is",a)
    print("The smallest no. is",b)
elif b>a:
    print("The largest no. is",b)
    print("The smallest no. is",a)
    

#Program 3
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
#To print the largest number
if a>b and a>c:
    print("The largest no. is",a)
elif b>a and b>c: 
    print("The largest no. is",b)
else:
    print("The largest no. is",c)
#To print the smallest number
if a<b and a<c:
    print("The smallest no. is",a)
elif b<a and b<c:
    print("The smallest no. is",b)
else:
    print("The smallest no. is",c)


#Program 4(a)
import math
x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
sum=1
for i in range(2,n+1):
    sum=sum+(math.pow(x,i))
print(sum)


#Program 4(b)
import math
x=int(input("Enter the value of x:"))
sign=0
sum=0
for i in range(1,7):
    if sign==0:
        sum=sum+((math.pow(x,i))/math.factorial(i))
        sign=1
        continue
    if sign==1:
        sum=sum-((math.pow(x,i))/math.factorial(i))
        sign=0
print(sum)


#Program 5
#Perfect Number
num=int(input("Enter no.:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
    else:
        continue
if sum==num:
    print("It's a perfect number")
else:
    print("It's not a perfect number")
#Armstrong Number
num=int(input("Enter no.:"))
final=num
str=str(num)
sum=0
for i in str:
    digit=num%10
    d=digit**3
    sum+=d
    num=num//10
if sum==final:
    print("It's a Armstrong number")
elif sum!=num:
    print("It's not a Armstrong number")
#Palindrome Number
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


#Program 6
num=int(input("Enter a number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("It's composite")
            break
    else:
        print("It's prime")
        

#Program7
n=int(input("Enter a number:"))
if n<=0:
    print("Not possible")
elif n==1:
    print("0")
elif n>=2:
    a=0
    b=1
    print('0')
    print('1')
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
    

#Program8a
for i in range(1,6):
    print('*'*i,end='')
    print()


#Program8b
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()


#Program8c      
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end='')
    print()
    

#Program9
lcase=0
ucase=0
vowels=0
consonants=0
str=input("Enter a string:")
for i in str:
    if i>='A' and i<='Z':
        ucase+=1
    elif i>='a' and i<='z':
        lcase+=1
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1;
    else:
        consonants=consonants+1 
print(ucase,'Uppercase Characters')
print(lcase,'Lowercase Characters')
print(vowels,'Vowels')
print(consonants,'Consonants')


#Program10
percent=float(input("Enter the percentage:"))
if percent>90 and percent<100:
            print("The Grade is A1")
if percent>80 and percent<90:
            print("The Grade is A2")
if percent>70 and percent<80:
            print("The Grade is B1")
if percent>60 and percent<70:
            print("The Grade is B2")
if percent>50 and percent<60:
            print("The Grade is C1")
if percent<50 :
            print("The Grade is C2")
if percent<35:
            print("You have Failed")


#Program11
i=1
while i<11:
    product=10*i
    print(10,'x',i,'=',product)
    i+=1


#Program12
day=int(input("Enter the date(dd):"))
month=int(input("Enterthe month (mm):"))
year=int(input("Enter the year(yyyy):"))
if day>00 and day<32 and month>00 and month<13 and year>1900 and year<2023:
    print("The Date is valid")
else:
    print("The Date is invalid")


#Program13
print("What function do you want to perform?:")
print("press 1 to find the factorial")
print("press 2 to find the sum of the digits")
print("press 3 to check whether its palindrome")
print("press 4 to check whether its Armstrong no.")
print("press 5 to check whether its prime or not")
print("press 6 to Exit the function")

#Find Factorial
func=int(input("Enter the function:"))
if func==1:
    num=int(input("Enter the number:"))    
    factorial = 1    
    if num<0:    
       print("Factorial does not exist for negative numbers")    
    elif num == 0:    
        print("The factorial of 0 is 1")    
    else:    
       for i in range(1,num + 1):    
           factorial = factorial*i    
       print("The factorial of",num,"is",factorial) 

#Sum of digits
if func==2:
    sum=0
    print("How many digits do you want to enter?")
    n=int(input("No. of Digits you wish to enter:"))
    for i in range(n):
        number=int(input("Enter the digit:"))
        sum=sum+number
    print("The sum is",sum)
#Palindrome or not
if func==3:
    num=int(input("Enter a number:"))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
#Armstrong number
if func==4:
    num=int(input("Enter no.:"))
    final=num
    str=str(num)
    sum=0
    for i in str:
        digit=num%10
        d=digit**3
        sum+=d
        num=num//10
    if sum==final:
        print("It's an Armstrong number")
    elif sum!=num:
        print("It's not an Armstrong number")
#Prime or not
if func==5:
    num=int(input("Enter a number:"))
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print("It's not prime")
                break
        else:
            print("It's prime")
#Exit
if func==6:
    print("Thank you for using this Program.")


#Program14
s=int(input("Enter the start value of a range:"))
e=int(input("Enter the end value of a range:"))
oddsum=0
evensum=0
primesum=0
for i in range(s,e+1):
    if i%2==0:
        evensum+=i
    elif i%2!=0:
        oddsum+=i
for num in range(s,e+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primesum+=num
print("Sum of odd numbers is",oddsum)
print("Sum of even numbers is",evensum)
print("Sum of prime numbers is",primesum)



#Program 15
lower=int(input("Enter the start value of a range:"))
upper=int(input("Enter the end value of a range:"))
primesum=0
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primesum+=num
print("The sum of prime numbers is ",primesum)


#Program 16
lower=int(input("Enter the start value of a range:"))
upper=int(input("Enter the end value of a range:"))
primesum=0
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           primesum+=num
print(primesum)


#Program 17
import math
a=int(input("Enter the coefficient of x^2:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant term:"))
print("Your Final Equation is",a,"x^2+",b,"x+",c,'=0')
#Finding Discriminant
d=(b*b)-4*a*c
if d<0:
    print("The eq. has no real roots.")
elif d==0 or d>0:
    Root1=(-1*b+ math.sqrt(d))/(2*a)
    print(Root1)
    Root2=(-1*b-math.sqrt(d))/(2*a)
    print(Root2)
 



    

