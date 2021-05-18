class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C,A)) # True
print(issubclass(C,B)) # True
print(issubclass(C,C)) # True

print(issubclass(B,A)) # True
print(issubclass(B,B)) # True
print(issubclass(B,C)) # False

print(issubclass(A,A)) # True
print(issubclass(A,B)) # False
print(issubclass(A,C)) # False

# Evaluating if a class is a subclass of itself always returns True
