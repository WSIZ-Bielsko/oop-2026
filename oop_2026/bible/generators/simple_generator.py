from collections.abc import Generator

from loguru import logger


def count_up_to(n) -> Generator[int]:
    count = 1
    while count <= n:
        logger.info(f"yielding")
        yield count  # Pauses here, returns count
        logger.info(f"resuming")
        count += 1  # Resumes here next time


if __name__ == '__main__':
    # Usage
    gen = count_up_to(3)
    logger.info(next(gen))  # Output: 1
    logger.info('kadabra')
    logger.info(next(gen))  # Output: 2
