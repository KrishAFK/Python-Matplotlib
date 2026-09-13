def deleteword():
    with open('employees.txt','r') as file:
        word=input('Enter a word:')
        s=''
        line=file.readlines()
        for i in line:
            a=i.split()
            for j in a:
                if j==word:
                    del j
                else:
                    s+=j
            s+='\n'
        file.write(s)
        print(s)
        
deleteword()
            
                
        
    
    
