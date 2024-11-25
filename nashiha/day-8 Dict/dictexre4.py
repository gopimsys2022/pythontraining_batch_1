'''remove duplicate values in dictionary
{'apple' : 10, 'mango' : 15, 'grape' : 20}'''
dict1 ={'apple' : 10, 'mango' : 15, 'grape' : 20, 'orange' : 10, 'banana' : 20}
dict2 = {}
for key, value in dict1.items():
    if value not in dict2.values():
        dict2[key] = value
    print(dict2)


list1 = [10,15,20,10,20]
list2 = set(list1)
print(list2)
res = [item for item in list2]
print(res)


