#Armstrong Number
New=[]
L=eval(input('Enter a list:'))
for num in L:
    original=num
    string=str(num)
    length=len(string)
    sum=0
    for i in range(1,length+1):
        Digit=num%10
        sum=sum+(Digit**length)
        num=num//10

    if sum==original:
        New.append(sum)
print(New)


