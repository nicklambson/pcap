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
# inheritance works bottom to top
# and left to right