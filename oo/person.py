class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0+percent)
    def __str__(self):
        return '<%s => %s => %s>' % (self.__class__.__name__,self.name, self.pay)

if __name__ == '__main__':
    bob = Person('bob smith', 42, 30000, 'software')
    sue = Person('sue jones', 45, 40000, 'hardware')
    print('bob name',bob.name)
    print(bob)

    print(bob.lastName())
    print('[sue] before raise', sue.pay)
    sue.giveRaise(0.2)
    print('[sue] after raise', sue.pay)

