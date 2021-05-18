def readint(prompt, min, max):
    user_text = input(prompt)
    try:
        user_text = int(user_text)
    except:
        return "Error: wrong input"
    if min <= user_text <= max:
        return f"The number is: {user_text}"
    else:
        return f"Error: The value is not within permitted range ({min}..{max})"

v = readint("Enter a number from -10 to 10: ", -10, 10)

print(v)