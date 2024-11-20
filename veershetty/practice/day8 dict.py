dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) 

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) 
print(dct['key4'])

l = [1,2,3,4,1,2,3]
for num in l:
    if l.count(num) ==1:
        print(num)

        person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name'])
print(person['country'])    
print(person['skills'])     
print(person['skills'][0]) 
print(person['address']['street'])
print(person['city'])       

        