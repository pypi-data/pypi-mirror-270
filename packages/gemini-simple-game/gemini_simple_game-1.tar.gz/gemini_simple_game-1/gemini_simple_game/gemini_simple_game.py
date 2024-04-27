"""
This file contains code for the game "Gemini Simple Game".
Author: SoftwareApkDev
"""

# Importing necessary libraries


import sys
import uuid
import copy
import google.generativeai as gemini
import os
from dotenv import load_dotenv
from mpmath import mp, mpf
from tabulate import tabulate

mp.pretty = True


# Creating static functions to be used in this game.


def is_number(string: str) -> bool:
    try:
        mpf(string)
        return True
    except ValueError:
        return False


def row_match(board: list, row_number: int, content: str) -> bool:
    if row_number < 0 or row_number > len(board):
        return False
    for i in range(len(board[row_number])):
        if board[row_number][i] != content:
            return False
    return True


def col_match(board: list, col_number: int, content: str) -> bool:
    if col_number < 0 or col_number > len(board[0]):
        return False
    for i in range(len(board[0])):
        if board[i][col_number] != content:
            return False
    return True


def diagonals_match(board: list, content: str) -> bool:
    first_diagonals_match: bool = True
    for i in range(len(board)):
        if board[i][i] != content:
            first_diagonals_match = False
            break

    if first_diagonals_match:
        return True

    for j in range(len(board)):
        if board[len(board) - 1 - j][j] != content:
            return False
    return True


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating main function used to run the game.


def main() -> int:
    """
    This main function is used to run the game.
    :return: an integer
    """

    load_dotenv()
    gemini.configure(api_key=os.environ['GEMINI_API_KEY'])

    # Asking user input values for generation config
    temperature: str = input("Please enter temperature (0 - 1): ")
    while not is_number(temperature) or float(temperature) < 0 or float(temperature) > 1:
        temperature = input("Sorry, invalid input! Please re-enter temperature (0 - 1): ")

    float_temperature: float = float(temperature)

    top_p: str = input("Please enter Top P (0 - 1): ")
    while not is_number(top_p) or float(top_p) < 0 or float(top_p) > 1:
        top_p = input("Sorry, invalid input! Please re-enter Top P (0 - 1): ")

    float_top_p: float = float(top_p)

    top_k: str = input("Please enter Top K (at least 1): ")
    while not is_number(top_k) or int(top_k) < 1:
        top_k = input("Sorry, invalid input! Please re-enter Top K (at least 1): ")

    float_top_k: int = int(top_k)

    max_output_tokens: str = input("Please enter maximum input tokens (at least 1): ")
    while not is_number(max_output_tokens) or int(max_output_tokens) < 1:
        max_output_tokens = input("Sorry, invalid input! Please re-enter maximum input tokens (at least 1): ")

    int_max_output_tokens: int = int(max_output_tokens)

    # Set up the model
    generation_config = {
        "temperature": float_temperature,
        "top_p": float_top_p,
        "top_k": float_top_k,
        "max_output_tokens": int_max_output_tokens,
    }

    # Gemini safety settings
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = gemini.GenerativeModel(model_name="gemini-1.0-pro",
                                   generation_config=generation_config,
                                   safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])
    convo.send_message("Please enter any integer between 3 and 6 inclusive!")
    board_len: int = int(convo.last.text.split("\n")[0])
    board: list = []
    for i in range(board_len):
        board.append([])
        board[i] = ["NONE"] * board_len

    turn: int = 0

    while True:
        clear()
        has_winner: bool = False  # initial value
        while not has_winner:
            print("You are playing as \"O\"!")
            print("Your opponent plays as \"X\"!")
            print("Below is the current board representation:\n" +
                  str(tabulate(board, headers='firstrow', tablefmt='fancy_grid')))
            turn += 1
            if turn % 2 == 1:
                print("It is your turn!")
                row_number: int = int(input("Please enter any row number between 0 and " + str(len(board) - 1)
                                      + " inclusive: "))
                col_number: int = int(input("Please enter any column number between 0 and " + str(len(board[0]) - 1)
                                      + " inclusive: "))
                while row_number < 0 or row_number >= len(board) or col_number < 0 or col_number >= len(board[0]) or \
                        board[row_number][col_number] != "NONE":
                    print("Sorry, invalid input!")
                    row_number: int = int(input("Please enter any row number between 0 and " + str(len(board) - 1)
                                          + " inclusive: "))
                    col_number: int = int(input("Please enter any column number between 0 and " + str(len(board[0]) - 1)
                                          + " inclusive: "))

                board[row_number][col_number] = "O"
            else:
                print("It is CPU's turn")
                convo.send_message("Please enter any integer between 0 and " + str(len(board) - 1) + " inclusive!")
                row_number: int = int(convo.last.text.split("\n")[0])
                convo.send_message("Please enter any integer between 0 and " + str(len(board[0]) - 1) + " inclusive!")
                col_number: int = int(convo.last.text.split("\n")[0])
                while row_number < 0 or row_number >= len(board) or col_number < 0 or col_number >= len(board[0]) or \
                        board[row_number][col_number] != "NONE":
                    convo.send_message("Please enter any integer between 0 and " + str(len(board) - 1) + " inclusive!")
                    row_number: int = int(convo.last.text.split("\n")[0])
                    convo.send_message("Please enter any integer between 0 and " + str(len(board[0]) - 1) + " inclusive!")
                    col_number: int = int(convo.last.text.split("\n")[0])

                board[row_number][col_number] = "X"

            for row in range(len(board)):
                if row_match(board, row, "O"):
                    print("You won!")
                    has_winner = True
                elif row_match(board, row, "X"):
                    print("CPU won!")
                    has_winner = True

            for col in range(len(board)):
                if col_match(board, col, "O"):
                    print("You won!")
                    has_winner = True
                elif col_match(board, col, "X"):
                    print("CPU won!")
                    has_winner = True

            if diagonals_match(board, "O"):
                print("You won!")
                has_winner = True
            elif diagonals_match(board, "X"):
                print("CPU won!")
                has_winner = True

        # Reset the game board
        convo = model.start_chat(history=[
        ])
        convo.send_message("Please enter any integer between 3 and 6 inclusive!")
        board_len = int(convo.last.text.split("\n")[0])
        board = []
        for i in range(board_len):
            board.append([])
            board[i] = ["NONE"] * board_len

        turn = 0

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_playing: str = input("Do you want to continue playing \"Gemini Simple Game\"? ")
        if continue_playing != "Y":
            return 0


if __name__ == '__main__':
    main()
