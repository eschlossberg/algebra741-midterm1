from Permutation import Permutation
from itertools import permutations
from random import choice


class SymmetricGroup:
    """
    Python class representing the symmetric group on n elements
    To create the symmetric group on an arbitrary set, simply
    create a list and consider the symmetric group on the indices
    of the list.
    """

    def __init__(self, n: int, subgroup=False, elements=list()):
        self.n = n  # the size of the symmetric group
        self.elements = set([])  # the elements of the group

        if subgroup:
            for elmnt in elements:
                self.elements.add(elmnt)
            return

        # Generate the permutations
        perms = list(permutations([i+1 for i in range(n)]))
        for perm in perms:
            d = {}
            for i in range(n):
                d[i+1] = perm[i]
            self.elements.add(Permutation(d))
        p = choice(list(self.elements))
        self.id = ~p*p

    def __len__(self):
        """
        :return: The order of the group
        """
        return len(self.elements)

    def __str__(self):
        """
        :return: A string on which every new line is the set of permutations which
        swap the same number of elements
        """
        s = [[] for _ in range(self.n)]
        for p in self.elements:
            s[len(p) - 1].append(str(p))
        out_str = ""
        for st in s:
            if len(st) == 0:
                continue
            st.sort()
            out_str += "{"
            for perm in st:
                out_str += str(perm)
                if perm != st[-1]:
                    out_str += ", "
            out_str += "}\n"
        return out_str

    @staticmethod
    def generate(*generators: Permutation):
        """
        Returns a subgroup of the symmetric group on n elements generated by the generators
        :param generators: an iterable of permutations that generate the subgroup
        :return: the subgroup generated by the generators
        """
        old_perms = []
        perms = list(generators)
        while True:
            for x in old_perms:
                for y in old_perms:
                    if x*y not in perms:
                        perms.append(x*y)
            if old_perms == perms:
                break
            old_perms = perms.copy()
        g = SymmetricGroup(max(len(perm) for perm in perms) + 1, subgroup=True, elements=perms)
        return g
