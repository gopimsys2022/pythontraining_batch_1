#a2b3c1d3e5

word1 = "aabbbcddddeeeee"
dict1 = {}
for item in word1:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] = 1
print(dict1)

#from two given strings, separated by a space and swap the first two characters of each string.
str1 = 'abc', 'xyz'
str2 = str1[1][0] + str1[0][1:]
print(str2)
str3 = str1[0][0] + str1[1][1:]
res = str2 + str3
print(res)

