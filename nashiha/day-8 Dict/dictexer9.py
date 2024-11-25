'''input = xyzmamama
output = xyzma$a$a'''

word1 = "xyzmamama"
word1 = list(word1)
print(word1)
count = 0
for i in range(len(word1)):
    if word1[i] == "m":
        count += 1
        if count >1:
            word1[i] = "$"
            print(word1)
word2 = " ".join(word1)
print(word2)
'''for i in range(len(word1)):
    word1[i].join(',')
print(word1)'''



