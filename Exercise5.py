from Permutation import Permutation
from SymmetricGroup import SymmetricGroup
from itertools import product, combinations
from random import choice

V = list(product([0, 1], repeat=3))
E = []

# Generate the graph
for x in range(len(V)):
    for y in range(len(V)):
        if x == y:
            continue
        s = 0
        for i in range(3):
            s += abs(V[x][i] - V[y][i])
        if s == 1 and {x + 1, y + 1} not in E:
            E.append({x + 1, y + 1})

s8 = SymmetricGroup(8)
swaps = []
# Compute the group G
for perm in s8.elements:
    valid = True
    for edge in E:
        [x, y] = list(edge)
        if {perm[x], perm[y]} in E:
            continue
        valid = False
        break
    if valid:
        swaps.append(perm)

G = SymmetricGroup.generate(*swaps)

print(G)

E2 = list(combinations(E, 2))
print(E2)

print(len(E2))
# Identify each element with its image in the map (x_1,x_2,x_3)|->1+x_1+x_2*2+x_3*2^2
# in order to deal with permutations easier
new_V = []
for v in V:
    new_V.append(1+v[0]+v[1]*2+v[2]*4)
V = new_V


def permute(p: Permutation, obj):
    e1, e2 = obj
    e1 = list(e1)
    e2 = list(e2)
    e1_new = {p[e1[0]], p[e1[1]]}
    e2_new = {p[e2[0]], p[e2[1]]}
    return frozenset(e1_new), frozenset(e2_new)


# Calculate the number of orbits. Note that any element of _G Hom((E,2),V) must preserve orbits
# Thus we can look at orbits instead of elements for the calculation
# Otherwise the calculation would be on the order of 8^66, which would exceed the heat death of the universe
orbits = []
for e in E2:
    orbit = set()
    for g in G.elements:
        pg = frozenset(permute(g, e))
        if pg not in orbit:
            orbit.add(pg)
    if orbit not in orbits:
        orbits.append(orbit)
print("There are", len(orbits), "orbits in (E,2) of sizes:")
for orbit in orbits:
    print(int(len(orbit)))

product = 1
for orbit in orbits:
    rep = choice(list(orbit))  # The representative of the orbit
    valid_maps = 0
    for v in V:
        # Consider the map sending the representative to a given vertex
        mapping = {rep: v}
        valid = True
        # Check chosen mapping holds under the group action
        for perm in G.elements:
            permuted_rep = frozenset(permute(perm, rep))
            permuted_vert = perm[v]
            if permuted_rep in mapping.keys() and \
                    mapping[permuted_rep] != permuted_vert:
                valid = False
                print("Invalid mapping:", perm, list(rep), list(permuted_rep), v, permuted_vert, mapping[permuted_rep])
                break
            elif permuted_rep not in mapping.keys():
                mapping[permuted_rep] = permuted_vert
        if valid:
            valid_maps += 1
    product *= valid_maps
print(product)
