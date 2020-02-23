
import sys

def reader(F):
    tmp, sys.stdin = sys.stdin, F
    line = input()
    print(line)
    sys.stdin = tmp

reader( open('test-stream-modes.py') )         # works: input() returns text
reader( open('test-stream-modes.py', 'rb') )   # works: but input() returns bytes

def writer(F):
    tmp, sys.stdout = sys.stdout, F
    print(99, 'spam')
    sys.stdout = tmp

writer( open('temp', 'w') )             # works: print() passes text str to .write()
print(open('temp').read())

writer( open('temp', 'wb') )            # FAILS on print: binary mode requires bytes
writer( open('temp', 'w', 0) )          # FAILS on open: text must be unbuffered
