# 7. Print a multiplication table from 0 to 10:
# for i in range(11):
#     print(f"{i} x {i} = {i * i}")

# Exercises: Level 2

# 15. Total number of languages from countries_data.py:
# Assuming countries_data.py contains a list of languages for each country, the code could look something like this:

# # Example data format: countries_data = [{'country': 'USA', 'languages': ['English', 'Spanish']}, ...]
# countries_data = [
#     {'country': 'USA', 'languages': ['English', 'Spanish']},
#     {'country': 'India', 'languages': ['Hindi', 'English']},
#     # Add more countries with languages
# ]

# total_languages = set()
# for country in countries_data:
#     total_languages.update(country['languages'])

# print(f"Total number of languages: {len(total_languages)}")
# 16. Find the ten most spoken languages from the data:
# This would depend on how the data is structured, but here's a generic approach:

# # Example: countries_data = [{'country': 'USA', 'languages': ['English', 'Spanish']}, ...]
# languages_count = {}
# for country in countries_data:
#     for language in country['languages']:
#         languages_count[language] = languages_count.get(language, 0) + 1

# # Sort languages by frequency and pick the top 10
# sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)
# top_10_languages = sorted_languages[:10]

# print("Top 10 most spoken languages:")
# for language, count in top_10_languages:
#     print(f"{language}: {count} countries")
# 17. Find the 10 most populated countries:
# Assuming you have population data in countries_data.py like:

# # Example format: countries_data = [{'country': 'USA', 'population': 331000000}, ...]
# countries_data = [
#     {'country': 'USA', 'population': 331000000},
#     {'country': 'India', 'population': 1380004385},
#     # Add more countries with population data
# ]

# # Sort countries by population and pick the top 10
# sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
# top_10_countries = sorted_countries[:10]

# print("Top 10 most populated countries:")
# for country in top_10_countries:
#     print(f"{country['country']}: {country['population']}")

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# def evens_and_odds(n):
#     even_count = 0
#     odd_count = 0
#     for i in range(1, 100):
# #for digit in str(n):  # Convert the number to a string to loop through its digits
#         if n % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return f"The number of evens are {even_count}. The number of odds are {odd_count}."
# print(evens_and_odds(100))  

# def sum_of_even(n):
#     sum=0
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             sum += i
#     return sum
# print(sum_of_even(100))
# # Output: The number of evens are 2. The number of odds are 1.

# given_list = [1, 2, 3, 6, 8, 9]
# full_list = list(range(1, 10))
# missing_numbers = []
# for num in full_list:
#     if num not in given_list:
#         missing_numbers.append(num)
# print(missing_numbers)

weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
count = {}
for day in weekdays:
    if day in count:
        count[day] += 1
    else:
        count[day] = 1
list1 = []
dup = set()
print(list1)
for day in weekdays:
    if day not in dup:
        list1.append([day, count[day]])
        dup.add(day)
print(list1)
dictionary = {key: value for key, value in list1}
print(dictionary)

# s = "HelloWorld!"
# i = 0
# while i < len(s):
# print (s[i])
# i += 1

s="xhdmfjfmmdhm"
i=s.index("m")
s=s[:i+1]+s[i+1:].replace("m","$")
print(s)