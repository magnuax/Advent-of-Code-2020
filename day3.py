
trees   = 0
steps_r = 0

with open("day3.txt", "r") as infile:
    for line in infile:

        if line[steps_r] == "#":
            trees += 1

        steps_r += 3

        if steps_r >= 31:
            steps_r -= 31

print(f"Tree encounters: {trees}")
