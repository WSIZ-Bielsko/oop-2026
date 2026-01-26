import os
import numpy as np

from oop_2026.systems.map_storage.base import MapStorage


class MMapedStorage(MapStorage):
    def __init__(self, storage_file: str = "./mmaped_stogage.bin", max_items=10000):
        # assumes keys are ints
        self.mm = np.memmap(storage_file, dtype=np.int32, mode='w+', shape=(max_items,))
        # self.mm[:] = 0 # not needed; OS should fill it with zeros
        self.max_items = max_items
        self.used_keys = np.zeros(max_items, dtype=np.bool_)

    def __validate_key(self, key):
        if not isinstance(key, int):
            raise TypeError(f"Key must be int, got {type(key)}")
        if key >= self.max_items:
            raise KeyError(f"Key {key} is out of range (max {self.max_items - 1})")

    def __getitem__(self, key):
        self.__validate_key(key)
        if not self.used_keys[key]:
            raise KeyError(key)
        return self.mm[key]

    def __setitem__(self, key, value):
        self.__validate_key(key)
        self.mm[key] = value
        self.used_keys[key] = True

    def __len__(self):
        return self.used_keys.sum()

    def keys(self):
        return np.where(self.used_keys)[0].tolist()

    def clear(self):
        self.mm[:] = 0
        self.used_keys[:] = False

    def __repr__(self):
        return super().__repr__()


if __name__ == '__main__':
    d = MMapedStorage()
    d[1] = 8
    d[2] = 12
    d[2] = 1
    d[1] = d[1] + 2
    d[3] = 38
    print(d)
    d.clear()
