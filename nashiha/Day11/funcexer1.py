def most_frequent(x):
    z = [x.count(i) for i in x]
    print(z)
    z.sort(key= lambda y:y)
    print(f"The frequently occured element is {x[0]} \n")
    print(z)


list1 = [2, 1, 2, 2, 1, 3]
most_frequent(list1)
