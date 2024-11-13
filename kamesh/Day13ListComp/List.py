#Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero) 

#Flatten the following list of lists of lists to a one dimensional list

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimensional = [i for i in list_of_lists for sublist in i for i in sublist]
print(one_dimensional)

#Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [[country[0:].upper(), country[:3].upper(), city.upper()] for i in countries for country, city in i]
print(new_list)

#Change the following list to a list of dictionaries

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dictionary = [{"country": country.upper(),"city":city.upper()} for country, city in[i[0] for i in countries]]
print(dictionary)

#Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = [" ".join (name) for name in [item[0] for item in names]]
print(result)


output 

[-4, -3, -2, -1, 0]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
[{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]
['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']