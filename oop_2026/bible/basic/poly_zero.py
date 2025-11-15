class B:
    def __init__(self, a):
        self.a = a

    def say_hello(self):
        print("Hello world!")

    def report_square(self):
        print(f'square: {self.a ** 2}')


class D(B):
    pass


class E(B):
    def say_hello(self):
        print("Hello world from E!")

if __name__ == '__main__':
    b = B(3)
    b.say_hello()
    b.report_square()

    d = D(3)
    d.say_hello()
    d.report_square()

    e = E(3)
    e.say_hello()
    e.report_square()