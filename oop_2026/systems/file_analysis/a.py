



def foo(a: int) -> str | int:
    if a<0:
        return "less then zero"
    else:
        return a


if __name__ == '__main__':
    print(foo(-10))