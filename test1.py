
class Dog:
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name

    def tell_name(self, pozdrav):
        self.pozdrav = pozdrav
        print(pozdrav, "my name", self.name)

Haf = Dog("Sandy", 20)

Haf.tell_name("Ahoj")

fridge_contents = {"egg":12, "milk": 2, "apple": 6, "celery": 5}

for variable1, variable2 in fridge_contents.items():
    if variable1 in fridge_contents:
        print(fridge_contents[variable1])
    if variable2 in fridge_contents:
        print(fridge_contents[variable2])
