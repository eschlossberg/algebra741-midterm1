from Permutation import Permutation
from SymmetricGroup import SymmetricGroup

generators = [
    Permutation({1:2,2:3,3:4,4:5,5:6,6:1}),
    Permutation({1:2,2:1,3:6,4:5,5:4,6:3})
]

G = SymmetricGroup.generate(*generators)
print(G)

S6 = SymmetricGroup(6)

S6_G = S6.cosets(*G.elements)
for cos in S6_G:
    print(cos)
print(len(S6_G))
