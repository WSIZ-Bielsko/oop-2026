def first[T](items: list[T]) -> T:
    print(type(items[0]))
    return items[0]


if __name__ == '__main__':
    result = first([1, 2, 3])  # T inferred as int

    result2 = first(['ab', 'cd'])
    print(result2.upper())

    first([3.14, 1.41])

    first([1, 1.12])

    # tuple[int] ... (1) .... (1,1,1);;; tuple[int,...]
    w = (1, 2)
    print(w)
