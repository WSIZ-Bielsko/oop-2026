from loguru import logger


class Squares:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        # Using 'yield' here makes this method return a generator
        current = 0
        while current < self.limit:
            yield current * current
            logger.info(f"resuming")
            current += 1


if __name__ == '__main__':
    # Usage
    squares = Squares(5)

    # The class is now iterable (usable in for-loops)
    for num in squares:
        logger.warning(num)

    # Output:
    # 0
    # 1
    # 4
    # 9
    # 16
