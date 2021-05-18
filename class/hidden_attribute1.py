class A:
    def __init__(self, v):
        self._a = v + 1

a = A(0)
print(a._a)

# 1
# single underscore before variable is accessible

class A:
    def __init__(self, v):
        self.__a = v + 1

a = A(0)
print(a.__a)

# AttributeError
# double underscore before a variable makes it unaccessible

