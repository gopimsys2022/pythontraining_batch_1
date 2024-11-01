#Empty Dict
dict = {}
print(dict)

#Add keys and values
dog = {
    "name" : "puppy",
    "color" : "white",
    "breed" : "lab",
    "legs"  : 4,
    "age"  : 5

}
print(dog)

#Student Dict
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(student)

#Length
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(len(student))

#Get the values
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(student["skills"])

#Modify skills
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
}
student["skills"].extend(["java","React"])
print(student)

#Get Keys
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(student.keys())

#Get Values
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(student.values())

#Change dict 
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
}

student_tuples = list(student.items())
print(student_tuples)

#Delete one item
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
}

del student["age"]
print(student)

#Delete one of dict
student ={
    "first_name" : "Kiran",
    "last_name" : "kumar",
    "gender" : "Male",
    "age" : 26,
    "Marital status" : "single",
    "skills" : ["Python","Storage","Linux"],
    "country" : "India",
    "city" : "Chennai",
    "address" : {
        'street':'Space street',
        'zipcode':'02210'
    }
} 

print(student)

del student["address"]
print(student) 

output 

{}
{'name': 'puppy', 'color': 'white', 'breed': 'lab', 'legs': 4, 'age': 5}
{'first_name': 'Kiran', 'last_name': 'kumar', 'gender': 'Male', 'age': 26, 'Marital status': 'single', 'skills': ['Python', 'Storage', 'Linux'], 'country': 'India', 'city': 'Chennai', 'address': {'street': 'Space street', 'zipcode': '02210'}}    
9
['Python', 'Storage', 'Linux']
{'first_name': 'Kiran', 'last_name': 'kumar', 'gender': 'Male', 'age': 26, 'Marital status': 'single', 'skills': ['Python', 'Storage', 'Linux', 'java', 'React'], 'country': 'India', 'city': 'Chennai', 'address': {'street': 'Space street', 'zipcode': '02210'}}
dict_keys(['first_name', 'last_name', 'gender', 'age', 'Marital status', 'skills', 'country', 'city', 'address'])
dict_values(['Kiran', 'kumar', 'Male', 26, 'single', ['Python', 'Storage', 'Linux'], 'India', 'Chennai', {'street': 'Space 
street', 'zipcode': '02210'}])
[('first_name', 'Kiran'), ('last_name', 'kumar'), ('gender', 'Male'), ('age', 26), ('Marital status', 'single'), ('skills', ['Python', 'Storage', 'Linux']), ('country', 'India'), ('city', 'Chennai'), ('address', {'street': 'Space street', 'zipcode': '02210'})]
{'first_name': 'Kiran', 'last_name': 'kumar', 'gender': 'Male', 'Marital status': 'single', 'skills': ['Python', 'Storage', 'Linux'], 'country': 'India', 'city': 'Chennai', 'address': {'street': 'Space street', 'zipcode': '02210'}}
{'first_name': 'Kiran', 'last_name': 'kumar', 'gender': 'Male', 'age': 26, 'Marital status': 'single', 'skills': ['Python', 'Storage', 'Linux'], 'country': 'India', 'city': 'Chennai', 'address': {'street': 'Space street', 'zipcode': '02210'}}    
{'first_name': 'Kiran', 'last_name': 'kumar', 'gender': 'Male', 'age': 26, 'Marital status': 'single', 'skills': ['Python', 'Storage', 'Linux'], 'country': 'India', 'city': 'Chennai'}