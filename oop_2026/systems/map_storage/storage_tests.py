import pytest

from oop_2026.systems.map_storage.base import MapStorage, BlockStorage, DictStorage
from oop_2026.systems.map_storage.storage_client import WebMapStorage


@pytest.fixture
def map_storage() -> MapStorage:
    # “certain” instance: always BlockStorage
    # return BlockStorage()
    # return DictStorage()
    return WebMapStorage(base_url="http://localhost:5007")


def test_simple(map_storage: MapStorage):
    d = map_storage
    d[11] = 'kadabra'
    d[2] = 'xiao'
    d[2] = 'xiao1'
    d[1] = d[11] + '---'
    print(d)


def test_simple2(map_storage: MapStorage):
    d = map_storage
    for k in range(1000):
        d[k] = k

    for k in range(1000):
        d[k] = k

    assert len(d) == 1000
