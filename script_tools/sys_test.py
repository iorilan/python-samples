import sys
print(sys)
print(sys.platform)
print(sys.maxsize)
print(sys.version)
print(sys.path)
print(sys.modules)

try:
    raise IndexError
except:
    print(sys.exc_info())

try:
    raise TypeError('already got one')
except:
    exc_info = sys.exc_info()
    for i in exc_info:
        print(i)


