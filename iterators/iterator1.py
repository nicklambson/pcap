def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c

for x in I():
    print(x, end="")

# answer: 'ace'
# skip by 2s