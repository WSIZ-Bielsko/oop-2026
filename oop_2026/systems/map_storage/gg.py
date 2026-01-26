class A:
    def __getitem__(self, item):
        return '---ha ha ha ---'

    def __setitem__(self, key, value):
        print(f'ah... setting {key}')


if __name__ == '__main__':
    a = A()
    a[12] = 5
    print(a[0])
