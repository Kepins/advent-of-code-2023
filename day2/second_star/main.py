import sys
from collections import defaultdict

import ply.lex as lex
import ply.yacc as yacc

# Define the token names
tokens = (
    "GAME",
    "INTEGER",
    "COLON",
    "COLOR",
    "COMMA",
    "SEMICOLON",
)

# Define regular expressions for tokens
t_GAME = r'Game'
t_INTEGER = r'\d+'
t_COLON = r':'
t_COLOR = r'blue|red|green'
t_COMMA = r','
t_SEMICOLON = r';'


# Ignore whitespace
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling for invalid characters
def t_error(t):
    print(f"Invalid character: {repr(t.value[0])} at line {t.lineno}, position {t.lexpos}")
    raise SyntaxError(f"Invalid character: {repr(t.value[0])} at line {t.lineno}, position {t.lexpos}")


# Build the lexer
lexer = lex.lex()


def p_big_game_list(p):
    """big_game_list : big_game
                     | big_game big_game_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_big_game(p):
    """big_game : GAME INTEGER COLON small_game_list"""
    p[0] = {"game_num": int(p[2]), "game": p[4]}


def p_small_game_list(p):
    """small_game_list : small_game
                       | small_game SEMICOLON small_game_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_small_game(p):
    """small_game : num_with_color
                  | num_with_color COMMA small_game"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_num_with_color(p):
    """num_with_color : INTEGER COLOR"""
    p[0] = {"number": int(p[1]), "color": p[2]}


def p_error(p):
    print(f"Syntax error at '{p.value}'")


# Build the parser
parser = yacc.yacc()

# Example usage
# data_string = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """
#
# lexer.input.txt(data_string)

# Tokenize and print tokens
# for token in lexer:
#     print(token)


if __name__ == "__main__":
    input = sys.stdin.read()
    lexer.input(input)

    games = parser.parse(input, lexer)

    colors = ("red", "green", "blue",)

    sum = 0
    for game in games:
        num_occurrences = defaultdict(int)
        for small_game in game["game"]:
            for pair in small_game:
                if num_occurrences[pair["color"]] < pair["number"]:
                    num_occurrences[pair["color"]] = pair["number"]

        power = 1
        for color in colors:
            power *= num_occurrences[color]

        sum += power


    print(sum)
