import matplotlib.pyplot as plt

csv_file=open("Gendata.csv","r")
csv_file.readline()
line_count=1
valid_number_count=0
gen1_list=[]
for line in csv_file:
    line_count+=1
    gen_values=line.split(",")
    if (len(gen_values[1])==0):
        continue

    try:
        float(gen_values[1])
    
    except:
        continue
    valid_number_count+=1
    value=float(gen_values[1])   
    gen1_list.append(value)

print("Gne 1 values to plot = ",len(gen1_list))

plt.plot(gen1_list,'-k',label='Generator 1 (MW)')

plt.title("Power Station Ouput")
plt.xlabel('Time')
plt.ylabel("MW Output")
plt.show()
           