# Exercise 1: Calculate the multiplication and sum of two numbers

# num1 = 30
# num2 = 40

# if num1*num2 < 1000:
#     print(num1*num2)
# else: 
#     print(num1+num2)

# Exercise 2: Print the sum of the current number and the previous number

# for i in range(10):
#     a = i + (i-1)
#     print("Printing current and previous number sum in a range(10)")
#     print("Current number : " , i)
#     print("Previous Number:", (i-1))
#     print("sum", a)
#     # print("'Current number : ' , %i, 'Previous Number', %(i-1), 'Sum: ' %a")

# Exercise 3: Print characters from a string that are present at an even index number
# str = "pynative"
# print("Printing only even index chars")
# start = 0
# stop = len(str)-1
# step=2

# for s in range(start, stop, step):
#     print(str[s])

# Exercise 4: Remove first n characters from a string

# def remove_chars(word, n):
#     print("Original word: ", word)
#     x = word[n:]
#     return x


# print(remove_chars("pynative", 4))
# print(remove_chars("pynative", 2))

# Exercise 5: Check if the first and last number of a list is the same

# def first_last_same(list1):
#     print("Given list: " , list1)
#     if list1[0] == list1[-1]:
#         return True
#     else:
#         return False 
        

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]


# print(first_last_same(numbers_x))
# print(first_last_same(numbers_y))

# Exercise 6: Display numbers divisible by 5 from a list


# list1 = [10, 20, 33, 46, 55]

# for i in list1:
#     if i%5 == 0:
#         print(i)

# Exercise 7: Return the count of a given substring from a string

# str_x = "Emma is good developer. Emma is a writer"

# sub = "Emma"
# count = 0

# def string_count():
#  global count
#  for x in str_x.split():
#     if x == sub:
#         count = count+1
#  return count

# print(string_count())

#  Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# rows = 6

# for i in range(rows):
#     for j in range(i):
#         print(i, end=' ')
#     print('')
    
#  Exercise 9: Check Palindrome Number
# number = 1331342

# rev_number = str(number)[::-1]
# print(rev_number)

# Exercise 10: Create a new list from two list using the following condition

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# list3 = []
# for i in list1:
#     if i % 2 !=0:
#         list3.append(i)

# for j in list2:
#     if j % 2==0:
#         list3.append(j) 
# print(list3)      
# 
# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

num = 7536
# rev_num  = str(num)[::-1]

# while(num>0):
#     digit = num % 10
#     print(digit)
#     num = num // 10
#     print(num)
#     print(digit, end=" ")

# Exercise 12: Calculate income tax for the given income by adhering to the rules below

# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
    
# For example, suppose the taxable income is 45000, and the income tax payable is

# number = 45000
# tax1 = 0
# tax2 = 0
# tax3 = 0

# if number <= 10000:
#     tax1 = number * 0
#     print(tax1)
# elif number <= 20000:
#     tax2 = number-10000 * 0.10
#     print(tax2)
# else: 
#     tax1 = number * 0
#     tax2 = number-10000 * 0.10
#     tax3= (number-20000)*0.20
#     print(tax1+tax2+tax3)

# Exercise 13: Print multiplication table from 1 to 10

# for i in range(1,11):
#     # print(i)
#     for j in range(1,11):
#         print(i*j, end=" ")
#     print("\t\t")

    
# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *


# for i in range(6, 0, -1):
#     # print("*")
#     for j in range(0, i-1):
#         print("*", end=' ')
#     print(' ')

# for i in range(rows):
#     for j in range(-i):
#         print(i, end=' ')
#     print('')

# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    exp = base ** exp
    return exp

print(exponent(2,5))
print(exponent(5,4))
