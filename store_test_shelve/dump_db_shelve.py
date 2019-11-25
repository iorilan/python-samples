import shelve
db = shelve.open('people-shelve')
for k in db:
    print(k, '=>\n', db[k])
db.close()
