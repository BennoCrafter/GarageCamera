import os

stream = os.popen('pwd ; cd; pwd')
output = stream.read()
print(output)