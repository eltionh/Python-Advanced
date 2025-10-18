class Dog:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Woof")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Meow")


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Ciuu")

dog = Dog("Max")
cat = Cat("Kitten")
bird = Bird("bird")

for animal in (dog,cat,bird):
    animal.sound()