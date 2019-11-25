def scanner(name, processFunc):
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line: break
        processFunc(line)
    file.close()

