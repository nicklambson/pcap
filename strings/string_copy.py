str1 = 'string'
str2 = str1[:]

print(f"{len(str1)=}")
print(f"{len(str2)=}")
print(f"{str1 == str2=}")
print(f"{str1 is str2=}")

str3 = str2

print(f"{str2 == str3=}")
print(f"{str2 is str3=}")


# str1 and str2 are different but equal strings
# They are not different names for the same string