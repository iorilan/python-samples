import shelve
fieldnames = ('name','age','job','pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

for p in db:
    print(p, '=>\n', db[p])

while True:
    key = input ('\nkey? => ')
    if not key:break
    try:
        record = db[key]
    except:
        print('no such key "%s"!' %key)
    else:
        for f in fieldnames:
            print (f.ljust(maxfield), '=>', getattr(record, f))


    