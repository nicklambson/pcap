# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78,
}

key = 'sample'


if word_freq[key] != None:
    print(f"Yes, key: '{key}' exists in dictionary.")
else:
    print(f"No, key: '{key}' does not exist in dictionary.")
if key in word_freq:
    print(f"Yes, key: '{key}' exists in dictionary.")
else:
    print(f"No, key: '{key}' does not exist in dictionary.")
if word_freq.get(key):
    print(f"Yes, key: '{key}' exists in dictionary.")
else:
    print(f"No, key: '{key}' does not exist in dictionary.")
if key in word_freq.keys():
    print(f"Yes, key: '{key}' exists in dictionary.")
else:
    print(f"No, key: '{key}' does not exist in dictionary.")
