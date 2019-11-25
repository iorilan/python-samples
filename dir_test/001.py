import os
lines = [line[:-1] for line in os.popen('ls')]
print(lines)
print(os.listdir('.'))
print(os.curdir)
print(os.listdir('parts'))

import glob
print(glob.glob("*.txt"))
print(glob.glob(r'parts/*'))
