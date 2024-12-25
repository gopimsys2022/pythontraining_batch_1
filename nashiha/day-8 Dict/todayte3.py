import os
import sys
with open("example1.txt", "r") as fp1:
    content = fp1.read()
print(os.listdir())
print(content)