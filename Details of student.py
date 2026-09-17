with open('data.txt','w+') as file:
    n=int(input('Enter:'))
    l=[]
    """
    for i in range(n):
        s=''
        grn=int(input('Enter grn:'))
        name=input('Enter name:')
        mark=int(input('Enter marks:'))
        s+=str(grn)
        s+=' '
        s+=name
        s+=' '
        s+=str(mark)
        l.append(s)
        """
    l=['1 a 3', '2 b 4']
    print(l)
    file.write(str(l))
    file.seek(0)
    line=file.read()
    line=list(line)
    print(line)
    inp=input('Enter grn to search:')
    
  
