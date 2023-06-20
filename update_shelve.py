from people_base import tom
import shelve

db = shelve.open('shelve-people')

sue = db['sue']
sue['salary'] *= 1.50
db['sue'] = sue
db['tom'] = tom

db.close()