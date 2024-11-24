'''Use loop to update the value of type2=50
{"friuts": {"appe": 1, "mango":2, "watermelon":[{"type1":10}, {"type2": 50}], "grape":4, "orange":5}}'''

dict1 = {"friuts": {"apple": 1, "mango":2, "banana":[{"type1":10}, {"type2": 20}], "grape":4, "orange":5}}
for key, value in dict1.items():
    for key1, value1 in value.items():
        if type(value1) == list:
            for item in value1:
                for keylis, valuelis in item.items():
                   if keylis == "type2":
                       item["type2"] = 50
                       print(item)
print(dict1)

