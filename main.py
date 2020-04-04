import numpy
from termcolor import colored

game_board = numpy.zeros((6,7))
full_columns = []

def main():
    global game_board
    print(game_board)

def pretty_print(active_player):
    global game_board
    if active_player:
        print("\nMy turn!\n")
    else:
        print("\nYour turn!\n")

    print("  0   1   2   3   4   5   6  ")
    for row in game_board:
        output = "| "
        for col in row:
            if col == 0:
                output += " "
            elif col == 1:
                output += colored('O', 'red')
                # output += "O"
            else:
                output += colored('O', 'blue')
                # output += "O"
            output += " | "
        print(output)
    print("|\/\/\/\/\/\/\/\/\/\/\/\/\/\|")


# def check_if_over(game_board, )
pretty_print(False)

