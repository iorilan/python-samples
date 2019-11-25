import sys, os

def dfslister(curdir):
    print('['+curdir+']')
    for file in os.listdir(curdir):
        path = os.path.join(curdir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            dfslister(path)

if __name__ == '__main__':
    dfslister(sys.argv[1])