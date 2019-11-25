import os, sys
print ('my os.getced =>', os.getcwd())
print ('my sys.path =>',sys.path[:6])
print(os.environ.keys())

for k in os.environ.keys():
    print(k,'=>',os.environ[k])

sys.stdout.write('another print')