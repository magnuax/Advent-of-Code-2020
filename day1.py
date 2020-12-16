
entries=[]

with open("day1.txt", "r") as infile:
    for line in infile:
        entries.append(line)

for i in entries:
    i=int(i)
    for j in entries:
        j=int(j)
        if i+j==2020:
            print(f"{i}+{j}={i+j}")
            print(f"{i}*{j}={i*j}")
