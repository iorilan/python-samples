import shelve

def raiseAndSave(name, percent):
    db = shelve.open('class-shelve')
    person = db[name]
    person.giveRaise(percent)
    db[name] = person
    db.close()

raiseAndSave('sue jones', 0.5)
raiseAndSave('tom doe', 0.7)