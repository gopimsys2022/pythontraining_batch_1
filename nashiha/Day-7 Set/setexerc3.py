'''
    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
    Explain the difference between the following data types: string, list, tuple and set
    I am a teacher and I love to inspire and teach people. How many unique words have been used
     in the sentence? Use the split methods and set to get the unique words.
'''

age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
lislen = len(age)
print(lislen)
setlen = len(ages)
print(setlen)
print(type(ages))
if lislen > setlen:
    print(lislen)
else:
    print(setlen)
word = "I am a teacher and I love to inspire and teach people"
print(type(word))
print(len(word))
word1 = list(word)
print(len(word1))
word2 = set(word1)
print(type(word2))
print(len(word2))
print(f"{word2} is a set of {word}\n")
word3 = tuple(word)
print(f"{word3} is a tuple of {word}\n")
for item in word:
    if item in word3:
        print(word.split(item))
#print(word.split("I"))
