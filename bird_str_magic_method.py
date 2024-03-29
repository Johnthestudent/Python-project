#Code overwrites the behavior of the __str__ magic method
#Usage example around the last lines of the program
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(format(self.name) + " bird can fly")
        return format(self.name) + " bird can fly"

    def walk(self):
        print(format(self.name) + " bird can walk")
        return format(self.name) + " bird can walk"

    def __str__(self):
        print(self.name + " bird can walk and fly ")
        return self.name + " bird can walk and fly"


class FlyingBird(Bird):
    def __init__(self, name, ration="insect"):
        self.name = name
        self.ration = ration
        if (self.name == "Canary"):
            self.ration = "grains"

    def eat(self):
        print("It eats mostly " + format(self.ration))
        return "It eats mostly " + format(self.ration)

    def fly(self):
        print(format(self.name) + " bird can fly")
        return format(self.name) + " bird can fly"

    def walk(self):
        print(format(self.name) + " bird can walk")
        return format(self.name) + " bird can walk"

    def str(self):
        super().__str__(self)


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        self.name = name
        self.ration = ration
        if (self.name == "Ostrich" or self.name == "Emu"):
            self.ration = "grains"

    def swim(self):
        print(format(self.name) + " bird can swim")
        return format(self.name) + " bird can swim"

    def eat(self):
        print("It eats mostly " + format(self.ration))
        return "It eats mostly " + format(self.ration)


class SuperBird(NonFlyingBird):
    def __init__(self, name, ration="fish"):
        self.name = name
        self.ration = ration
        if (self.name == "Seagull"):
            self.ration = "fish"

    def __str__(self):
        print(self.name + " bird can walk, swim and fly")
        return self.name + " bird can walk, swim and fly"

    def eat(self):
        super().eat()
        return "It eats mostly " + format(self.ration)

b = Bird("Any")
b.walk()

p = NonFlyingBird("Penguin", "fish")
p.swim()
p.eat()

c = FlyingBird("Canary")
str(c)
c.eat()

s = SuperBird("Gull")
str(s)
s.eat()