class FinFieldMatrix:
    def __init__(self, n: int, r1: list, r2: list):
        """
        Creates a matrix over a finite field of order n with rows r1 and r2 respectively
        :param n: order of the finite field
        :param r1: row 1
        :param r2: row 2
        """
        self.a = r1[0] % n
        self.b = r1[1] % n
        self.c = r2[0] % n
        self.d = r2[1] % n
        self.n = n

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and \
            self.c == other.c and self.d == other.d and self.n == other.n

    def __mul__(self, other):
        if other.n != self.n:
            raise ArithmeticError
        a = (self.a * other.a + self.b * other.c) % self.n
        b = (self.a * other.b + self.b * other.d) % self.n
        c = (self.c * other.a + self.d * other.c) % self.n
        d = (self.c * other.b + self.d * other.d) % self.n
        return FinFieldMatrix(self.n, [a, b], [c, d])

    def __str__(self):
        st = "[[" + str(self.a) + ", " + str(self.b) + "]\n[" + str(self.c) + ", " + str(self.d) + "]]"
        return st


# Generators found at https://people.maths.bris.ac.uk/~matyd/GroupNames/1/GL(2,3).html
generators = [
    FinFieldMatrix(3, [2, 1], [1, 1]),
    FinFieldMatrix(3, [1, 1], [1, 2]),
    FinFieldMatrix(3, [1, 2], [0, 1]),
    FinFieldMatrix(3, [2, 0], [0, 1])
]

# Generate the group GL_2(3)
old_mats = []
mats = list(generators)
while True:
    for x in old_mats:
        for y in old_mats:
            if x*y not in mats:
                mats.append(x*y)
    if old_mats == mats:
        break
    old_mats = mats.copy()

# Find pairs of matrices (x, y) such that yxy=x
pairs = []
for x in mats:
    for y in mats:
        if y*x*y == x:
            if (x, y) not in pairs:
                pairs.append((x, y))

for pair in pairs:
    print(pair[0], pair[1])

print(len(pairs))
