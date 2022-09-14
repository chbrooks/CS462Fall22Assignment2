
### State representing a Tic-Tac-Toe board. ' ' is used for unfilled squares.

class TicTacToeState(State):
    def __init__(self, board=None):
        self.score = 0
        if board:
            self.board = board
        else:
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]


    def isGoal(self):
        ### we have a win
        if rowWin(self.board) or colWin(self.board) or diagonalWin(self.board):
            return True
        elif boardFull(self.board):
            return True
        else:
            return False

    ## move is either 'x' or 'o'
    def successors(self, move='x'):
        successorStates = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    newBoard = copy.deepcopy(self.board)
                    newBoard[i][j] = move
                    successorStates.append(TicTacToeState(newBoard))

        return successorStates

    ### player is either x or o
    def scoreSelf(self, player):
        winner = rowWin(self.board)
        if not winner:
            winner = colWin(self.board)
        if not winner:
            winner = diagonalWin(self.board)
        if winner:
            if winner == player:
                self.score = 1
            else:
                self.score = -1
        else :
            self.score = 0

    def __repr__(self):
        return " %s\n %s\n %s\n" % (self.board[0], self.board[1], self.board[2])




#############
## TicTacToeState

### Helper functions to determine whether we are at a leaf node.

def rowWin(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    return False


def colWin(board):
    for i in range(3):
        col = [item[i] for item in board]
        if len(set(col)) == 1 and col[0] != ' ' :
            return col[0]
    return False


def diagonalWin(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' ':
        return board[1][1]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != ' ':
        return board[1][1]
    else:
        return False


def boardFull(board):
    if any(x == ' ' for x in board[0]) or any(x == ' ' for x in board[1]) or any(x == ' ' for x in board[2]):
        return False
    else:
        return True
