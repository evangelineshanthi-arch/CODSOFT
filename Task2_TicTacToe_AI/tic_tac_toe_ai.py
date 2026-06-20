import math

board = [" " for _ in range(9)]

# Display Board
def display_board():
    print("\n")
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---|---|---")
    print("\n")

# Check Winner
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

# Check Draw
def is_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_ai):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_ai:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Human Move
def human_move():
    while True:
        try:
            move = int(input("Choose position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position!")
                continue

            if board[move] != " ":
                print("Position already taken!")
                continue

            board[move] = "X"
            break

        except ValueError:
            print("Enter a number between 1 and 9.")

# Main Game
print("=== TIC TAC TOE AI ===")
print("You are X")
print("""
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
""")

while True:
    display_board()

    human_move()

    if check_winner("X"):
        display_board()
        print("🎉 You Win!")
        break

    if is_draw():
        display_board()
        print("It's a Draw!")
        break

    print("AI is thinking...")
    ai_move()

    if check_winner("O"):
        display_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        display_board()
        print("It's a Draw!")
        break