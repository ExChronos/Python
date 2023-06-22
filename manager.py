from mark import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent+bonus)

tom = Manager('Tom Jones', 50)
print(tom)

if __name__ == '__main__':
    tom = Manager(name='Tom Chester', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)