from typing import List


def parse(line: str) -> (List[int], List[int]):
    numbers = line.split(":")[1]

    winning_numbers = numbers.split("|")[0]
    player_numbers = numbers.split("|")[1]

    winning_numbers = {int(num) for num in winning_numbers.split(" ") if num}
    player_numbers = {int(num) for num in player_numbers.split(" ") if num}

    return winning_numbers, player_numbers


def points_from_line(line: str) -> int:
    winning_numbers, player_numbers = parse(line)

    matches = 0

    for w_n in winning_numbers:
        if w_n in player_numbers:
            matches += 1

    return 2 ** (matches-1) if matches else 0


if __name__ == "__main__":
    sum_points = 0
    while True:
        try:
            line = input()
            sum_points += points_from_line(line)
        except EOFError:
            break

    print(sum_points)
