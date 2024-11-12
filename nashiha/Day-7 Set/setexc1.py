'''A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

Exercises: Level 1

    Find the length of the set it_companies
    Add 'Twitter' to it_companies
    Insert multiple IT companies at once to the set it_companies
    Remove one of the companies from the set it_companies
    What is the difference between remove and discard
'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(type(it_companies))
it_companies.add('twitter')
print(it_companies)
it_companies.update(['Msys', 'Solarwinds', 'HCL'])
it_companies.remove('HCL')
print(it_companies)
it_companies1 = it_companies.copy()
print(it_companies1)
it_companies1.discard('Silversoft')
it_companies1.remove('Facebook')
print(it_companies1)
print(it_companies)
it_companies.union(it_companies1)
it_companies1.clear()
print(it_companies1)
it_companies.pop()
print(it_companies)


