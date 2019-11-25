import os
pipe = os.popen('python e4.py')
pipe.read()
stat = pipe.close()
print('exit code :==>' , stat)