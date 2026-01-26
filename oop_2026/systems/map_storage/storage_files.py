import os
import pickle
from collections.abc import Collection

from oop_2026.systems.map_storage.base import MapStorage


def save_data(data: Collection, filename: str) -> None:
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_data(filename: str) -> Collection:
    with open(filename, 'rb') as f:
        return pickle.load(f)


class FileStorage(MapStorage):
    def __init__(self, directory: str = "./data", items_per_file: int = 1000):
        # assumes keys are ints
        self.prefix = 'data'
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.directory = directory
        self.items_per_file = items_per_file
        self.file_items: list[set[int]] = []  # id's of elems in each file

    def __file_id(self, key: int) -> int:
        if not isinstance(key, int):
            raise TypeError(f"Key must be int, got {type(key)}")
        for i, file_items in enumerate(self.file_items):
            if key in file_items:
                return i
        raise KeyError(key)

    def __filename(self, file_id: int) -> str:
        return self.directory + '/' + self.prefix + f'{self.prefix}_{file_id}.pkl'

    def __getitem__(self, key):
        file_id = self.__file_id(key)
        elems = load_data(self.__filename(file_id))
        if key not in elems:
            raise KeyError(key)
        return elems[key]

    def __setitem__(self, key, value):
        try:
            file_id = self.__file_id(key)
            elems = load_data(self.__filename(file_id))
            elems[key] = value
            save_data(elems, self.__filename(file_id))

        except KeyError:
            # insert
            if len(self.file_items) > 0 and (len(self.file_items[-1]) < self.items_per_file):
                # into existing file
                file_id = len(self.file_items) - 1
                self.file_items[-1].add(key)
                elems = load_data(self.__filename(file_id))
                elems[key] = value
                save_data(elems, self.__filename(file_id))
            else:
                file_id = len(self.file_items)
                self.file_items.append({key})
                save_data({key: value}, self.__filename(file_id))

    def __len__(self):
        all_keys = sum([len(k) for k in self.file_items])
        return all_keys

    def keys(self):
        all_keys = set()
        for k in self.file_items:
            all_keys.update(k)
        return all_keys

    def clear(self):
        n_files = len(self.file_items)
        for i in range(n_files):
            os.remove(self.__filename(i))
        self.file_items = []

    def __repr__(self):
        return super().__repr__()


if __name__ == '__main__':
    d = FileStorage()
    d[1] = 'kadabra'
    d[2] = 'xiao'
    d[2] = 'xiao1'
    d[1] = d[1] + '---'
    d[3] = 38
    print(d)
    d.clear()
