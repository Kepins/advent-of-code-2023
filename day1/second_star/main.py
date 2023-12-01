import string
import sys


written_digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_digit(substr: str):
    if substr[0] in string.digits:
        return int(substr[0])

    for key, value in written_digits.items():
        if len(substr) >= len(key) and substr[:len(key)] == key:
            return value

    return None


def get_number_from_line(line: str) -> int:
    i = 0

    first_digit = get_digit(line[i:])
    while not first_digit:
        i += 1
        first_digit = get_digit(line[i:])

    i = len(line) - 1
    last_digit = get_digit(line[i:])
    while not last_digit:
        i -= 1
        last_digit = get_digit(line[i:])

    return 10*first_digit+last_digit


if __name__ == "__main__":
    sum = 0
    while line := sys.stdin.readline():
        line = line.replace("\n", "")
        sum += get_number_from_line(line)

    print(sum)
