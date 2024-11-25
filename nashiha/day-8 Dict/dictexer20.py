'''to add 'ing' at the end of a given string . If the given string already ends with 'ing', add 'ly' instead.
 If the string length of the given string is less than 3, leave it unchanged. '''
word1 = input("Enter the word: ")
print(word1[-3:])
if len(word1) >3 and (word1[-3:] != 'ing'):
    res = word1[0:] + 'ing'
    print(res)
elif len(word1) >3 and (word1[-3:]) == 'ing':
    res = word1[0:] + 'ly'
    print(res)
else:
    res = word1
    print(res)

'''the first appearance of the substrings 'not' and 'poor' in a given string. If 'not'
 follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.'''

word3 = "The lyrics is not that poor!"
word4 = word3.replace("not", "good")
word4.replace("poor", "gooder")
print(word4)

#to find the longest word

list1= ["PHP", "Exercises", "Backend"]
res = [len(item) for item in list1]
print(res)
maxi = max(res)
print(res)
print(f"{maxi} is the maximum length of the word ")
res1 =  [item for item in list1 if len(item) == maxi]
print(f"{res1} is  the word with the maximum length {maxi} \n")

'''Python program to remove the nth index character from a nonempty string. '''
str5 = "The lyrics are very good"
length = len(str5)
index = int(input("Enter the index character to be removed: "))
str6 = str5[index: length-5] + str5[-index:]
print(str6)

'''given string to a newly string where the first and last chars have been exchanged'''
print(length)
x = str5[length-1]
print(x)
y = str5[0]
print(y)

print(str5[-1:])
print(str5[1:-1])
str6 = x +str5[1: -1] +y
print(str6)

