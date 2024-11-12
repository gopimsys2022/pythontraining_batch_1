'''
    Check if an item exists in tuple:

    Check if 'Estonia' is a nordic country

    Check if 'Iceland' is a nordic country

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'''
fruits = ("banana", 'orange', 'lime', 'grapes')
new = [x for x in fruits if "lime" in x]
print(new)
vegetables = ('brinjal', 'potato', 'carrot', 'drumstick')
animals = ('dog', 'cat', 'cow', 'fox')
food_stuff = fruits+ vegetables+ animals
food_stuff =list(food_stuff)
new_stuff = food_stuff.copy()
print (f"{new_stuff} is copy of the food_stuff list\n")
print(food_stuff[0:3])
print(food_stuff[-3:])
food_stuff.append("hirerachy")
print(f"{food_stuff}\n")
print(f"{new_stuff}\n")
print(f"The {food_stuff} is the joined elements of all the tuples \n")
food_stuff[2:6] = ['pomegranite', 'bottle guard', 'Tiger', 'Lion']
print(f"The {food_stuff} is the joined elements of all the tuples \n")
print (f"{new_stuff} is copy of the food_stuff list\n")
family_mem = ('kader Hillson', 'Nashiha', 'Zainab', 'Hafza', 'Mafaz', 'Ayaan')
siblings = family_mem[2:]
print(f"The siblings are {siblings} \n")
parents = family_mem[0:2]
print(f"The siblings are {siblings} \n")
print(f"The parents are {parents} \n")
print(f"{food_stuff} is the tuple to be cleared \n")
food_stuff.clear()
print(f"{food_stuff} is the deleted tuple \n")
print (f"{new_stuff} is copy of the food_stuff list\n")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
res =[item if item == 'Estoncia' else 'Iceland' for item in nordic_countries]
print(res)
