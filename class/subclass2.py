class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        # self.a = 2
        self.b = 3

# use super() to access the methods of the parent class
# or A.__init__(self)
# use super().__init__() to initialize from the parent class
# If it's not initialized, b.a will not unless called explicitly from B's __init__()


a = A()
b = B()

print(a.a)

print(b.a)
print(b.b)