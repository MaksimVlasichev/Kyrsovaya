import random
class Person():#наш чипиздрик
    def __init__(self, userName, password):
        self.userName = userName
        self.pssword = password
        self.perm = 1#random.randint(0,1)
        self.id = random.randint(1000000,9999999)
newUser = Person("ivan", 123)
