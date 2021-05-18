class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
 
print()

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")


# except will match only the *first matching exception class*
# even if it's a super class.
# for example, D is a subclass of C, which is a subclass
# of B. When the D exception occurs, it matches the D subclass.
# Its super classes also match the following lines, but D
# has already been executed. So only D is run. BCD

# In the second example, each subclass class matches superclass B,
# So B is run, and only the B code is run. BBB