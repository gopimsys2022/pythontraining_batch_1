dict1 = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}
res = (dict(sorted(dict1.items(), key= lambda x: x[0])))
res1 = (dict(sorted(dict1.items(), key= lambda x: x[0])))
print(res)

maxi = max(dict1.values())
print(f"{maxi} is the maximum amongst the dictionary values \n")
mini = min(dict1.values())
print(f"{mini} is the minimum of the dictionary values \n")