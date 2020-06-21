def mysplit(strng):
    words = []
    word = ""
    for char in strng:
        if char == " ":
            if len(word) > 0:
                words.append(word)
                word = ""
        else:
            word += char
    if word:
        words.append(word)
    return words
            
# custom mysplit function

print(mysplit("To be or not to be, that is the question "))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))