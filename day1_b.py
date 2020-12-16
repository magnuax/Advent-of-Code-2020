
entries=[]

with open("day1.txt", "r") as infile:
    for line in infile:
        entries.append(line)

for i in entries:
    i=int(i)
    for j in entries:
        j=int(j)
        for k in entries:
            k=int(k)
            sum = i+j+k
            if sum==2020:
                print(f"{i}+{j}+{k}={i+j+k}")
                print(f"{i}*{j}*{k}={i*j*k}")
