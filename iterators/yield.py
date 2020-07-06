def fun(n):
    s = "+"
    for i in range(n):
        # print(f"{i=}")
        s += s
        # print(f"{s=}")
        yield s

for x in fun(2):
    # print(f"{x=}")
    print(x, end="")

# range starts with 0 and ends before the number
# x yields ++ the first time
# then ++++ the second time
# for a total of ++++++