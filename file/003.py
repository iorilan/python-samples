import os
#os.rename(r'data.txt',r'data1.txt')
#os.remove(r'spam.txt')
print(os.stat(r'data1.txt'))

path = r'data1.txt'
print(os.path.isdir(path), os.path.isfile(path), os.path.getsize(path))