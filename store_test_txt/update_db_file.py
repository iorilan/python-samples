from make_db_file import loadDb,storeDb


db = loadDb()
db['sue']['pay'] = 1.10
db['tom']['name'] = 'tm tom'
storeDb(db)
