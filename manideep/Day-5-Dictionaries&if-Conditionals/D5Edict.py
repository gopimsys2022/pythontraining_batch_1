# Create an empty dictionary called dog
dog = {}
print (type(dog))

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'snoppy'
dog['colour'] = 'white'
dog['breed'] = 'Germanshepard'
dog['legs'] = '4'
dog['age'] = '2years'
print (dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_details = {"first_name" : "manideep", "last_name" : "maddali", "gender" : "male", "age": "31", "marital_status" : "married", "skills" : ['storage', 'Testing', 'Python'], "country" : "India", "city" : "Guntur"}
print (student_details)

# Get the length of the student dictionary
print (len(student_details))

# Get the value of skills and check the data type, it should be a list
student_skill = student_details["skills"]
print (student_skill)
print(type(student_skill))

# Modify the skills values by adding one or two skills
student_details["skills"].extend(["VMware","RAID"])
print (student_details["skills"])

# Get the dictionary keys as a list
keys = student_details.keys()
print (keys)

# Get the dictionary values as a list
values =student_details.values()
print (values)

# Change the dictionary to a list of tuples using items() method
# Delete one of the items in the dictionary
del student_details["marital_status"]
print(student_details)


# Delete one of the dictionaries
dict = {"name" : "mani", "place" : "chennai"}
del dict
print (dict)


### Output  :
# <class 'dict'>
# {'name': 'snoppy', 'colour': 'white', 'breed': 'Germanshepard', 'legs': '4', 'age': '2years'}
# {'first_name': 'manideep', 'last_name': 'maddali', 'gender': 'male', 'age': '31', 'marital_status': 'married', 'skills': ['storage', 'Testing', 'Python'], 'country': 'India', 'city': 'Guntur'}
# 8
# ['storage', 'Testing', 'Python']
# <class 'list'>
# ['storage', 'Testing', 'Python', 'VMware', 'RAID']
# dict_keys(['first_name', 'last_name', 'gender', 'age', 'marital_status', 'skills', 'country', 'city'])
# dict_values(['manideep', 'maddali', 'male', '31', 'married', ['storage', 'Testing', 'Python', 'VMware', 'RAID'], 'India', 'Guntur'])
# {'first_name': 'manideep', 'last_name': 'maddali', 'gender': 'male', 'age': '31', 'skills': ['storage', 'Testing', 'Python', 'VMware', 'RAID'], 'country': 'India', 'city': 'Guntur'}
# <class 'dict'>