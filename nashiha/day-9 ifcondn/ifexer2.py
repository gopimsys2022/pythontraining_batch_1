'''Write a code which gives grade to students according to theirs scores:
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''
mark = int(input("Enter the mark obtained by the student: "))
if ((mark >= 80) and (mark<=100)):
    print(f"GRADE- A\n")
elif ((mark >= 70) and (mark <= 89)):
    print(f"GRADE- B\n")
elif ((mark >= 60) and (mark <= 69)):
    print(f"GRADE- C\n")
elif ((mark >= 50) and (mark < 59)):
    print(f"GRADE- D\n")
else:
    print(f"GRADE- F\n")
'''Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October
or November, the season is Autumn. December, January or February, the season is Winter. March, April 
or May, the season is Spring June, July or August, the season is Summer'''
climate = input('Enter the month you are in: \n')
list1 = ['September', 'October',  'November']
list2 = ['December', 'January', 'February']
list3 = ['March', 'April', 'May']
list4 = ['June', 'July', 'August']
for item in list1:
    if climate == item:
        print(f"You are having the AUTUMN season \n")
for item in list2:
    if climate == item:
        print(f"You are having the WINTER season \n")
for item in list3:
    if climate == item:
        print(f"You are having the SPRING season \n")
for item in list4:
    if climate == item:
        print(f"You are having the SUMMER season \n")