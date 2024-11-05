#Decalre a Empty list
list = []
print(list)

#More then 5 items
list = ["Apple","Mango","Kiwi","Banana","Orange","Sapota"]
print(list)

#length
list = ["Apple","Mango","Kiwi","Banana","Orange","Sapota"]
print(len(list))

#First, Middle, last item
list = ["Apple","Mango","Kiwi","Banana","Orange","Sapota"]
print(list[0])
middle = len(list) // 2
print(middle)
print(list[-1])

#Mixed Data Types
#name,age,height,status,address
mixed_data_types = ["Pavan", 28, 5.8, "Single", "3-34 kiran nagar"] 
print(mixed_data_types)

#List IT Comp
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

#Num of comp
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(len(it_companies))

#First,middle,Last
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[0])
middle = len(it_companies)//2
print(middle)
print(it_companies[-1])

#ADD 
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("TCS")
print(it_companies)

#Insert Middle
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(4, "Capgemini")
print(it_companies)

#One Upper Case
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
uppercase = it_companies[2].upper() 
print(uppercase)

#Join
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(" # ".join(it_companies))

#Check
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("Apple" in it_companies) 

#sort
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies.sort())

#Reverse
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies.reverse())

#slice first 3 comp
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[0:3])

#last 3 companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[4:7])

#Middle
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[3])

#Remove 1st company
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies.pop(0))

#Remove middle
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies.pop(3))

#last item
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies.pop(-1))

#All
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies.clear())

#Destroy
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies

#Join the list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

#copy the join the list
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5,"Python")
full_stack.insert(6,"SQl")
print(full_stack)

#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

#sort
ages.sort()
print(ages)

result = max(ages)
print(result)

result = min(ages)
print(result)

#Add min and max Age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
max_age = max(ages)
ages.append(max_age)
print(ages)

#Min age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = min(ages)
ages.append(min_age)
print(ages)

#Average
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

no_of_values = len(ages)
print(no_of_values)

total = sum(ages)
print(total)

avg = total / no_of_values  
print(avg)

#Range
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
range = max(ages) - min(ages)
print(range)

#Middle Countrys
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 
    'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 
    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 
    'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 
    'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 
    'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 
    'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 
    'Central African Republic', 'Chad', 'Chile', 'China', 
    'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo', 
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 
    'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 
    'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 
    'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 
    'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 
    'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 
    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 
    'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 
    'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 
    'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 
    'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 
    'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 
    'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 
    'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 
    'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 
    'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 
    'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 
    'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 
    'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 
    'Philippines', 'Poland', 'Portugal', 'Qatar', 
    'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 
    'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 
    'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 
    'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 
    'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 
    'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 
    'Sudan', 'Suriname', 'Swaziland', 'Sweden', 
    'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 
    'Tanzania', 'Thailand', 'Togo', 'Tonga', 
    'Trinidad and Tobago', 'Tunisia', 'Turkey', 
    'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 
    'United Arab Emirates', 'United Kingdom', 
    'United States', 'Uruguay', 'Uzbekistan', 
    'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 
    'Yemen', 'Zambia', 'Zimbabwe'
]

middle_country = countries[len(countries) // 2]
print(middle_country)

#Divide the countries
split = (len(countries)+1) //2 
first = countries[:split]
second = countries[split:]
print(first)
print(second)

#Unpack
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = countries
print(first_country)
print(second_country)
print(third_country)
print(scandic_countries)

output

[]
['Apple', 'Mango', 'Kiwi', 'Banana', 'Orange', 'Sapota']
6
Apple
3
Sapota
['Pavan', 28, 5.8, 'Single', '3-34 kiran nagar']
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
7
Facebook
3
Amazon
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'TCS']
['Facebook', 'Google', 'Microsoft', 'Apple', 'Capgemini', 'IBM', 'Oracle', 'Amazon']
MICROSOFT
Facebook # Google # Microsoft # Apple # IBM # Oracle # Amazon
True
None
None
['Facebook', 'Google', 'Microsoft']
['IBM', 'Oracle', 'Amazon']
Apple
Facebook
Apple
Amazon
None
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQl', 'Node', 'Express', 'MongoDB']
[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
26
19
[19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 26]
[19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19]
[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
10
228
22.8
7
Lesotho
['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 
'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho']
['Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United 
States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']        
China
Russia
USA
['Finland', 'Sweden', 'Norway', 'Denmark']