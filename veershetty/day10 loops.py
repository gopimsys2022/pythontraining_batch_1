import math

def prefer_square(numbers):
    return [math.sqrt(numbers) for num in numbers]
    numbers=[25,64,16,4]
    squared_numbers=prefer_square(numbers)
    
    print(squared_numbers)