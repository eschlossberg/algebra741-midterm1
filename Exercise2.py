from Permutation import Permutation
from SymmetricGroup import SymmetricGroup
import IllegalActionException

# Generating set
maps = [
    {1:2,2:3,3:1},
    {2:3,3:4,4:2},
]


# Generate subgroup
old_perms = []
perms = []
for m in maps:
    try:
        perms.append(Permutation(m))
    except IllegalActionException:
        print("Illegal Action: ", str(m))
G = SymmetricGroup.generate(*perms)

print(G)
# Results show that G is the alternating group A_4


def display_cosets(cosets):
    for coset in cosets:
        print(str(coset))


# Calculate H1=<(123)>
H1 = SymmetricGroup.generate(perms[0])
print("H1 Cosets:")
display_cosets(G.cosets(*H1.elements))

# Calculate H2=<(12)(34)>
p = {1:2,2:1,3:4,4:3}
H2 = SymmetricGroup.generate(Permutation(p))
print("H2 Cosets:")
display_cosets(G.cosets(*H2.elements))

# Calculate H3=<(12)(34),(13)(24),(14)(23)>
H3 = SymmetricGroup.generate(*[Permutation({1:2,2:1,3:4,4:3}),
                               Permutation({1:3,2:4,3:1,4:2}),
                               Permutation({1:4,2:3,3:2,4:1})])
print("H3 Cosets:")
display_cosets(G.cosets(*H3.elements))
