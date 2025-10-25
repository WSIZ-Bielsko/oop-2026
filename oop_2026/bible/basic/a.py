from random import randint


class Dog:
    def __init__(self, name, age):
        # konstruktor
        # atrybuty/pola
        self.name = name
        self.age = age
        self.mass = 10

    # metody
    def bark(self):
        return f"{self.name} says Woof!"

    def eat(self, food):
        self.mass += food


def random_dogs() -> list[Dog]:
    dog1 = Dog("Rex", 3)
    dog2 = Dog("Bella", 2)
    dog3 = Dog("Max", 5)
    dog4 = Dog("Luna", 1)

    return [dog1, dog2, dog3, dog4]


def feed_dogs(dogs: list[Dog]):
    for dog in dogs:
        dog.eat(randint(1, 10))


def sort_dogs_by_weight(dogs: list[Dog]) -> list[Dog]:
    return sorted(dogs, key=lambda d: d.mass)


def add(arg):
    arg += 1


if __name__ == '__main__':
    dogs = random_dogs()
    feed_dogs(dogs)
    print(id(dogs[0]))
    print(id(dogs[1]))
    print(id(dogs[2]))
    sorted_dogs = sort_dogs_by_weight(dogs)
    for dog in sorted_dogs:
        print(dog.name, dog.mass)

    fff = [1, 2, 3, 4]
    gg = fff
    gg[0] = 111
    print(fff)  # [111, 2, 3, 4]
    print(gg)

    z = 12
    add(z)
    print(z)  # 12


