#Checking whether a number is prime or not

num=int(input("Enter a number:"))
if num==1:
    print("1 is neither prime nor composite")
elif num!=1:    
    for i in range(2,num):
        if num%i==0:
            print("The number is composite")
            print(i,'x',num//i,'is',num)
            
    else:
        print("The number is prime")
