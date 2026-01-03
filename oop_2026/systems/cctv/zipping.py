if __name__ == '__main__':
    w = [1, 2, 3, 4]
    g = [0, 1, 0, 1]
    t = ['a', 'b', 'c', 'x', 'y']

    n = len(w)
    for i in range(n):
        name = w[i]
        gender = g[i]
        code = t[i]


    for name, gender, code in zip(w, g, t):
        print(name, gender, code)