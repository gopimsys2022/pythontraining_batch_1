'''
    Create an empty dictionary called dog
    Add name, color, breed, legs, age to the dog dictionary
    Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
    country, city and address as keys for the dictionary
    Get the length of the student dictionary
    Get the value of skills and check the data type, it should be a list
    Modify the skills values by adding one or two skills
    Get the dictionary keys as a list
    Get the dictionary values as a list
    Change the dictionary to a list of tuples using items() method
    Delete one of the items in the dictionary
    Delete one of the dictionaries
'''
dog ={}
dog['name'] = 'beauty'
dog['greed'] = 'pomerian'
dog['colour'] = 'white'
dog['legs'] = 'four'
dog['age'] = 'five'
print(f"The newly created dictionary is {dog}\n")
student = {}
student['first_name'] = 'Sulthan'
student['last_name'] = 'Nashiha'
student['age'] = '39'
student['marital status'] = 'Married'
student['skills'] = ['storage', 'QA', 'Python', 'Bugzilla']
student['country'] = 'India'
student['city'] = 'Chennai'
student['address'] = ['1A', 'First main road', 'Vignarajapuram', 'santhospuram']
print(f"The newly created dictionary is {student}\n")
for key, value in student.items():
    print(f"{key} key==> value {value} \n")
    if type(value) is list:
        student['skills'].extend(['HPE', 'HCL', 'Solar'])
        print(f"{value} is a list \n")
res = dict(sorted(student.items(), key=lambda x: x[0]))
res1 = {key: (lambda x: x*2)(value) for key, value in student.items()}
print(res1)
print(f"The sorted elements using lambda function is {res}\n")
print(student['skills'][4])
print(student.get('skills'))
print(student.pop(['skills'][0]))
print(student)
print(student.popitem())
print(student)
print(student.items())
print(f"{student.values()} is the list of values \n")
print(f"{student.keys()} is the keys of list \n" )
student.__delitem__('last_name')
print(student)
print(dog)
print(dog.popitem())
print(dog)
print(dog.clear())
print(dog)
