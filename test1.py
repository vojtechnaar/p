
class Dog:
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name

    def tell_name(self, pozdrav):
        self.pozdrav = pozdrav
        print(pozdrav, "my name", self.name)

Haf = Dog("Sandy", 20)

Haf.tell_name("Ahoj")


