bob = {'name': 'Bob Smith', 'age': 45, 'job': 'developer', 'salary': 38000}
sue = {'name': 'Sue Darbont', 'age': 35, 'job': 'doctor', 'salary': 51000}
tom = {'name': 'Tom Crowler', 'age': 21, 'job': 'student', 'salary': 3500}

db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>', db['key'])

    