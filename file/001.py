def appendEnter(lines):
    return list(l+'\n' for l in lines)

def processFile(f, data):
    try:
        f.write('hello file world!\n')
        f.writelines(appendEnter(data))
    finally:
        f.close()

file = open('data.txt', 'w')
processFile(file, ["111","222","333"])


#with context manager
with open('data.txt','w') as myFile:
    processFile(myFile, ["aaa","bbb","ccc"])


