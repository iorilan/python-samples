#open('file').read() # read entire file
#open('file').read(10) #read 10 bytes into string
#open('file').readlines()#read entire file into line string list
#open('file').readline()#read next line

file = open('spam.txt', 'w')
ret = file.write(('spam\n'*5))
print(ret)
file.close()

file = open('spam.txt')
#text = file.read()
#print(text)
lines = file.readlines()
lines2 = [l.strip() for l in lines]
print(lines2)
file.close()


