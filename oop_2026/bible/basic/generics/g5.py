from typing import Protocol


class MyProtocol(Protocol):
    def __len__(self) -> int: ...

    pass
