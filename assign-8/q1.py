import os

path = "./notes.txt"
fd = os.open(path, os.O_RDONLY)

string= os.read(fd,50)
print(string)