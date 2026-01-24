from dataclasses import dataclass
from typing import Any


@dataclass
class Person[IDType]:
    name: str
    age: int
    national_id: IDType | None = None


if __name__ == '__main__':
    d: dict[str, Person[str]] = {}  # --> should guess that IDType = str

    d['john'] = Person('John', 30)
    d['jane'] = Person('Jane', 29)
    d['jack'] = Person('Jack', 31)
    d['xiao'] = Person('Xiao', 28)

    dd: dict[str, str] = {}
    dd['aa'] = 'bb'
    dd[11] = 88

    print(dd)