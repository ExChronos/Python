import pickle

dbfile = open('pickle-people', 'rb')
db = pickle.load(dbfile)

for key in db:
    print(key, '=>\n', db[key])

dbfile.close()