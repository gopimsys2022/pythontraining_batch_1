''' To remove duplicates from the dictionary'''
student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}
dict1 = {}
for key, value in student_data.items():
    if value not in dict1.values():
        dict1[key] = value
print(dict1)

#To check whether a dictionary is empty or not
dict2 = {}
if (student_data):
    print ("pass")
if not (dict2):
    print("Fail")
if not (dict2):
    print(f" dictionary is empty\n")