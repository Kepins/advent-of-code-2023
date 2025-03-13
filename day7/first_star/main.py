import string
from collections import namedtuple, Counter


card_strengths = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}
for c in string.digits:
    card_strengths[c] = int(c)


def has_5(char_counts):
    return 5 in char_counts.values()


def has_4(char_counts):
    return 4 in char_counts.values()


def has_full_house(char_counts):
    return 2 in char_counts.values() and 3 in char_counts.values()


def has_two_pairs(char_counts):
    pairs = 0
    for v in char_counts.values():
        if v == 2:
            pairs += 1
    return pairs == 2


def has_three_of_a_kind(char_counts):
    return 3 in char_counts.values()


def has_pair(char_counts):
    return 2 in char_counts.values()


def to_comparable(hand):
    char_counts = Counter(hand)

    combo_strength = 1

    if has_5(char_counts):
        combo_strength = 7
    elif has_4(char_counts):
        combo_strength = 6
    elif has_full_house(char_counts):
        combo_strength = 5
    elif has_three_of_a_kind(char_counts):
        combo_strength = 4
    elif has_two_pairs(char_counts):
        combo_strength = 3
    elif has_pair(char_counts):
        combo_strength = 2

    card_values = [card_strengths[c] for c in hand]
    card_values.insert(0, combo_strength)
    return card_values



if __name__ == "__main__":

    line = namedtuple("line", ("hand", "bid"))

    puzzle_input = []

    while True:
        try:
            line_str = input()
            puzzle_input.append(line(line_str.split(" ")[0], int(line_str.split(" ")[1])))
        except EOFError:
            break

    puzzle_input.sort(key=lambda x: to_comparable(x.hand))

    sum = 0
    for i, line in enumerate(puzzle_input):
        sum += (i+1) * line.bid

    print(sum)
