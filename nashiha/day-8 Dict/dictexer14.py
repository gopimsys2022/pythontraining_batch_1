'''To add the values of the common keys'''
import sys
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
for key, value in d1.items():
    for key1, value1 in d2.items():
        if key in key1:
            value += value1
        d1[key] = value
print(d1)
print(sys.version)
print(sys.platform)
#To print all unique values in a dictionary

list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
dict2 = {}
for item in list1:
    for keys, values in item.items():
        if values not in dict2:
            print(values)
            dict2[keys] = values
            print(dict2)
