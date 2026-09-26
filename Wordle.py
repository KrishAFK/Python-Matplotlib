import random
alpha= (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
a=alpha[random.randint(0,25)]
b=alpha[random.randint(0,25)]
c=alpha[random.randint(0,25)]
word=a+b+c
while True:
    ans=input('Enter your guess:')
    if ans==word:
        print('CORRECT ANSWER')
        break
    if ans[0]==a:
        print('A is correct')
    if ans[1]==a or ans[2] ==a:
        print('A is at wrong position')
    if ans[1]==b:
        print('B is correct')
    if ans[0]==b or ans[2] ==b:
        print('B is at wrong position')
    if ans[2]==c:
        print('C is correct')
    if ans[0]==c or ans[1] ==c:
        print('C is at wrong position')
else:
    print('No letter is correct')

