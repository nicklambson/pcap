def prepare_string(text: str) -> str:
    text = text.upper()
    text = text.replace(" ", "")
    text = list(text)
    text = sorted(text)
    text = "".join(text)
    return text

def are_anagrams(text_1: str, text_2: str) -> bool:
    if prepare_string(text_1) == prepare_string(text_2):
        print(f"{text_1} and {text_2} are anagrams.")
        return True
    else:
        print(f"{text_1} and {text_2} are NOT anagrams.")
        return False

text_1 = input("Please enter the first word to compare:")

text_2 = input("Please enter the second word to compare:")

are_anagrams(text_1, text_2)