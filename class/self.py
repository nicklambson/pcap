class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g():
        return self.f()

a = A()
print(a.g())

# TypeError: g() takes 0 positional arguments but 1 was given