def digit_of_life(digit: int) -> int:
    print(f"Digit of life from {digit} is ", end="")
    while digit > 9:
        digit = list(str(digit))
        digit = sum([int(x) for x in digit])
    print(f"{digit}.")
    return digit
                    

while True:
    digit = input("Please enter a birthday in any format YYYYMMDD YYYYDDMM MMDDYYYY: ")
    if not digit.isdigit():
        continue
    else:
        digit = int(digit)
        break
    
digit_of_life(digit)

# Scenario
# Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 is the digit we searched for and found.

# Your task is to write a program which:

# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
# outputs the Digit of Life for the date.
# Test your code using the data we've provided.

# Test data
# Sample input:

# 19991229

# Sample output:

# 6