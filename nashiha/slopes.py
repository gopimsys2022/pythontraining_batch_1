'''Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value
y is going to be 0.'''
def slope_intercepts (x, y):
    slope = 2*x -2
    y= x^2 + 6*x + 9
    print(f"The slope value of x-intercept and y-intercept is {slope} \n")
    return slope, y
def euclidean_slope(x1, x2, y1, y2):
    m= y2-y1 /x2-x1
    print(f"The Euclidean distance between the slopes are: {m}")
    return m

x_intercept = int(input("Enter the 'x-intercept' "))
y_intercept = int(input("Enter the 'y-intercept' "))
a1,a2,b1,b2 = 3,3,6,10
print(slope_intercepts(x_intercept, y_intercept))
print(euclidean_slope(a1, a2, b1, b2))
