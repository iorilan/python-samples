import shelve

def dumpPerson():
    db = shelve.open('class-shelve')
    for k in db:
        print(k, '=>\n', db[k])

dumpPerson()