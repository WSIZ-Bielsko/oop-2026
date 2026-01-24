from typing import Protocol


class Comparable(Protocol):
    def __gt__(self, other) -> bool: ...


def maximum[T: Comparable](a: T, b: T) -> T:
    return a if a > b else b


if __name__ == '__main__':
    print(maximum('1', '2'))
