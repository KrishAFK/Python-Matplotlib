"""
#Question 1
bookstack=[]
def pushbook():
    bookrec=[]
    title=input('Enter title:')
    aut=input('Enter author name:')
    year=input('Enter year:')
    bookrec=[title,aut,year]
    bookstack.append(bookrec)
pushbook()

def popbook():
    if bookstack==[]:
        print('Stack empty')
    else:
        i=bookstack.pop()
        print(i)
popbook()

def peep(x):
    if x==[]:
        print('Stack Empty')
    else:
        print(x[-1])
peep(bookstack)

def display(x):
    for i in range (len(x)-1,0,-1):
        print(x[i])
display(bookstack)
"""
#Question2

    
