''' Join A and B
    Find A intersection B
    Is A subset of B
    Are A and B disjoint sets
    Join A with B and B with A
    What is the symmetric difference between A and B
    Delete the sets completely
'''
Whole_numbers = {0, 1, 2, 4, 5, 6, 8, 9}
even_numbers = {0, 1, 2, 4, 5, 6, 8, 9}
odd_numbers = {1, 3, 5, 7, 9}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
intersec = even_numbers.intersection(odd_numbers)
print(intersec)
print(even_numbers.issubset(odd_numbers))
print(A.issubset(B))
print(A.issuperset(B))
print(even_numbers.issuperset(odd_numbers))
print(odd_numbers.issuperset(even_numbers))
print(Whole_numbers.issuperset(even_numbers))
print(even_numbers.issuperset(Whole_numbers))
print(even_numbers.isdisjoint(odd_numbers))
print(A.isdisjoint(B))
print(even_numbers.issuperset(Whole_numbers))
print(Whole_numbers.issubset(even_numbers))
print(Whole_numbers.symmetric_difference(odd_numbers))
Whole_numbers.symmetric_difference_update(odd_numbers)
even_numbers.clear()
print(Whole_numbers.pop())
print(Whole_numbers)