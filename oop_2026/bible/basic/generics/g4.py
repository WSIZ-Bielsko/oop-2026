from collections.abc import Sized
from datetime import datetime


def get_length[T: Sized](item: T) -> int:
    return len(item)


length = get_length([1, 2, 3])  # Valid: a list is Sized
print(length)


w = datetime.now()
# g = get_length(w)


class A(Sized):
    def __len__(self):
        return 1

a = A()
print(get_length(a))


