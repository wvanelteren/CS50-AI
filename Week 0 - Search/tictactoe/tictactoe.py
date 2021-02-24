"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)

    # Checks if the empty count is even or odd to determine player's turn
    # X always has the first move, so X's turn count is always odd
    if (empty_count % 2) == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # Iterate over board
    for r in range(len(board)):
        for c in range(len(board[r])):
            # If an empty spot is found on board, store index of r and c as coordinates as tuple
            if board[r][c] == EMPTY:
                possible_actions.add((r, c))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create deepcopy as to not overwrite original board
    board_copy = copy.deepcopy(board)

    # Iterate over board to position where move is intended based on coordinates defined in the action tuple
    for r in range(len(board_copy)):
        for c in range(len(board_copy[r])):
            if r == action[0] and c == action[1]:
                # Checks if spot is not already occupied, otherwise raises exception
                if board_copy[r][c] is not EMPTY:
                    raise Exception("Not a valid move")
                else:
                    # Updates board
                    board_copy[r][c] = player(board_copy)
                    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for r in range(len(board)):
        for c in range(len(board[r])):

            # check rows for winner
            if board[r][0] == board[r][1] == board[r][2] is not None:
                return board[r][0]

            # check columns for winner
            if board[0][c] == board[1][c] == board[2][c] is not None:
                return board[0][c]

            # check diagonals for winner
            if board[0][0] == board[1][1] == board[2][2] is not None:
                return board[0][0]
            elif board[0][2] == board[1][1] == board[2][0] is not None:
                return board[0][2]

    # If no winners, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks whether game is a tie
    if not any(EMPTY in row for row in board) and winner(board) is None:
        # print("Board is a tie")
        return True

    # Checks whether game has a winner
    if winner(board) is not None:
        # print(f" Winning board: {board}")
        return True
    else:
        return False


def utility(terminal_board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(terminal_board) == X:
        return 1
    elif winner(terminal_board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Returns best move based on minimax algo
    if player(board) == X:
        return max_value(board)[1]
    elif player(board) == O:
        return min_value(board)[1]


def max_value(board):
    """
    Implementation of maximization pseudocode as described in the lecture
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_move = None

    for action in actions(board):
        _ = min_value(result(board, action))[0]
        if _ > v:
            v = _
            best_move = action

    return v, best_move


def min_value(board):
    """
    Implementation of minimization pseudocode as described in the lecture
    """
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_move = None

    for action in actions(board):
        _ = max_value(result(board, action))[0]
        if _ < v:
            v = _
            best_move = action

    return v, best_move



