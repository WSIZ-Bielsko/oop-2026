def first[T](items: list[T]) -> T | None:
    return items[0] if items else None


if __name__ == '__main__':
    result = first([1, 2, 3])  # T inferred as int

    result2 = first(['ab', 'cd'])
    print(result2.upper())
