class A:
    def a(self):
        print('a')

class B(A):
    def a(self):
        print('b')

class C(B,A):
    def c(self):
        self.a()

o = C()
o.c()

# answer = 'b'
# inheritance prioritizes bottom over top
# and left over right

print(issubclass(C, A))
print(issubclass(C, B))

# C is a subclass of B and of A. Both print true