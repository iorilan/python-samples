import os
print(os.path.isdir(r'/home'),os.path.isfile(r'/etc'))
print(os.path.isdir(r'/home'), os.path.isfile(r'/etc'))
print(os.path.exists(r'/usr/bin'))
print(os.path.getsize(r'/usr/bin'))
print(os.path.split(r'/usr/bin'))
print(os.path.join(r'/usr/bin','etc'))
p = '/home/aaa/temp/data.txt'
print(os.path.dirname(p), os.path.basename(p)) #{path} and 'data.txt'
print(os.path.splitext(p)) #\{path} and .txt
q = '//home//aa//temp//data.txt'
print(os.path.normpath(q))

# current path
print(os.getcwd())

#current path\tmp
print(os.path.abspath('tmp'))

# parent path
print(os.path.abspath('../'))

