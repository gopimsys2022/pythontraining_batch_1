#to find the frequency of the characters
str1 = "Google.com"
dict1 = {}
keys = dict1.keys()
for item in str1:
    if item in keys:
        dict1[item] += 1
    else:
        dict1[item] =1
print(dict1)

#string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead

str2 = "W3resource.com"
length = len(str2)
mid = length//2
print(mid)
res =str2[0: 3] + str2[-3:]
print(res)