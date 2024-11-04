person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,  # Fixed the key spelling
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person has the skills key
if 'skills' in person:
    skills = person['skills']
    
    # Print out the middle skill
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print(f"The middle skill is: {middle_skill}")
else:
    print("Unknown title.")