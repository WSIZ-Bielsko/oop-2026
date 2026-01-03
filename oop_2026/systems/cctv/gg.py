if __name__ == '__main__':
    vision1 = [
        '       *            ',
        '    *               ',
        '   **    *          ',
        '   ****  *          ',
        '    ****            ',
        '     ****           ',
        '  *  ***   *        ',
        '  * **  *  *        ',
        ' **                 ',
        ' *                  ',
    ]

    n_cols = len(vision1[0])
    sol = [0] * n_cols
    for line in vision1:
        for c in range(n_cols):
            zzz = line[c]
            sol[c] += 1 if zzz == '*' else 0
    print(sol)

