from copy import deepcopy

import aoc_13


inp = aoc_13.from_file("input.txt", keep_blank=True)
N = []


def scan_rows(N, prev=None):
    ROWS = len(N)
    for row in range(ROWS - 1):
        cur_row = N[row]
        next_row = N[row + 1]
        if cur_row == next_row:
            top, bot = row, row + 1
            while True:
                if (top == 0 or bot == ROWS - 1) and N[top] == N[bot]:
                    refl = (row + 1) * 100
                    if prev == None:
                        return refl
                    if prev == refl:
                        break
                    return refl
                if N[top] != N[bot]:
                    break
                else:
                    top -= 1
                    bot += 1
    return 0


def get_col(N, col):
    return [x[col] for x in N]


def scan_cols(N, prev=None):
    COLS = len(N[0])
    for col in range(COLS - 1):
        cur_col = get_col(N, col)
        next_col = get_col(N, col + 1)
        if cur_col == next_col:
            left, right = col, col + 1
            while True:
                if (left == 0 or right == COLS - 1) and get_col(N, left) == get_col(N, right):
                    refl = col + 1
                    if prev == None:
                        return refl
                    if prev == refl:
                        break
                    return refl
                if get_col(N, left) != get_col(N, right):
                    break
                else:
                    left -= 1
                    right += 1
    return 0


def search_p1(N):
    rs = scan_rows(N)
    cs = scan_cols(N)
    return rs + cs


def search_p2(N, prev):
    for row in range(len(N)):
        for col in range(len(N[0])):
            NN = deepcopy(N)
            NN[row][col] = "#" if NN[row][col] == "." else "."
            rs = scan_rows(NN, prev)
            cs = scan_cols(NN, prev)
            if rs != 0:
                return rs
            if cs != 0:
                return cs
    return 0


s1 = 0
s2 = 0
for line in inp:
    if line == "":
        p1_refl = search_p1(N)
        s1 += p1_refl
        p2_refl = search_p2(N, p1_refl)
        print(p2_refl)
        s2 += p2_refl
        N = []
    else:
        N.append([h for h in line])

p1_refl = search_p1(N)
s1 += p1_refl
print(s1)
p2_refl = search_p2(N, p1_refl)
print(p2_refl)
s2 += p2_refl
print(s2)

