from people_base import bob, sue
import shelve

db = shelve.open('shelve-people')
db['sue'] = sue
db['bob'] = bob
db.close()