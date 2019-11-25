import shelve
from person import Person
from manager import Manager

bob = Person('bob smith', 42, 30000, 'software')
sue = Person('sue jones', 45, 40000, 'hardware')
tom = Manager('tom doe', 50, 50000)

def savePerson(persons):
    db = shelve.open('class-shelve')
    for p in persons:
        db[p.name] = p
    db.close()

savePerson([bob,sue,tom])
