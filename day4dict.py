from operator import itemgetter

fields  = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
field_dict = {}
valid   = 0

eyecolors =["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_data(passport):
    byr = 1920 <= float(passport["byr"]) <= 2002
    eyr = 2020 <= float(passport["eyr"]) <= 2030
    iyr = 2010 <= float(passport["iyr"]) <= 2020
    hcl = passport["hcl"][0]=="#" and len(passport["hcl"])==7
    ecl = passport["ecl"] in eyecolors
    pid = len(passport["pid"]) == 9
    hgt = (passport["hgt"][-2:]=="cm" and 150<=float(passport["hgt"][:-2]) <=193) or \
          (passport["hgt"][-2:]=="in" and 59 <=float(passport["hgt"][:-2]) <=76)

    if hgt and byr and iyr and eyr and hcl and ecl and pid == True:
        return True
    else:
        return False


infile  = open("day4.txt", "r")

for line in infile:
    words = line.replace(":"," ")
    words = words.split()
    if words:
        for i in range(0, len(words), 2):
            field_dict[words[i]] = words[i+1]
    else:
        if len(field_dict) >= len(fields):
            try:
                if check_data(field_dict) == True:
                    valid += 1

            except KeyError:
                pass

        field_dict = {}

# Check last f_count on last line
if len(field_dict) >= len(fields):
    try:
        if check_data(field_dict) == True:
            valid += 1
            
    except KeyError:
        pass

print(f"Valid passports: {valid}")

infile.close()
