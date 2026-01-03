def how_many(vision1):
    return [col.count('*') for col in zip(*vision1)]


if __name__ == '__main__':
    data = ex3 = [
        '  *  ',
        ' *** ',
        '*****',
        ' *** ',
        '  *  ',
    ]
    print(how_many(data))
