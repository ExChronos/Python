import shelve

db = shelve.open('shelve-people')

for key in db:
    print(key, '=>\n', db[key])

db.close()