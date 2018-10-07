from Permutation import Permutation
from SymmetricGroup import SymmetricGroup
from itertools import product, combinations

V = list(product([0, 1], repeat=3))
E = set()

# Generate the graph
for x in range(len(V)):
    for y in range(len(V)):
        if x == y:
            continue
        s = 0
        for i in range(3):
            s += abs(V[x][i] - V[y][i])
        if s == 1:
            E.add((x, y))

s8 = SymmetricGroup(8)
swaps = []
# Compute the group G
for perm in s8.elements:
    valid = True
    for (x, y) in E:
        if (perm[x], perm[y]) in E:
            continue
        valid = False
        break
    if valid:
        swaps.append(perm)

G = SymmetricGroup.generate(*swaps)

print(G)
print(E)

E2 = list(combinations(E, 2))

print(len(E2))
