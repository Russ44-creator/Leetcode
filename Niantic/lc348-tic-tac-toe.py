class TicTacToe:

    def __init__(self, n: int):
        #key: (val,player) => set()
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.antiDiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        if row == col:
            self.antiDiag += 1 if player == 1 else -1
        if row + col == self.n - 1:
            self.diag += 1 if player == 1 else - 1
        self.row[row] += 1 if player == 1 else -1
        self.col[col] += 1 if player == 1 else -1
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.antiDiag) == self.n:
            return player
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)