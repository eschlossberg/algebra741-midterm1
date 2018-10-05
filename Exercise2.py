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

g = SymmetricGroup.generate(*perms)

print(g)
