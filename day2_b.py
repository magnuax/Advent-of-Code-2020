
valid = 0
invalid = 0
with open("day2.txt", "r") as infile:
    for line in infile:
        words = line.replace("-"," ")
        words = words.split()

        i_1   = int(words[0]) - 1
        i_2   = int(words[1]) - 1
        char  = words[2].replace(":","")
        passw = words[3]

        if passw[i_1]==char and passw[i_2]==char:
            invalid += 1

        elif passw[i_1]==char or passw[i_2]==char:
            valid += 1

        else:
            invalid+=1

print(f"valid: {valid}\ninvalid:{invalid}")
