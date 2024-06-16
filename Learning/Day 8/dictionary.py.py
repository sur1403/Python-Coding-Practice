# Exercise 1: Convert two lists into a dictionary

# result_dict = {}
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# result_dict = dict(zip(keys, values))
# print(result_dict)

# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# result = {}

# result = {**dict1, **dict2}
# print(result)

# Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict['class']['student']['marks']['history'])

# Exercise 4: Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# res = dict.fromkeys(employees, defaults)
# print(res)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# new_dict = {}

# for k in keys:
#     if k in sample_dict:
#         new_dict[k] = sample_dict[k]
# print(new_dict)

#Exercise 6: Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

# for k in keys:
#     if k in sample_dict:
#         sample_dict.pop(k)
# print(sample_dict)
# # 
# Exercise 7: Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# if 200 in sample_dict.values():
#     print("Yes")

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# sample_dict['location'] = sample_dict.pop['city'] 

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# print(min(sample_dict.values()))

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500

print(sample_dict)