import string
from itertools import product


def remove_number(matrix, x, y):
    row = matrix[y]

    beg = x
    while beg > 0 and row[beg-1] in string.digits:
        beg -= 1

    end = x
    while end < len(row) - 1 and row[end+1] in string.digits:
        end += 1

    number = int("".join(row[beg: end+1]))

    for i in range(beg, end+1):
        row[i] = "."

    return number


if __name__ == "__main__":
    matrix = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        mat_line = []
        for c in line:
            mat_line.append(c)
        matrix.append(mat_line)

    sum = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            c = matrix[y][x]
            if c not in string.digits and c != ".":
                # c is a part
                for dx, dy in product({-1, 0, 1}, {-1, 0, 1}):
                    neigh_c = matrix[y + dy][x+dx]
                    if neigh_c in string.digits:
                        sum += remove_number(matrix, x + dx, y + dy)

    print(sum)
