import math

HUMAN = "X"
AI = "O"


def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]

    if all(position in ["X", "O"] for position in board):
        return "Draw"

    return None


def minimax(board, depth, is_maximizing):
    result = check_winner(board)

    if result == AI:
        return 10 - depth

    if result == HUMAN:
        return depth - 10

    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] not in ["X", "O"]:
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = str(i + 1)
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] not in ["X", "O"]:
                board[i] = HUMAN
                score = minimax(board, depth + 1, True)
                board[i] = str(i + 1)
                best_score = min(best_score, score)

        return best_score


def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] not in ["X", "O"]:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = str(i + 1)

            if score > best_score:
                best_score = score
                move = i

    return move


def human_move(board):
    while True:
        try:
            choice = int(input("Enter your move (1-9): "))

            if choice < 1 or choice > 9:
                print("Please enter a number from 1 to 9.")
                continue

            index = choice - 1

            if board[index] in ["X", "O"]:
                print("That position is already occupied.")
                continue

            board[index] = HUMAN
            break

        except ValueError:
            print("Please enter a valid number.")


def play_game():
    board = [str(i) for i in range(1, 10)]

    print("\n===================================")
    print("       TIC-TAC-TOE AI")
    print("===================================")
    print("You are X")
    print("AI is O")
    print("Choose positions from 1 to 9.")

    print_board(board)

    while True:
        human_move(board)
        print_board(board)

        result = check_winner(board)

        if result:
            break

        print("AI is thinking...")
        ai_index = best_move(board)
        board[ai_index] = AI

        print(f"AI chose position {ai_index + 1}.")
        print_board(board)

        result = check_winner(board)

        if result:
            break

    if result == HUMAN:
        print("🎉 Congratulations! You won!")

    elif result == AI:
        print("🤖 AI wins! Better luck next time.")

    else:
        print("🤝 It's a draw!")


def main():
    while True:
        play_game()

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if again not in ["yes", "y"]:
            print("\nThanks for playing Tic-Tac-Toe AI!")
            break


if __name__ == "__main__":
    main()