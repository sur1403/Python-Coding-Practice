#Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]

# l3 = []
# for i in l1[1:7:2]:
#     l3.append(i)
# for j in l2[0:7:2]:
#     l3.append(j)
# print("Final list is: ", l3)


#Exercise 2: Remove and add item in a list

# l1 = [34, 54, 67, 89, 91, 43, 94]

# element = l1.pop(4)
# print(element, l1)

# l1.insert(2, element)
# print(l1)

# l1.append(element)
# print(l1)

#Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# l1= []
# l1 = sample_list[2::-1]
# l2 = sample_list[5:2:-1]
# l3 = sample_list[8:5:-1]

# print(l1)
# print(l2)
# print(l3)

# Exercise 4: Count the occurrence of each element from a list

# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# count_dic = dict()

# for i in sample_list:
#     if i in count_dic:
#         count_dic[i]+=1
#     else:
#         count_dic[i]=1
# print(count_dic)

# Exercise 5: Create a Python set such that it shows the element from both lists in a pair

# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

# pyzip = zip(first_list, second_list)
# print(set(pyzip))


# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

# intersec = first_set.intersection(second_set)
# print(intersec)

# for i in intersec:
#     first_set.remove(i)
# print(first_set)

#Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set

# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}

# print(first_set.issubset(second_set))
# print(second_set.issubset(first_set))

# print(first_set.issuperset(second_set))
# print(second_set.issuperset(first_set))

# if first_set.issubset(second_set):
#     first_set.clear()
    

# if second_set.issubset(first_set):
#     second_set.clear()
    
# print("first", first_set)
# print("seconds", second_set)

# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# roll_number = [num for num in roll_number if num in sample_dict.values()]
# print(roll_number)

# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates

# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# list1 = speed.values()
# speed_list =  list()

# for i in list1:
#     if i not in speed_list:
#         speed_list.append(i)
# print(speed_list)

# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
tup = []

for i in sample_list:
    if i not in tup:
        tup.append(i)
print(tup)

print(max(tup))
print(min(tup))

samp = list(set(sample_list))
print(samp)


