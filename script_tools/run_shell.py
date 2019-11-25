import os
#os.system("python3 001.py  001.py")

for line in os.popen('ls |grep .py'):print(line, end='')
