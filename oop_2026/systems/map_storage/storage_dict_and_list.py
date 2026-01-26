from oop_2026.systems.map_storage.base import MapStorage


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

    def clear(self):
        self.data.clear()

    def keys(self):
        return sorted(self.data.keys())


class BlockStorage(MapStorage):

    def __init__(self):
        self.data = []  # [ [1,'kadabra'], [2, 'xiao'] ]

    def __getitem__(self, key):
        for block in self.data:
            if block[0] == key:
                return block[1]
        return None

    def __setitem__(self, key, value):
        # pass thru all pairs in self.data
        # if key found --> update value
        # if not found --> just append [key,value] to self.data
        for element in self.data:
            if element[0] == key:
                element[1] = value
                return
        self.data.append([key, value])

    def __len__(self):
        # just return the length of self.data
        return len(self.data)

    def keys(self):
        # pass thru all data in self.data; gather the item[0] elements (the keys) in some list...
        key_array = []
        for block in self.data:
            key_array.append(block[0])
        return key_array

    def clear(self):
        self.data.clear()
