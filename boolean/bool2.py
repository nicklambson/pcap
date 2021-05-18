y = 1
z = 2

a = y < z                              # True
b = y < z or z > y                     # True
c = y < z or z > y and y > z           # True
d = y < z or z > y and y > z or z < y  # True

l =                             y > z  # False
m =                    y > z or z < y  # False
n =          z > y and y > z or z < y  # False
o = y < z or z > y and y > z or z < y  # True

# 
# Expressions are evaluated lazily from right to left in this case
# True

print(f"{a=}", f"{b=}", f"{c=}", f"{d=}", f"{l=}", f"{m=}", f"{n=}", f"{o=}", sep="\n")

# True

