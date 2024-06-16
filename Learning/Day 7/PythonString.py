# Exercise 1A: Write a program to create a new string made of an input string’s first, middle, and last character.

# str1 = "surbhibansal"

# res = str1[0]

# len1 = len(str1)

# mid = int(len1/2)

# res = res + str1[mid]
# res = res + str1[len1-1]

# print(res)

# Exercise 1B: Create a string made of the middle three characters
# str1 = "JhonDipPeta"

# str2 = "JaSonAy"

# len1 = len(str1)
# len2 = len(str2)

# mid = int(len1/2)
# mid_next = int(len1/2)+1
# mid_prev = int(len1/2)-1

# print(str1[mid_prev] + str1[mid] + str1[mid_next])

# mid2 = int(len2/2)
# mid_next2 = int(len2/2)+1
# mid_prev2 = int(len2/2)-1
# print(str2[mid_prev2] + str2[mid2] + str2[mid_next2])

# Exercise 2: Append new string in the middle of a given string
# s1 = "Ault"
# s2 = "Kelly"

# # AuKellylt

# len = len(s1)
# mid = int(len/2)
# x = s1[:mid:]
# x = x + s2
# x = x + s1[mid:]
# print(x)

#Exercise 3: Create a new string made of the first, middle, and last characters of each input string

# s1 = "America"
# s2 = "Japan"

# # AJrpan

# mid1 = int(len(s1)/2)
# mid2 = int(len(s2)/2)

# start1 = s1[0]
# start2 = s2[0]

# x1 = s1[mid1]
# x2 = s2[mid2]

# last1 = s1[len(s1)-1]
# last2 = s2[len(s2)-1]

# final1 = start1+start2+x1+x2+last1+last2
# print(final1)

# Exercise 4: Arrange string characters such that lowercase letters should come first
# str1 = "PyNaTive"
# str2 = []
# str3 = []
# for char in str1:
#     if char.islower():
#         str2.append(char)
#     else:
#         str3.append(char)
# print(''.join(str2 + str3))

# Exercise 5: Count all letters, digits, and special symbols from a given string
# str1 = "P@#yn26at^&i5ve"

# print("Total counts of chars, digits, and symbols")

# Chars =  ""
# Digits = ""
# Symbol = ""

# char_count = 0
# digit_count = 0
# symbol_count = 0
# for i in str1:
#     if i.isalpha():
#         char_count = char_count+1
#     elif i.isdigit():
#         digit_count+=1
#     else: 
#         symbol_count+=1
# print(f"Total counts of chars{char_count}, digits {digit_count}, and symbols {symbol_count}" )
# print("Total counts of chars: {}, digits: {}, and symbols: {}".format(char_count, digit_count, symbol_count))


# Exercise 6: Create a mixed String using the following rules

# s1 = "Abc"
# s2 = "Xyz"

# output = "AzbycX"

# s1_length = len(s1)
# s2_length = len(s2)

# print(s1_length, s2_length)

# length = s1_length if s1_length > s2_length else s2_length
# result = ""

# s2 = s2[::-1]

# for i in range(length):
#     if i < s1_length:
#         result = result+ s1[i]
#     if i < s2_length:
#         result = result+ s2[i]

# print(result)

# Exercise 7: String characters balance Test

# def balance_test(s1, s2):
#     flag = True
#     for i in s1:
#         if i in s2:
#             continue
#         else:
#             flag = False
#     return flag

# s1 = "Yn"
# s2 = "PYnative"
# flag = balance_test(s1, s2)
# print(flag)


# s1 = "Ynf"
# s2 = "PYnative"
# flag = balance_test(s1, s2)

# print(flag)

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# str1 = "Welcome to USA. usa awesome, isn't it?"
# str3 = "USA"
# count = 0
# str2 = str1.split()
# for i in str2:
#  if i.lower() == str3.lower():
#    count+=1
#  if i.upper() == str3.upper():
#     count+=1
# print(count)

# Exercise 9: Calculate the sum and average of the digits present in a string

# str1 = "PYnative29@#8496"
# str2 = []
# count = 0
# total = 0

# for char in str1:
#     if char.isdigit():
#         print(char)
#         total+= int(char)
#         count+=1

# avg = total/count
# print(total)
# print(avg)

# Exercise 10: Write a program to count occurrences of all characters within a string
# str1 = "Apple"
# dict_count = {}
# for char in str1:
#     count = str1.count(char)
#     dict_count[char] = count
# print(dict_count)

# Exercise 11: Reverse a given string
# str1 = "PYnative"

# print(str1[::-1])

# Exercise 12: Find the last position of a given substring
# str1 = "Emma is a data scientist who knows Python. Emma works at google."

# str2 = "Emma"

# index = str1.rfind(str2)
# print(index)

# Exercise 13: Split a string on hyphens
# str1 = "Emma-is-a-data-scientist"

# res = str1.split("-")

# for sub in res:
#     print(sub)

# Exercise 14: Remove empty strings from a list of strings
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# res_list = []
# print(list(filter(None, str_list)))

# for i in str_list:
#     if i:
#         res_list.append(i)
# print(res_list)

# Exercise 15: Remove special symbols / punctuation from a string
# str1 = "/*Jon is @developer & musician"
# str2 = ""

# for char in str1:
#     if char.isalnum() or char.isspace():
#         str2+=char
# str2 = ' '.join(str2.split())
# print(str2)

# Exercise 16: Removal all characters from a string except integers
# str1 = 'I am 25 years and 10 months old'
# str2 = ""

# for char in str1:
#     if char.isdigit():
#         str2+=char
# print(' '.join(str2.split()))

# Exercise 17: Find words with both alphabets and numbers
# str1 = "Emma25 is Data scientist50 and AI Expert"
# print("The original string is : " + str1)

# res = []
# # split string on whitespace
# temp = str1.split()

# # Words with both alphabets and numbers
# # isdigit() for numbers + isalpha() for alphabets
# # use any() to check each character

# for item in temp:
#         if any(char.isdigit() for char in item) and any(char.isalpha() for char in item):
#          res.append(item)

# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)

# Exercise 18: Replace each special symbol with # in the following string
# import string
# str1 = '/*Jon is @developer & musician!!'

# for i in string.punctuation:
#     str1 = str1.replace(i, "#")
# print(str1)









        



    
