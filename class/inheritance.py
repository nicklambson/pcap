class A:
    v = 2

class B(A):
    v = 1

class C(B):
    pass

o = C()
print(o.v)

# Inheritance follows left to right for multiple inheritance
# and bottom to top for vertical inheritance

# answer = 1