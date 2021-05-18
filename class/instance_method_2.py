class A:
    A = 1
    def __init__(self, v=2):
        self.v = v + A.A
        A.A += 1

    def set(self, v):
        self.v += v
        A.A += 1
        return

a = A()
a.set(2)
print(a.v)

# 5
# a is instantiated
# through __init__, self.v becomes 3 and A.A. becomes 2
# through set, self.v becomes 5 and A.A. becomes 3