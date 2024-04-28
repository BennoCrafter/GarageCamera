import os

stream = os.popen('git push')
output = stream.read()
print("lol")
print(output)
print("s")