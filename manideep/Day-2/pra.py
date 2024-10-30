fruits = ('apple', 'banana', 'orange', 'grape', 'kiwi')
vegetables = ('carrot', 'broccoli', 'spinach', 'pepper', 'potato')
animal_products = ('chicken', 'beef', 'milk', 'cheese', 'egg')

# Join the three tuples into one tuple
food_stuff_tp = fruits + vegetables + animal_products

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

print (food_stuff_lt)

# Slice out the first three items and the last three items
ft = food_stuff_lt[:3]
print (ft)

lt = food_stuff_lt[-3:]
print (lt)
