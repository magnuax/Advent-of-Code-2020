import numpy as np

def tree_encounters(map, right, down):
    trees   = 0
    steps_r = 0

    with open(map, "r") as infile:
        for line in infile:

            if line[steps_r] == "#":
                trees += 1

            steps_r += right

            if steps_r >= 31:
                steps_r -= 31

            if down > 1:
                for i in range(1, down):
                    infile.readline()

    return trees


trees = []
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

for i in slopes:
    trees.append(tree_encounters("day3.txt", i[0], i[1]))

tree_prod = np.prod(trees)


print(f"Tree encounters: {trees} \nTree product: {tree_prod}")
