class A:
    def __init__(self):
        pass

a = A(1)
# raises TypeError exception
# 2 positional arguments given
# but only 1 expected

print(hasattr(a,"A"))
# False