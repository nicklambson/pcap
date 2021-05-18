from collections import defaultdict

counts = defaultdict(int)

with open("count_chars.txt", "r", encoding="utf-8") as f:
    text = f.read()
    for char in text:
        counts[char.lower()] += 1

alphabetical_order = sorted(counts.items())

for pair in alphabetical_order:
    print(pair[0], "->", pair[1])

frequency_order = sorted(counts.items(), key=lambda frequency: frequency[1])

for pair in reversed(frequency_order):
    print(pair[0], "->", pair[1])