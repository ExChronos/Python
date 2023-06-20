import pickle

dbfile = open('pickle-people', 'rb')
db = pickle.load(dbfile)
dbfile.close()

for key in db:
    db[key]['salary'] *= 1.10

dbfile = open('pickle-people', 'wb')
pickle.dump(db, dbfile)
dbfile.close()