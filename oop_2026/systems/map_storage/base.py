from abc import abstractmethod, ABC
from collections.abc import *
from time import sleep


# MutableMapping
class MapStorage(ABC):

    @abstractmethod
    def __getitem__(self, key):
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def keys(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    def __repr__(self):
        s = []
        for k in self.keys():
            s.append(f'{k}: {self.__getitem__(k)}')
        return '{' + ', '.join(s) + '}'


if __name__ == '__main__':
    # d: dict[int, str] = DictStorage()
    pass
