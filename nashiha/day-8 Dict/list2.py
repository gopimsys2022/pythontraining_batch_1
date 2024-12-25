import sys
print(sys.version)

list1 =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
try:
    res = sorted(list1, key= lambda  x:x[1], reverse= True)
    print(res)
except list1 == None:
    print(f"Empty list can not be sorted")