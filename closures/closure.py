def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r() + s())

# r will be defined as a function that returns *
# s will be defined as a function that returns **
# together, they will print ***