sum=0
s=''
num=int(input('Enter your number:'))
for i in range(1,num):
    if num%i==0:
        sum+=i
        s+=str(i)
print('+'.join(s),'=',sum)
if sum==num:
    print('It is a perfect number')
else:
    print('Its not a perfect number')
