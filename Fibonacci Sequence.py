#Fibonacci series

length=int(input("How many numbers do you want in the fibonacci series?:"))
print('0')
print('1')
a=0
b=1
r=(length-2)//2
for i in range(0,r):
    sum=a+b
    print(sum)
    a=sum
    sum1=a+b
    print(sum1)
    b=sum1

# To print that 1 extra term if input is an odd number since our above code prints sum in pairs.
if (length%2)!=0:
    sum=a+b
    print(sum)

