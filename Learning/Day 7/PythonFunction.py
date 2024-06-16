# Exercise 1: Create a function in Python

# def arg(name, age):
#     print(name, age)

# arg("surbhi", "16")

#Exercise 2: Create a function with variable length of arguments

# def func1(*args):
#     for i in args:
     
#      print(i)
# print("Printing values")
# func1(10, 20, 30 )
# func1(10, 20)

# Exercise 3: Return multiple values from a function - return both addition and subtraction in a single return call.

# def calculation(a, b):
#     add = a+b
#     sub = a-b
#     return (add, sub)

# res = calculation(40, 10)
# print(res)

# Exercise 4: Create a function with a default argument
# def showEmployee(Name, salary= 9000):
#         print("Name:", Name, "salary:", salary)

# showEmployee("Ben", 12000)
# showEmployee("Jessa")

# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

# def out(a,b):
#     def add(a,b):
#         return a+b
#     result = add(a,b)
#     result+=5
#     return result

# print(out(20,15))

# Exercise 6: Create a recursive function/ Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# def rec_add(num):
#     if num:
#         return num + rec_add(num-1)
#     else: 
#         return 0
    
# print(rec_add(10))

# Exercise 7: Assign a different name to function and call it through the new name

# def display_student(name, age):
#     print(name, age)
# show_student = display_student
# show_student("Emma", 26)
# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# print(list(range(4,30,2)))

# Exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# print(max(x))
# print(min(x))





    




    
