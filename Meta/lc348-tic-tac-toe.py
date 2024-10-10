class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.Rsum = [[0] * n, [0] * n]
        self.Csum = [[0] * n, [0] * n]

        self.DLRsum = [0, 0]
        self.DRLsum = [0, 0]

        self.l = n

    def move(self, row: int, col: int, player: int) -> int:
        player -= 1

        self.Rsum[player][row] += 1
        self.Csum[player][col] += 1
        if row == col:
            self.DLRsum[player] += 1
        if row + col == self.l - 1:
            self.DRLsum[player] += 1
        
        if self.Rsum[player][row] == self.l or self.Csum[player][col] == self.l or self.DLRsum[player] == self.l or self.DRLsum[player] == self.l:
            return player + 1
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)