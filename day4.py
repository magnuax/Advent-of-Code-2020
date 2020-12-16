from operator import itemgetter

fields  = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid   = 0
f_count = 0
eyecolors =["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
vals = []
infile  = open("day4.txt", "r")


def sort_fields(data):
    for i in range(len(vals)):
        if   data[i][0]=="byr": byr = data[i][1]
        elif data[i][0]=="ecl": ecl = data[i][1]
        elif data[i][0]=="eyr": eyr = data[i][1]
        elif data[i][0]=="hcl": hcl = data[i][1]
        elif data[i][0]=="hgt": hgt = data[i][1]
        elif data[i][0]=="iyr": iyr = data[i][1]
        elif data[i][0]=="pid": pid = data[i][1]

    return byr, ecl, eyr, hcl, hgt, iyr, pid

def check_data(byr, ecl, eyr, hcl, hgt, iyr, pid):
    birth  = 1920 <= float(byr) <= 2002
    eye    = ecl in eyecolors
    expire = 2020 <= float(eyr) <= 2030
    hair   = hcl[0]=="#" and len(hcl)==7
    height = (hgt[-2:]=="cm" and 150<=float(hgt[:-2]) <=193) or (hgt[-2:]=="in" and 59 <=float(hgt[:-2]) <=76)
    issue  = 2010 <= float(iyr) <= 2020
    passid = len(pid) == 9

    if height and birth and issue and expire and hair and eye and passid == True:
        return True

    else:
        return False



for line in infile:
    words = line.replace(":"," ")
    words = words.split()
    if words:
        # i was doing some dumb stuff here,
        # god bless Frida for showing me the way
        for i in range(0, len(words), 2):
            """
            for j in fields:
                if words[i]==j:
                    f_count += 1
                    break
            """
            if words[i] in fields:
                f_count += 1

            vals += [[words[i], words[i+1]]]

    else:
        if f_count == len(fields):
            byr, ecl, eyr, hcl, hgt, iyr, pid = sort_fields(vals)
            if check_data(byr, ecl, eyr, hcl, hgt, iyr, pid) == True:
                valid += 1
                
        f_count  = 0
        vals = []
# Check last f_count on last line
if f_count == len(fields):
    valid += 1

print(f"Valid passports: {valid}")

infile.close()
