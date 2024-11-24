# Create the second dictionary 'd2' with key-value pairs.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200, 'b': 400}
total = 0
mul= 1
dict3 = {**d1, **d2}
print(dict3)
res = sum(dict3.values())
for value1 in dict3.values():
    total += value1
    mul = mul *value1
    print(f"{total} is the sum of all values \n")
    print(f"{mul} is the sum of all values \n")
print(res)
dict4 = d1.update(d2)
print(d1)
for key, value in d1.items():
    d2[key] = value
print(d1)
