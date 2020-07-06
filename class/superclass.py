class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = 2

object = B()
print(object.a)
print(object.b)

# If B is a subclass of A, then it should init A and pass itself.