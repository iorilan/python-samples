import os
matches = []
def lister(path, ext):
    for (dirname, dirshere, fileshere) in os.walk(path):
        for filename in fileshere:
            if filename.endswith(ext):
                pathname = os.path.join(dirname, filename)
               # if 'mimetypes' in open(pathname).read():
                matches.append(pathname)

lister(r'/home/lanliang', '.py')
for name in matches:print(name)



