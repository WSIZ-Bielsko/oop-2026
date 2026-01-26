from collections.abc import Generator

import pytest

from oop_2026.systems.map_storage.base import MapStorage
from oop_2026.systems.map_storage.storage_client import WebMapStorage
from oop_2026.systems.map_storage.storage_dict_and_list import BlockStorage, DictStorage
from oop_2026.systems.map_storage.storage_files import FileStorage
from oop_2026.systems.map_storage.storage_mmap import MMapedStorage


# -- runs tests for all 3 types of storage
# @pytest.fixture(params=["block", "dict", "web"])
# @pytest.fixture(params=["file"])
@pytest.fixture(params=["mmap"])
def map_storage(request) -> Generator[MapStorage]:
    if request.param == "block":
        storage = BlockStorage()
    elif request.param == "dict":
        storage = DictStorage()
    elif request.param == "web":
        storage = WebMapStorage(base_url="http://localhost:5007")
    elif request.param == "file":
        storage = FileStorage()
    elif request.param == "mmap":
        storage = MMapedStorage()
    else:
        raise RuntimeError(f"Unknown storage type: {request.param}")

    storage.clear()

    yield storage

    storage.clear()


def test_simple_strs(map_storage: MapStorage):
    d = map_storage
    d[11] = 'kadabra'
    d[2] = 'xiao'
    d[2] = 'xiao1'
    d[1] = d[11] + '---'
    print(d)


def test_simple_ints(map_storage: MapStorage):
    d = map_storage
    d[11] = 8
    d[2] = 1
    d[2] = 2
    d[1] = d[11] + 8
    print(d)


def test_simple2(map_storage: MapStorage):
    d = map_storage
    for k in range(1000):
        d[k] = k

    for k in range(1000):
        d[k] = k

    assert len(d) == 1000
