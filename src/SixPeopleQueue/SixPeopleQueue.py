from itertools import permutations


def has_a_in_first_place(permutation):
    return permutation[0] == "A"


def has_a_before_b(permutation):
    aIndex = permutation.index("A")
    bIndex = permutation.index("B")
    return aIndex < bIndex


def has_a_neighbor_b(permutation):
    aIndex = permutation.index("A")
    if aIndex < len(permutation)-1:
        return permutation[aIndex + 1] == "B"
    if aIndex > 0:
        return permutation[aIndex - 1] == "B"
    return False


countAFirstPlace = 0.0
countABeforeB = 0.0
countANeighborB = 0.0
for c in permutations("ABCDEF", 6):
    if has_a_in_first_place(c):
        countAFirstPlace += 1
    if has_a_before_b(c):
        print(c)
        countABeforeB += 1
    if has_a_neighbor_b(c):
        countANeighborB += 1

print("countAFirstPlace")
print(countAFirstPlace)
print(countAFirstPlace/(6*5*4*3*2))

print("countABeforeB")
print(countABeforeB)
print(countABeforeB/(6*5*4*3*2))

print("countANeighborB")
print(countANeighborB)
print(countANeighborB/(6*5*4*3*2))

