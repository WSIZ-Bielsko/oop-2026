


class A:
    def __init__(self, x: int):
        self.x = x

    def __add__(self, other):
        return A(self.x + other.x)

    def __bool__(self):
        return self.x == 12


if __name__ == '__main__':
    a = A(1)
    a += A(2)


    print(a.x)
    a.x=12

    if a:
        # happens only if x=12
        print('yes')