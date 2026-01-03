if __name__ == '__main__':
    v = [
        '  **',
        ' ** ',
        '****',
        '* **',
    ]
    cols = [[1 if v[i][c] == '*' else 0 for i in range(len(v))] for c in range(len(v[0]))]
    for c in cols:
        print(c, sum(c))

    one_d = ''.join(['*' if sum(c) >= 3 else ' ' for c in cols])
    print(f'[{one_d}]')

    ooo = ''.join(['*' if sum(c) >= 3 else ' ' for c in [[1 if v[i][c] == '*' else 0 for i in range(len(v))] for c in range(len(v[0]))]])

    print(f'[{ooo}]')
