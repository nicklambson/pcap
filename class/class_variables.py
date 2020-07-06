class A:
    X = 0
    def __init__(self, v=0):
        self.Y = v
        A.X += v

a = A()
b = A(1)
c = A(2)
print(c.X)

# 3
# class variable is common among
# all the objects of that class
# it is accessed whenever any object
# of that class is used