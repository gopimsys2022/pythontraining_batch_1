#Level 1
#Get user Input
age = int(input("Enter your age: "))

if age > 18:
    print("You are old enough to learn to drive.")
else:
    print("You need 3 more years to learn to drive.")

#Comapre a and b
a = input("Enter num one: ")
b = input("Enter num two: ")

if a> b:
    print( a,"is greater then", b)
elif a<b:
    print(a,"is less then", "b")
else:
    print(a, "is equal to","b")


#Level 2

score = int(input("Enter student score: "))

if 80<=score<=100:
    print("grade A")
elif 70<=score<=89:
    print("grade B")
elif 60<=score<=69:
    print("grade C")
elif 50<=score<=59:
    print("grade D")
elif 0<=score<=49:
    print("grade F")
else:
    print("Invalid")


#check the season
month = input("Enter a month: ")

if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month. Please enter a valid month name.")

#List
fruits = ['banana', 'orange', 'mango', 'lemon']
user = input("Enter a fruit: ")

if user in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(user)
    print(fruits)

#Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']

    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

    if skills == ['JavaScript', 'React']:
        print("He is a front end developer.")
    elif skills == ['Node', 'Python', 'MongoDB']:
        print("He is a backend developer.")
    elif skills == ['React', 'Node', 'MongoDB']:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

    if person['is_married'] and person['country'] == 'Finland':
        print(person["first_name"] + " " + person["last_name"] + " is married and lives in Finland.")

output 

Enter your age: 27
You are old enough to learn to drive.
Enter num one: 7
Enter num two: 9
7 is less then b
Enter student score: 76
grade B
Enter a month: March
The season is Spring.
Enter a fruit: Apple
['banana', 'orange', 'mango', 'lemon', 'Apple']
Middle skill: Node
Unknown title.
Asabeneh Yetayeh is married and lives in Finland