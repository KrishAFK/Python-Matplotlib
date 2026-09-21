import pickle
f=open('emp.txt','wb')
n=int(input('How many students:'))
for i in range(n):
    l=eval(input('Enter a list of roll,name,marks:'))
    pickle.dump(l,f)
f.close()
f=open('emp.txt','ab+')
f.seek(0)
try:
    while True:
        a=pickle.load(f)
        if a[2]==81.0:
            a[2]+=2
            b=a
except:
    f.close()
f=open('emp.txt','wb')
pickle.dump(b,f)
print(b)
f.close()

