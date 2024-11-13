'''The following list contains some fruits:
If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
If the fruit exists print('That fruit already exist in the list')
'''

list1 = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter the input for fruits: ")
for item in range(len(list1)):
    if fruit in list1[item]:
        print(f"The given fruit exists in {list1} \n")
        break
    list1.append(fruit)
    print(f"The modified fruit list is : {list1} \n")
