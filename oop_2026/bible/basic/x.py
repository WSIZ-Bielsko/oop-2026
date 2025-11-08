class Shape:
    def __init__(self):
        print('creating shape')


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        print('creating square')


if __name__ == '__main__':
    square = Square(5)
