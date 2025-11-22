from abc import ABC, abstractmethod


class SortableItem(ABC):
    # dodajemy taki interfejs... by explicite poinformować kodera, które obiekty mogą być sortowalne...

    @abstractmethod
    def __lt__(self, other) -> bool:
        pass


class G(SortableItem):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"G({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other) -> bool:
        return self.x < other.x or (self.x == other.x and self.y < other.y)


if __name__ == '__main__':
    g1 = G(1, 2)
    print(g1)
    g2 = G(1, 2)
    print(g2)

    print(g1 == g2)
    print(g1 < g2)
