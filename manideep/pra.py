# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,  # Fixed the key spelling
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# # Check if the person has the skills key
# if 'skills' in person:
#     skills = person['skills']
    
#     # Print out the middle skill
#     middle_index = len(skills) // 2
#     middle_skill = skills[middle_index]
#     print(f"The middle skill is: {middle_skill}")
# else:
#     print("Unknown title.")




# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# syntac
# re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
# 
# 1)
# Find the missing numbers in the list
# [1,2,3,6,8,9]
# nums = [1, 2, 3, 6, 8, 9]
# fullrange = list(range(1, 10))
# missingnumbers = list(set(fullrange) - set(nums))
# missingnumbers.sort()
# print("Missing numbers:", missingnumbers)

### (or)
# nums = [1, 2, 3, 6, 8, 9]
# missing_numbers = []
# for i in range(1 , 10):
#     if i not in nums:
#         missing_numbers.append(i)
# print(missing_numbers)

# 2)
# Update the value in the dict
# dict = {"a": 1, "b": [1,2], "c": "data"}
# dict.update({"b": {1,2,3,4}})
# print (dict)

# 3)
# Remove duplicates values, 20,30,40,20,10,40
# output:
# [10,20,30,40]
values = [20,30,40,20,10,40]
list=set(values)
print (list)

### (or)
# numbers = [20, 30, 40, 20, 10, 40]
# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:  # Check if the number is already in the list
#         unique_numbers.append(num)  # Add it if it's not already there
# print(unique_numbers)



# 4)
# input:
# x = [1,2,3]
# y = [3,2,6]
# output1-> [1,2,3,3,2,6]
# i) Get unique values
# z = x union y
# print (z)
# x = [1,2,3]
# y = [3,2,6]
# x.extend(y)
# print (x)
# z = set(x)
# print (z)

# unique_values = list(set(z))
# print(unique_values)

###
str1 = "xyzmamama"
res = ""
count = 0
for i in str1:
    if "m" == i:
        count+=1
        if count >= 2:
            res = res + "$"
        else:
            res = res + i
    else:
        res = res + i
print(res)
# output = xyzma$a$a

# str = "aabbbcddddeeeee"
# count = ""
# for i in str:
#     if str == i:
#         count+=1
#         if count >= 1:


# o/p : a2b3c1d3e5
# str2 = "aabbbcddddeeeee"
# freq = {}

# for i in str2:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)
# str3=str(freq)
# print(str3)

#####
str2 = "aabbbcddddeeeee"
result = ''
count = 1
for i in range(1, len(str2)):
    if str2[i] == str2[i-1]:
        count += 1
    else:
        result += str2[i-1] + str(count)
        count = 1  
result += str2[-1] + str(count)

print(result)
s = "aabbbcddddeeeee"  
result = "" 
count = 1  
for i in range(1, len(s)):
    
    if s[i] == s[i-1]:  
        
        count += 1  
    else:
        result = s[i-1] 
        count = 1

### kamesh
fruits = {"appe": 1, "mango":2, "banana":[{"type1":10}, {"type2": 20}], "grape":4, "orange":5}
print(fruits)

for fruit, items in fruits.items():
    if fruit == "banana":
        for item in items:
            if "type2" in item:
                item["type2"] = 50
print(fruits)


#####
fruits = {"appe": 1, "mango": 2, "banana": [{"type1": 10}, {"type2": 20}], "grape": 4, "orange": 5}
# fruits["watermelon"] = fruits.pop("banana")
for item in fruits["banana"]:
    if "type2" in item:
        item["type2"] = 50
print(fruits)

###
# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]

my_tuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
avg_value = []
for i in my_tuple:
    avg = sum(i) / len(i)
    avg_value.append(avg)
print (avg_value)

tuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

res = []

for i in range(len(tuple)): 
    total = 0
    count = 0
    
    for j in range(len(tuple[0])):
        total += tuple[j][i]
        count += 1
    
    res.append(total / count)

print(res)