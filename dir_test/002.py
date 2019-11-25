import os

dirname = r'/home/lanliang/py-study/dir_test'

import glob
for file in glob.glob(dirname+'/*'):
    head, tail = os.path.split(file)
    print(head, tail)

for file in os.listdir(dirname):
    print(dirname, file, '=>', os.path.join(dirname, file))
    