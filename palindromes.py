def is_palindrome(text: str) -> bool:
    prepped = text.replace(" ", "").lower()
    for i, character in enumerate(prepped):
        neg_index = (i * -1) - 1
        if character == prepped[neg_index]:
            continue
        else:
            print("text is not a palindrome.")
            return False
    else:
        print("text is a palindrome.")
        return True
    
def is_palindrome_2(text: str) -> bool:
    # remove all spaces...
    text = text.replace(' ','')
    # ... and check if the word is equal to reversed itself
    if len(text) > 1 and text.upper() == text[::-1].upper():
        print("It's a palindrome")
        return True
    else:
        print("It's not a palindrome")
        return False
        
user_input = input("Please enter some text:")

is_palindrome_2(user_input)