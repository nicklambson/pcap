l1 = [1, 2, 3, 4]

# the below line will cause an error: name 'l' is not defined
# lt = list(map(lambda x: 2*x, l))

# The correct way to run it is to pass an iterable as the second argument.
lt = list(map(lambda x: 2*x, l1))
print(lt)

l2 = list(x*2 for x in l1)
print(l2)

# this is an equivalent way of doing the same thing