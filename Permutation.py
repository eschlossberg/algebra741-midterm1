from IllegalActionException import IllegalActionException


class Permutation:
    """
    Permutations on a finite set may be considered as lookups in a special hash table
    with the properties
     1. all values are unique
     2. the set of keys equals the set of values, and
     3. the lookup of a value not in the hash table returns the same object.
    """
    def __init__(self, action: dict):
        # raise an exception if the keys and values are not in bijection
        if set(action.keys()) != set(action.values()):
            raise IllegalActionException(str(action))
        self.action = action

    def __getitem__(self, item):
        """
        Permutation action is the same as table lookup
        :param item: object to be acted on
        :return: the object after the permutation
        """
        if item not in self.action.keys():
            return item
        return self.action[item]

    def __mul__(self, other):
        """
        Composition is given by building a new hash table by repeated lookups
        :param other: the other permutation being multiplied (on the right)
        :return: a new Permutation object with values given by composition
        """
        keys = set(self.action.keys()).union(other.action.keys())
        new_map = dict()
        for key in keys:
            new_map[key] = self[other[key]]
        return Permutation(new_map)

    def __invert__(self):
        """
        Inverse is given by swapping the (key,value)-pairs in the hash map
        :return: the inverse of the permutation
        """
        kv_pairs = self.action.items()
        new_map = {}
        for (k, v) in kv_pairs:
            new_map[v] = k
        return Permutation(new_map)

    def __lt__(self, other):
        if len(self.action) < len(other.action):
            return True
        elif len(self.action) > len(other.action):
            return False
        else:
            if hasattr(list(self.action.keys())[0], "__lt__"):
                keys = list(self.action.keys())
                keys.sort()
                for key in keys:
                    if key not in list(other.action.keys()):
                        return True
        return False

    def __eq__(self, other):
        """
        Two permutations are equal if they act the same pointwise
        :param other: the other permutation to compare
        :return: true iff the two permutations are the same, false otherwise
        """
        keys = list(self.action.keys())
        keys.extend(other.action.keys())
        for key in keys:
            if self[key] != other[key]:
                return False
        return True

    def __len__(self):
        """
        For testing purposes only
        :return: the number of elements not fixed by the permutation
        """
        le = len(self.action)
        for k in self.action:
            if k == self.action[k]:
                le -= 1
        return le if le > 0 else 1

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        """
        :return: The permutation as a product of disjoint cycles
        """
        shift = lambda l, n : l[n:] + l[:n]
        keys = list(self.action.keys())
        if hasattr(keys[0], "__lt__"):
            keys.sort()

        out = []
        while len(keys) > 0:
            out.append([])
            key = keys.pop(0)
            out[-1].append(key)
            cur = self.action[key]
            while cur != key:
                keys.remove(cur)
                if cur != self.action[cur]:
                    out[-1].append(cur)
                cur = self.action[cur]

        out_str = ""
        for i in range(len(out)):
            if len(out[i]) <= 1:
                continue
            cycle = "("
            if hasattr(out[i][0], '__lt__'):
                index = out[i].index(min(out[i]))
                out[i] = shift(out[i], -1*index)
            for j in range(len(out[i])):
                cycle += str(out[i][j])
            cycle += ")"
            out_str += cycle
        return out_str if len(out_str) > 0 else "(1)"

    def act(self, l: list):
        """
        Permutes a list by acting on the indices
        :param l: the list to be permuted
        :return: the new list after each element has been permuted
        """
        if max(self.action.keys()) > len(l):
            raise IllegalActionException
        new_list = []
        for i in range(len(l)):
            new_list.append(l[self[i] - 1])
        return new_list
