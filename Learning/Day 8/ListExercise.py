# Exercise 1: Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
# print(list1[::-1])

# Exercise 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# result = zip(list1, list2)
# list3 = [i + j for i,j in result]
# print(list3)

# Exercise 3: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# result = []

# result = [x * x for x in numbers]
# print(result)

# Exercise 4: Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# res = []
# # ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# res = [x + y for x in list1 for y in list2]
# print(res)

# Exercise 5: Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# # 10 400
# # 20 300
# # 30 200
# # 40 100

# for x, y in zip(list1, list2[::-1]):
#     print(x,y)
        
# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list2 = []
# list2 = [i for i in list1 if i]

# res = list(filter(None,list1))
# print(res)

# # for i in list1:
# #     if i:
# #         list2.append(i)
# print(list2)

# Exercise 7: Add new item to list after a specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# output = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# list1[2][2].append(7000)
# print(list1)

# Exercise 8: Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub_list = ["h", "i", "j"]

# list1[2][1][2].extend(sub_list)
# print(list1)

# Exercise 9: Replace list’s item with new value if found
# list1 = [5, 10, 15, 20, 25, 50, 20]
# find = 20
# rep = 200

# # for i in range(len(list1)):
# #     if list1[i] == 20:
# #         list1[i] = 200
# # print(list1)

# index = list1.index(20)
# list1[index] = 200
# print(list1)

# Exercise 10: Remove all occurrences of a specific item from a list.

# list1 = [5, 20, 15, 20, 25, 50, 20]
# i = 0
# while i < len(list1):
#     if list1[i] == 20:
#         list1.pop(i)
#         continue
#     else:
#         i+=1
# print(list1)


# while 20 in list1:
#     list1.remove(20)

# print(list1)
