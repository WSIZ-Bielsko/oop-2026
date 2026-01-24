from abc import abstractmethod, ABC
from collections.abc import *


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

    def __repr__(self):
        pass


# first implementation
class DictStorage(MapStorage):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return len(self.data)

    def keys(self):
        return self.data.keys()

    def __repr__(self):
        s = []
        for k in self.keys():
            s.append(f'{k}: {self[k]}')
        return '{' + ' '.join(s) + '}'



if __name__ == '__main__':
    d: dict[int, str] = DictStorage()
    d[11] = 'kadabra'
    d[2] = 'xiao'

    d[1] = d[11] + '---'
    print(d)
