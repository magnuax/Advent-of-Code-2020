
valid = 0

with open("day2.txt", "r") as infile:
    for line in infile:
        words = line.replace("-"," ")
        words = words.split()

        min = float(words[0])
        max = float(words[1])
        char = words[2].replace(":","")
        password = words[3]

        counter = 0
        for character in password:
            if character == char:
                counter +=1

        if counter >= min and counter <= max:
            valid+=1

print(valid)
