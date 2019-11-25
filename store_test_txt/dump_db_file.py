from make_db_file import loadDb,storeDb
db = loadDb()

for k in db:
    print(k, '=>\n ',db[k])
print(db['sue']['name'])

