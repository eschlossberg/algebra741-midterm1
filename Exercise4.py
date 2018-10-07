from Permutation import Permutation
from SymmetricGroup import SymmetricGroup
from random import choice

generators = [
    Permutation({1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 1}),
    Permutation({1: 2, 2: 1, 3: 6, 4: 5, 5: 4, 6: 3})
]

# Generates the group G=<(123456),(12)(36)(45)>
G = SymmetricGroup.generate(*generators)
print(G)

# Generate the hom-set Hom([6],[2]), with functions represented as hash maps
funcs = []
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        funcs.append({
                            1: a + 1,
                            2: b + 1,
                            3: c + 1,
                            4: d + 1,
                            5: e + 1,
                            6: f + 1
                        })


def precompose(perm: Permutation, func: dict):
    # Returns func precomposed with perm
    d = {}
    for key in func.keys():
        d[perm[key]] = func[key]
    return d


def postcompose(perm: Permutation, func: dict):
    # Returns func postcompesd with perm
    d = {}
    for key in func.keys():
        d[key] = perm[func[key]]
    return d


# Take the quotient of Hom([6],[2]) by the action of G
G_Hom = []
for f in funcs:
    equiv_class = []
    # Compute the equivalence class of f
    for p in G.elements:
        pre_f = precompose(p, f)
        equiv_class.append(pre_f)
    matched = False
    # Add the equivalence class if not in G_Hom, or extend it if it is
    for eclass in G_Hom:
        if all(elem in equiv_class for elem in eclass) or \
                all(elem in eclass for elem in equiv_class):
            for elem in equiv_class:
                if elem not in eclass:
                    eclass.append(elem)
            matched = True
            break
    if not matched:
        G_Hom.append(equiv_class)

print(len(G_Hom))

# Compute the quotient of G_Hom by S_2
N = []
S2 = SymmetricGroup(2)
for equiv_class in G_Hom:
    # pick a representative of the equivalence class in G\Hom([6],[2])
    f = choice(equiv_class)
    eclass = []

    # Calculate the equivalence class in G\Hom([6],[2])/S_2
    for p in S2.elements:
        eclass.append(postcompose(p, f))

    # Add it to the list of equivalence classes
    matched = False
    for cls in N:
        if all(elem in eclass for elem in cls) or \
                all(elem in cls for elem in eclass):
            cls.extend(eclass)
            matched = True
            break
    if not matched:
        N.append(eclass)

print(N)
print(len(N))
# |N|=10
