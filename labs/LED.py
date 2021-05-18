def print_nums(to_print: list):
    for i in range(0, 5):
        row = ""
        for num in to_print:
            chunk = get_num_chunk(num, i)
            row += chunk
            row += " "
        print(row)
            
def get_num_chunk(num, i):
    rows = nums[num].split("\n")
    return rows[i]


nums = ["""###
# #
# #
# #
###""",

"""#
#
#
#
#""",

"""###
  #
###
#  
###""",

"""###
  #
###
  #
###""",
    
"""# #
# #
###
  #
  #""",
    
  """###
#  
###
  #
###"""]

number = 12345

num_as_str = str(number)

to_print = [int(x) for x in num_as_str]

print(to_print)
print_nums(to_print)

