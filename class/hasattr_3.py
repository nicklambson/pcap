class A:
    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A, 'a'))
print(hasattr(A, 'A'))

# False
# True
# hasattr only works for class variables (A)
# not for instance variables (A)