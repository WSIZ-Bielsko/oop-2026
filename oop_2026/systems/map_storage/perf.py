import os
from datetime import datetime
from random import randint

from loguru import logger

from oop_2026.systems.map_storage.storage_dict_and_list import DictStorage, BlockStorage
from oop_2026.systems.map_storage.storage_files import FileStorage
from oop_2026.systems.map_storage.storage_mmap import MMapedStorage, NumpyMemStorage


def ts():
    return datetime.now().timestamp()


def perf_test_1():
    logger.info(f"Starting perf test 1, current dir: {os.getcwd()}")
    SZ = 10 ** 7
    n_elems = 10 ** 5
    keys = [randint(0, SZ - 1) for _ in range(n_elems)]
    vals = [randint(0, SZ - 1) for _ in range(n_elems)]

    # storage = DictStorage()
    # storage = FileStorage()
    # storage = BlockStorage()
    # storage = MMapedStorage(max_items=2 * 10**7, storage_file='/pool/sdc_1t/space/data/mmapfile.bin')
    storage = NumpyMemStorage(max_items=2 * 10 ** 7)
    times = []
    for i in range(20):
        logger.info(f"iteration {i}")
        storage.clear()
        st = ts()
        for k, v in zip(keys, vals):
            storage[k] = v
        # storage.mm.flush()
        times.append(ts() - st)

    times.sort()

    logger.info(f"Took {times[len(times) // 2]:.4f} seconds (median)")


if __name__ == '__main__':
    perf_test_1()
