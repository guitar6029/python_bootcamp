acceptable_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q']

turn = 'x'  # goes first

# game board (what players see)
board = [
    ['*'] * 3,
    ['*'] * 3,
    ['*'] * 3,
]

# helper board to show cell numbers
boardCell = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]


def turn_sign(turn):
    return 'o' if turn == 'x' else 'x'


def print_board(b):
    for row in b:
        for col in row:
            print(col, end="|")
        print("")  # newline after each row
    print("")      # extra space after board


def check_who_won(b):
    # all 8 possible winning lines
    winning_lines = [
        # rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for line in winning_lines:
        cells = [b[r][c] for (r, c) in line]
        # all three equal and not empty
        if cells[0] != '*' and cells[0] == cells[1] == cells[2]:
            return cells[0]  # 'x' or 'o'
    return None


def is_draw(b):
    # draw if no '*' left anywhere
    for row in b:
        for cell in row:
            if cell == '*':
                return False
    return True


def placeSignOnBoard(userinput, turn):
    # validate input
    if userinput not in ['1','2','3','4','5','6','7','8','9']:
        print(f"Invalid input: {userinput}")
        return False

    pos = int(userinput) - 1  # 0–8
    row = pos // 3            # 0,1,2
    col = pos % 3             # 0,1,2

    if board[row][col] != '*':
        print("Cell already taken, choose another.")
        return False

    board[row][col] = turn
    return True


def game():
    global turn
    gameOver = False

    while not gameOver:
        print(f"You are {turn}")
        print_board(board)
        print("Cell layout:")
        print_board(boardCell)

        userinput = input("Enter a cell number (1-9) or 'q' to quit:\n")
        
        # check if input is valid and part of the aceeptable array
        while userinput not in acceptable_values:
            # ask for input again
            print("The value is not accepted, please enter 1 - 9 , or q to quit")
            userinput = input("Enter a cell number (1-9) or 'q' to quit:\n")



        if userinput == 'q':
            print("Quitting game.")
            break

        # if move was invalid or cell taken, ask again
        if not placeSignOnBoard(userinput, turn):
            continue

        # after a valid move, check for winner or draw
        winner = check_who_won(board)
        if winner:
            print_board(board)
            print(f"Player '{winner}' wins! 🎉")
            gameOver = True
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            gameOver = True
        else:
            # no winner, no draw → next player's turn
            turn = turn_sign(turn)


# init the game
game()
