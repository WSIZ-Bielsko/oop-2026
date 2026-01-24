def maximum[T: (int, float)](a: T, b: T) -> T:
    return a if a > b else b   # ty: ignore[unsupported-operator]


if __name__ == '__main__':
    result = maximum('1', '2')  # Valid: int
