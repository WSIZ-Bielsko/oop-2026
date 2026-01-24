import requests

from oop_2026.systems.map_storage.base import MapStorage


class WebMapStorage(MapStorage):

    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url

    def __getitem__(self, key):
        response = requests.get(f"{self.base_url}/items/{key}")
        if response.status_code == 404:
            raise KeyError(key)
        response.raise_for_status()
        return response.json()["value"]

    def __setitem__(self, key, value):
        response = requests.post(
            f"{self.base_url}/items",
            json={"key": key, "value": value}
        )
        response.raise_for_status()

    def __len__(self):
        response = requests.get(f"{self.base_url}/length")
        response.raise_for_status()
        return response.json()["length"]

    def keys(self):
        response = requests.get(f"{self.base_url}/keys")
        response.raise_for_status()
        return response.json()["keys"]


if __name__ == '__main__':
    storage = WebMapStorage("http://localhost:5007")
    storage["foo"] = "bar"
    storage["baz"] = 42
    print(storage["foo"])  # "bar"
    print(len(storage))  # 2
    print(list(storage.keys()))  # ["baz", "foo"]
    print(storage)  # {baz: 42, foo: bar}
