# # Exercise 1: Accept numbers from a user
# num1 = int(input("Enter First number:" ))
# num2 = int(input("Enter Second number: "))

# def mul(num5, num6):
#     mul = num5*num6
#     return mul

# print(mul(num1,num2))

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# a = "Name"
# b = "Is"
# c = "James"
# print(a + "**" + b + "**" + c)
# print(a,b,c, sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting

# num = 100
# print('%o' %num)

# Exercise 4: Display float number with 2 decimal places using print()
# num = 458.541315

# print('{:.2f}'.format(num))

# Exercise 5: Accept a list of 5 float numbers as an input from the user
# num1 = float(input("Enter First number:" ))
# num2 = float(input("Enter First number:" ))
# num3 = float(input("Enter First number:" ))
# num4 = float(input("Enter First number:" ))
# num5 = float(input("Enter First number:" ))
# list = []
# list.append(num1)
# list.append(num2)
# list.append(num3)
# list.append(num4)
# list.append(num5)
# print(list)

# list=[]
# for i in range(0,5):
#     item = float(input("Enter number:" ))
#     list.append(item)
# print(list)

# Exercise 6: Write all content of a given file into a new file by skipping line number 5

# with open("test.txt", 'r') as file:
#     lines = file.readlines()

# # Open the file in write mode ('w')
# with open("test.txt", 'w') as file:
#     for line in lines:
#         if line.strip() == 'line5':
#             continue
#         file.write(line)
# with open("test.txt", 'r') as file:
#     print(file.read())

# Exercise 7: Accept any three string from one input() call
# str1, str2, str3 = input("Enter three names: ").split()
# print("Name1:", str1)
# print("Name2:", str2)
# print("Name3", str3)

# Exercise 8: Format variables using a string.format() method.

# totalMoney = 1000
# quantity = 3
# price = 450

# output = "I have {0} dollars so I can buy {2} football for {2:2f} dollars."
# print(output.format(totalMoney, quantity, price))

# Exercise 9: Check file is empty or not

# with open("test.txt", 'r') as file:
#     if file.read() == None:
#         print("File is empty")
#     else:
#         print("File is not empty")

# Exercise 10: Read line number 4 from the following file
# with open("test.txt", 'r') as file:
#     lines = file.readlines()
#     print(lines[3])



