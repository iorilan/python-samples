import pickle
from pickle_common import filename
dbfile = open(filename,'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.2
db['tom']['name'] = 'tt'
print('updated', db['sue']['pay'],db['tom']['name'])

dbfile = open(filename,'wb')
pickle.dump(db, dbfile)
dbfile.close()
