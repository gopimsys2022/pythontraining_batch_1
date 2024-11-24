#Define a class
class dictObj():
#Define a constructor
    def __init__(self, x, y, z):
#Initialising thxe object attributes
        self.x = "red"
        self.y = "yellow"
        self.z = "blue"
    def no_function():
        pass
test = dictObj("red", "yeelow", "blue")
print(test.__dict__)
