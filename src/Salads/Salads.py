from itertools import combinations_with_replacement

count = 0
for c in combinations_with_replacement("TBL", 4):
    print("".join(c))
    count += 1
print(count)