import csv	
f=open('Trial 1.csv','a',newline='')
mywriter=csv.writer(f)
mywriter.writerow(['500','DDD','PGT','30000'])
f.close()
#Checking by opening the file again
f=open('Trial 1.csv','r',newline='\n')
a=csv.reader(f)
for i in a:
    print(i)
f.close()
