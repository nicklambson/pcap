
while True:
    text = input("Please enter text: ")
    if not text.isalpha():
        continue
    else:
        break

while True:
    shift = input("Please enter a shift value: ")
    if not shift.isdigit():
        continue
    else:
        shift = int(shift)
    if not 1 <= shift <= 25:
        continue
    else:
        break
    
cipher = ''

for char in text:
    if not char.isalpha():
        continue
    
    # uppercase chars only
    char = char.upper()
    
    # add the shift value
    code = ord(char) + shift
    
    # if it's after Z, move it to A
    if code > ord('Z'):
        code = code - 26
    
    cipher += chr(code)
    
print(cipher)