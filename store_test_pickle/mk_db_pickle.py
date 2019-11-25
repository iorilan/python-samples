from initdata import db
import pickle
from pickle_common import filename

dbfile = open(filename, 'wb')
pickle.dump(db, dbfile)
dbfile.close()