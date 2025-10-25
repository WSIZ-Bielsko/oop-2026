from decimal import Decimal
from random import randint


class Dog:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_random_name():
        return "Rex" + str(randint(1, 100))

    @staticmethod
    def get_dog_for_qr_code(qr: str) -> "Dog":
        # parse QR
        return Dog('Rex99')


def is_number(obj) -> bool:
    """Check if an object is a number ... crude way..."""
    try:
        z = obj * obj
        return True
    except:
        return False


if __name__ == '__main__':
    d = Dog("Thiao")
    print(d.get_random_name())

    print(Dog.get_random_name())

    d2 = Dog.get_dog_for_qr_code('base64...')

    s = "๑๒๓๔๕"
    print(int(s))
