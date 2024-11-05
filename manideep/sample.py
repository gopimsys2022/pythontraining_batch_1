
grid of # symbols (8 rows and 8 columns):
# for i in range(8):
#     print('# ' * 8)

# 7. Print a multiplication table from 0 to 10:
# for i in range(11):
#     print(f"{i} x {i} = {i * i}")
# 8. Iterate through the list ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] and print each item:

# 9. Print only even numbers from 0 to 100 using a for loop:
# python
# Copy code
# for i in range(0, 101, 2):
#     print(i)
# 10. Print only odd numbers from 0 to 100 using a for loop:

# for i in range(1, 101, 2):
#     print(i)

# Exercises: Level 2
# 13. Use the countries.py file to loop through countries and extract those containing "land":
# Assuming countries.py has a list of countries like countries = ['Finland', 'Ireland', 'Germany', 'Poland', 'Estonia'], you can use:

# python
# Copy code
# countries = ['Finland', 'Ireland', 'Germany', 'Poland', 'Estonia']
# for country in countries:
#     if 'land' in country:
#         print(country)
# 14. Reverse the fruit list ['banana', 'orange', 'mango', 'lemon'] using a loop:
# python
# Copy code
# fruits = ['banana', 'orange', 'mango', 'lemon']
# for i in range(len(fruits)-1, -1, -1):
#     print(fruits[i])
# 15. Total number of languages from countries_data.py:
# Assuming countries_data.py contains a list of languages for each country, the code could look something like this:

# python
# Copy code
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

# python
# Copy code
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

# python
# Copy code
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

