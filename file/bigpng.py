import os, glob, sys

if len(sys.argv) == 1 :
    dirname = r'D:\tmp' 
else :
    dirname = sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.png')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))
allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])