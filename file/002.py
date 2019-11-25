file = open('data.txt')
#open('data.txt','r')
#open('data.txt','r', encoding='utf8')

lines = file.readlines()
for l in lines:
    print(l, end='')

file.seek(0)
all = file.read()
print(all)
