from datetime import datetime
from random import randint

from loguru import logger

from oop_2026.systems.map_storage.storage_dict_and_list import DictStorage, BlockStorage
from oop_2026.systems.map_storage.storage_files import FileStorage
from oop_2026.systems.map_storage.storage_mmap import MMapedStorage


def ts():
    return datetime.now().timestamp()


def perf_test_1():
    SZ = 10**7
    n_elems = 10**5
    keys = [randint(0, SZ-1) for _ in range(n_elems)]
    vals = [randint(0, SZ-1) for _ in range(n_elems)]

    # storage = DictStorage()
    # storage = FileStorage()
    # storage = BlockStorage()
    storage = MMapedStorage(max_items=2 * 10**7)
    storage.clear()
    st = ts()
    for k, v in zip(keys, vals):
        storage[k] = v
    storage.mm.flush()

    logger.info(f"Took {ts() - st:.4f} seconds")


if __name__ == '__main__':
    perf_test_1()