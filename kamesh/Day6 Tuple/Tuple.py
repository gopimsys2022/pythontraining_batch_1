#Empty Tuple
t =()
print(t)

#Containing names
brothers = ("kiran","ajay","vikas")
sisters = ("sri","kumari")
siblings = brothers + sisters
print(siblings)

#length
siblings = ('kiran', 'ajay', 'vikas', 'sri', 'kumari')
print(len(siblings))

#Modify
siblings = ('kiran', 'ajay', 'vikas', 'sri', 'kumari')
print(siblings)  

siblings = list(siblings)

siblings.insert(0, "Vinay Varma")  
siblings.insert(1, "Devi")          

family_members = tuple(siblings)
print(family_members)


#Level 2
#Unpack
family_members = ('Vinay Varma', 'Devi', 'kiran', 'ajay', 'vikas', 'sri', 'kumari')
parents =("Vinay varma", "Devi")
print(parents)

siblings = ("kiran","ajay","vikas","sri","kumari")
print(siblings)

#Create a tuples
fruits = ("Orange","Mango","Apple")
vegetables = ("Potato","Onion","Cabbage")
Animals = ("Lion","Tiger","Elephant")
food_stuff_tp = fruits + vegetables + Animals
print(food_stuff_tp)

#Change to list 
food_stuff_tp = ('Orange', 'Mango', 'Apple', 'Potato', 'Onion', 'Cabbage', 'Lion', 'Tiger', 'Elephant')

food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

#Slice Middle Item
food_stuff_tp = ('Orange', 'Mango', 'Apple', 'Potato', 'Onion', 'Cabbage', 'Lion', 'Tiger', 'Elephant')
print(food_stuff_tp[4])

#First 3 and last 3
food_stuff_tp = ('Orange', 'Mango', 'Apple', 'Potato', 'Onion', 'Cabbage', 'Lion', 'Tiger', 'Elephant')
first = food_stuff_tp[:3]
last = food_stuff_tp[-3:]
print(first)
print(last)

#Delete
food_stuff_tp = ('Orange', 'Mango', 'Apple', 'Potato', 'Onion', 'Cabbage', 'Lion', 'Tiger', 'Elephant')
print(food_stuff_tp)
del food_stuff_tp

#Check
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


#Output
()
('kiran', 'ajay', 'vikas', 'sri', 'kumari')
5
('kiran', 'ajay', 'vikas', 'sri', 'kumari')
('Vinay Varma', 'Devi', 'kiran', 'ajay', 'vikas', 'sri', 'kumari')
('Vinay varma', 'Devi')
('kiran', 'ajay', 'vikas', 'sri', 'kumari')
('Orange', 'Mango', 'Apple', 'Potato', 'Onion', 'Cabbage', 'Lion', 'Tiger', 'Elephant')
['Orange', 'Mango', 'Apple', 'Potato', 'Onion', 'Cabbage', 'Lion', 'Tiger', 'Elephant']
Onion
('Orange', 'Mango', 'Apple')
('Lion', 'Tiger', 'Elephant')
('Orange', 'Mango', 'Apple', 'Potato', 'Onion', 'Cabbage', 'Lion', 'Tiger', 'Elephant')
False
True
