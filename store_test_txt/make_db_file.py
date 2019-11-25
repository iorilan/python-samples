db_file_name = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'

def storeDb(db, filename=db_file_name):
    "formatted dump of db to flat file"
    dbfile = open(filename, 'w')
    for k in db:
        print(k, file=dbfile)
        for (n, v) in db[k].items():
            print(n+RECSEP+repr(v), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

def loadDb(dbfilename=db_file_name):
    "parsing data to reconstruct db"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec={}
        field=input()
        while field != ENDREC:
            n,v = field.split(RECSEP)
            rec[n] = eval(v)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__': #run as script
    from initdata import db
    storeDb(db)
    print("done")
