import os 

stream = os.popen("python3 test.py")
output = stream.read()
print("Os:", output)