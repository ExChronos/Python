import shelve

db = shelve.open('shelve-class')

for key in db:
    print(key, '=>\n', db[key])

db.close()