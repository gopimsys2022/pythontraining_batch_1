# 1 to 10
for i in range(11):
    print(i)

#usin while loop
count = 0 
while count<11:
    print(count)
    count = count + 1 

# 10 to 0 





# Level 2
#0 to 100
sum = 0
for num in range(101):
    sum += num 
print(sum)

#Sum of even and odd num
even_sum = 0
odd_sum = 0

for num in range(101):
    
    if (num %2==0):
        even_sum += num 
    else:
        odd_sum += num
        
print("sum of all evens is:",even_sum)
print("sum of all odds is:",odd_sum)

        