from itertools import combinations
import random

lst = []
for i in range(5):
    lst.append(random.randint(1,10))
for i in combinations(lst, 3):
    if (i[0]+i[1]+i[2]) % 10 == 0:
        print(i)
        print("made")

