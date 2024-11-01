      ##### Sets #####
#     Level -1

# # Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
lc = len(it_companies)
print (lc)

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print (it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update (['Dell', 'HPE', 'Lenovo'])
print (it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Amazon')
print (it_companies)

# What is the difference between remove and discard
it_companies.discard('Hitachi')
print (it_companies)
# if the mentioned keyword is not present in remove method will throw "Keyerror" whereas discard method won't throw error

# Output : Level-1
# 7
# {'Facebook', 'Twitter', 'Amazon', 'Apple', 'Google', 'IBM', 'Microsoft', 'Oracle'}
# {'HPE', 'Google', 'Microsoft', 'Lenovo', 'Amazon', 'Apple', 'Facebook', 'Twitter', 'Oracle', 'IBM', 'Dell'}
# {'HPE', 'Google', 'Microsoft', 'Lenovo', 'Apple', 'Facebook', 'Twitter', 'Oracle', 'IBM', 'Dell'}
# {'HPE', 'Google', 'Microsoft', 'Lenovo', 'Apple', 'Facebook', 'Twitter', 'Oracle', 'IBM', 'Dell'}

#     Level-2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Join A and B
C = A.union(B)
print (C) # returns the new set by givin all values

# Find A intersection B
D = A.intersection(B)
print (D)   # returns only common values

# Is A subset of B
E = B.issubset(A)
print (E)  

# Are A and B disjoint sets
F = B.isdisjoint(A)
print (F)  # returns true or false if both sets are not with common values

# Join A with B and B with A
# What is the symmetric difference between A and B
G = B.symmetric_difference(A)
print (G)     # returns the differnce values from the sets

# Delete the sets completely
set = {'mani', 'deep', 'siva', 'maddali'}
del set
print (set)

# Output: L-2
# {19, 20, 22, 24, 25, 26, 27, 28}
# {19, 20, 22, 24, 25, 26}
# False
# False
# {27, 28}
# <class 'set'>

####  Level-3 ####
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.