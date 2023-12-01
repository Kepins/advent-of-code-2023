import string
import sys


def get_number_from_line(line: str) -> int:
    i = 0
    while line[i] not in string.digits:
        i += 1
    first_digit = line[i]

    i = len(line) - 1

    while line[i] not in string.digits:
        i -= 1
    last_digit = line[i]

    return int(first_digit+last_digit)


if __name__ == "__main__":
    sum = 0
    while line := sys.stdin.readline():
        sum += get_number_from_line(line)

    print(sum)
