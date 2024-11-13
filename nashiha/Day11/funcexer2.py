def to_insertele(x, y):
    x.sort(key= lambda x: x)
    x.insert(-1, y)
    return (x)
def swap_oftwonos(x, num1, num2, temp=0):
    temp = x[num1]
    x[num1] =x[num2]
    x[num2] =temp
    return x

list1 = ['z', 'a', 'b', 'c', 'd']
ele = 'y'
print(to_insertele(list1, ele))
print(swap_oftwonos(list1, 3, 5))




