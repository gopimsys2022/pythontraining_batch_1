'''Find unique numbers in list
output
{"unique": {"4": 1}, "duplicate": {"1": 2, "2": 2, "3": 2}'''

list1 = [1,2,3,4,1,2,3, 5, 3, 2]
dict1 = {}
dict2 = {}
uniquedict = {}
duplicatedict = {}
for item in list1:
    count = list1.count(item)
    if count >1:
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
    elif count ==1:
        if item in dict2:
            dict2[item] += 1
        else:
            dict2[item] = 1
print(dict1)
print(dict2)
uniquedict["unique"] = dict2
duplicatedict["duplicate"] =dict1
res = uniquedict. update(duplicatedict)
print(uniquedict)


