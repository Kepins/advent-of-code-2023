from typing import List


def parse(line: str) -> (List[int], List[int]):
    numbers = line.split(":")[1]

    winning_numbers = numbers.split("|")[0]
    player_numbers = numbers.split("|")[1]

    winning_numbers = {int(num) for num in winning_numbers.split(" ") if num}
    player_numbers = {int(num) for num in player_numbers.split(" ") if num}

    return winning_numbers, player_numbers


def points_from_line(line: str, copies_list: List[int]) -> int:
    winning_numbers, player_numbers = parse(line)

    matches = 0

    for w_n in winning_numbers:
        if w_n in player_numbers:
            matches += 1

    try:
        copies_of_line = copies_list.pop(0)
    except IndexError:
        copies_of_line = 1

    for i in range(matches):
        try:
            copies_list[i] = copies_list[i] + copies_of_line
        except IndexError:
            copies_list.append(1 + copies_of_line)

    return copies_of_line


if __name__ == "__main__":
    sum_points = 0
    copies_list = []
    while True:
        try:
            line = input()
            sum_points += points_from_line(line, copies_list)
        except EOFError:
            break

    print(sum_points)
