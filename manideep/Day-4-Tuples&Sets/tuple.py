##### Tuple ######

# Create an empty tuple
tuple_e = () 

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
sisters = ("Divi", "Gayu")
brothers = ("Mani", "Deep")
siblings = sisters + brothers
print (siblings)

# How many siblings do you have?
tup_length= len(siblings)
print (tup_length)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
print (family_members)
family_members.append("siva")
family_members.append("Lakshmi")
print (family_members)
t = tuple (family_members)
print (t)

# Exercises: Level 2
# Unpack siblings and parents from family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("custardapple", "mango", "grapes")
vegetables = ("carrot", "brinjal", "cucumber")
animal_products = ("milk", "butter", "ghee")
food_stuff_tp = fruits + vegetables + animal_products
print (food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print (food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
ft = food_stuff_lt[:3]
print (ft)

lt = food_stuff_lt[-3:]
print (lt)

# Delete the food_staff_tp tuple completely
del food_stuff_tp
# print (food_stuff_tp)

# Check if an item exists in tuple:
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden", "Estonia")
country_to_check = 'Iceland'  
exists = ("Finland" in nordic_countries)
print(exists)

# Check if 'Estonia' is a Nordic country
estonia_nordic = 'Estonia' in nordic_countries
print(estonia_nordic)


# Check if 'Iceland' is a nordic country
iceland_nordic = 'Iceland' in nordic_countries
print(iceland_nordic)

Output : 
('Divi', 'Gayu', 'Mani', 'Deep')
4
['Divi', 'Gayu', 'Mani', 'Deep']
['Divi', 'Gayu', 'Mani', 'Deep', 'siva', 'Lakshmi']
('Divi', 'Gayu', 'Mani', 'Deep', 'siva', 'Lakshmi')
('custardapple', 'mango', 'grapes', 'carrot', 'brinjal', 'cucumber', 'milk', 'butter', 'ghee')
['custardapple', 'mango', 'grapes', 'carrot', 'brinjal', 'cucumber', 'milk', 'butter', 'ghee']
[]'apple', 'banana', 'orange']
['milk', 'cheese', 'egg']
True
True
True
