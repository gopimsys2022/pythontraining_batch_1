#swapping first element to last and last to first
my_list = [1, 2, 3, 4, 5]
list1 = my_list.copy()
print(f"{list1} is the copy of {my_list} \n")
list1 = list1[::-1]
print(list1)
list2 = my_list[-1:] +my_list[1:-1]+my_list[:1]
print(list2)
word1= "hello world"
print(type(word1))
print(word1[::-1])
print(len(word1))
word2 = word1[-1:]+ word1[1:-1]+word1[::1]
print(word2)