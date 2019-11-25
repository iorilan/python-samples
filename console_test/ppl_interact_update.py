import shelve
from person import Person

fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')
while True:
    k = input('\nkey? => ')
    if not k: break
    if k in db:
        record = db[k]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' %(field, currval))
        if newtext:
           # v = eval(newtext)
           # print('!!! => ', v, field)
            setattr(record, field, newtext)
    db[k] = record

db.close()
