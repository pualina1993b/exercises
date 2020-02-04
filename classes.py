class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("john")
john.talk()


class Mammal():
    def walk(self):
        print("walk")
class Dog(Mammal):
    pass

class Cat(Mammal):
    pass


