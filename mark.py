from people_base import db
import pickle

Dbase = open('pickle-people', 'wb')
pickle.dump(db, Dbase)
Dbase.close()