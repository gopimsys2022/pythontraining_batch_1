#Length
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(it_companies)
print(len(it_companies))

#Add 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add("Twitter")
print(it_companies)

#Insert Multiple 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.update(["Twitter","TCS","Capgemini"])
print(it_companies)

#Remove
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#it_companies.remove("Msys") shows error company not their
it_companies.remove("Google")
print(it_companies)

#Diff bw remove and discard
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.discard("msys") #no error
it_companies.discard("Google") 
print(it_companies)
print(it_companies)

#Level 2
#Join
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

result = A.union(B)
print(result)

#Intersection
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

result = A.intersection(B)
print(result)

#SubSet
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

result = B.issubset(A)
print(result)

#Disjoint
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

result = B.isdisjoint(A)
print(result)

#Join both
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

result = A.union(B)
result1 = (B).union(A)

print(result)
print(result1)

#Symmetric 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

result = A.symmetric_difference(B)
print(result)

#Delete 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

del A
del B 

#Level 3
#convert list to set
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(age)
print(len(age))

age1 = set(age)  
print(age1)
print(len(age1))

if len(age) > len(age1):
    print("list age is bigger")
elif len(age) < len(age1):
    print("set age1 is bigger")
else:
    print("Both are the same")

#Unique
sentence = "I am a teacher and I love to inspire and teach people"
print(sentence) 
words = sentence.split()
unique_words = set(words)
num = len(unique_words)
print(unique_words)
print(num)

output

{'Google', 'Amazon', 'Facebook', 'IBM', 'Apple', 'Microsoft', 'Oracle'}
7
{'Google', 'Amazon', 'Facebook', 'IBM', 'Apple', 'Twitter', 'Microsoft', 'Oracle'}
{'TCS', 'Capgemini', 'Apple', 'Microsoft', 'IBM', 'Amazon', 'Facebook', 'Twitter', 'Google', 'Oracle'}
{'Amazon', 'Facebook', 'IBM', 'Apple', 'Microsoft', 'Oracle'}
{'Amazon', 'Facebook', 'IBM', 'Apple', 'Microsoft', 'Oracle'}
{'Amazon', 'Facebook', 'IBM', 'Apple', 'Microsoft', 'Oracle'}
{19, 20, 22, 24, 25, 26, 27, 28}
{19, 20, 22, 24, 25, 26}
False
False
{19, 20, 22, 24, 25, 26, 27, 28}
{19, 20, 22, 24, 25, 26, 27, 28}
{27, 28}
[22, 19, 24, 25, 26, 24, 25, 24]
8
{19, 22, 24, 25, 26}
5
list age is bigger
I am a teacher and I love to inspire and teach people
{'people', 'to', 'teach', 'a', 'teacher', 'love', 'and', 'am', 'inspire', 'I'}
10