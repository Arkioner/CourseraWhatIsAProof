import itertools as it

count = 0
for d in it.product(range(10), repeat=4):
    if sum(d) == 10:
        print(d)
        count += 1
print(count)