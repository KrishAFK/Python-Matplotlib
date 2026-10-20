str='abc'

#a
#bb
#ccc
j=1
for i in str:
    print(i*j)
    j+=1

#a
#ab
#abc
j=1
for i in str:
    print(str[0:j])
    j+=1

#abc
#ab
#a
j=3
for i in str:
    print(str[0:j])
    j-=1

#cba
#cb
#c
j=-4
for i in str:
    print(str[-1:j:-1])
    j+=1

#a
#abab
#abcabcabc
j=1
for i in str:
    print(j*str[0:j])
    j+=1









