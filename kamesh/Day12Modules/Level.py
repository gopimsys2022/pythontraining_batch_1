#Writ a function which generates a six digit/character random_user_id.

import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

print(random_user_id())

# #Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return str(r) + " " + str(g)+ " " + str(b)

print(rgb_color_gen())

#Level 2 

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random

def list_of_rgb_colors(n):
    
    colors = []
    
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append((r, g, b))
    
    return colors
print(list_of_rgb_colors(5))

#Level 3
#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(lst):
    random.shuffle(lst)  
    return lst
  
my_list = [1, 2, 3, 4, 5] 

shuffled_list = shuffle_list(my_list)

print(shuffled_list)

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

import random

def my_unique_numbers():

    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:7]

unique_numbers = my_unique_numbers()
print(unique_numbers)

output 

s4vohm
167 175 177
[(164, 166, 81), (59, 83, 89), (200, 246, 213), (100, 240, 105), (90, 63, 252)]
[5, 1, 3, 4, 2]
[3, 1, 0, 2, 7, 8, 4]