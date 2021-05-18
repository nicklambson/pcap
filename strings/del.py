str = 'abcdef'
def fun(s):
    del s[2]
    return s

print(fun(str))

# TypeError: 'str' object doesn't support item deletion

# Strings are immutable!