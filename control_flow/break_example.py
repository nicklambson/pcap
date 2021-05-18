i = 4

while i > 0:
    print("*")
    i -= 2
    if i == 2:
        break
else:
    print("*")

# The else block will only execute if the break clause is not triggered
# in the case of i = 5, the code will print * at 5, 3, 1, and then will go to the else statement.
# In that else statement, another * will be printed.