import pickle
from pickle_common import filename
dbfile = open(filename,'rb')
db = pickle.load(dbfile)

for k in db:
    print(k, '=>\n', db[k])
#print(db['sue']['name'])