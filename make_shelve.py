import shelve
from mark import Person, Manager

bob = Person('Bob Smith', 42, 30000, 'Devops')
sue = Person('Sue Storm', 38, 31000, 'Art Director')
tom = Manager('Tom Clover', 31, 37000)

db = shelve.open('shelve-class')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()