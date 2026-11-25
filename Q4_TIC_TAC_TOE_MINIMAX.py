"""
EXPERIMENT 4: TIC-TAC-TOE USING MINIMAX
"""

board = [' ' for _ in range(9)]


def display_board():
    print()
    for i in range(0, 9, 3):
        row = []
        for j in range(i, i + 3):
            row.append(board[j] if board[j] != ' ' else str(j + 1))
        print(" | ".join(row))
        if i < 6:
            print("---------")
    print()


def check_winner(player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = 'O'


def play_game():
    print("TIC TAC TOE")
    print("You are X and AI is O")
    print("Enter position numbers from 1 to 9")
    display_board()

    while True:
        try:
            move = int(input("Enter your position: ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if move < 0 or move >= 9 or board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move] = 'X'
        display_board()

        if check_winner('X'):
            print("Human Wins!")
            break
        if ' ' not in board:
            print("Game Draw!")
            break

        print("AI is thinking...")
        ai_move()
        display_board()

        if check_winner('O'):
            print("AI Wins!")
            break
        if ' ' not in board:
            print("Game Draw!")
            break


if __name__ == "__main__":
    print("=== EXPERIMENT 4: TIC-TAC-TOE USING MINIMAX ===")
    play_game()
