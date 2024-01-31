class ConnectFour():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['-' for i in range(width)] for i in range(height)]
        self.levels = [height - 1 for i in range(width)]
        self.playerOneTurn = True
        gameOver = False
        while not gameOver:
            gameOver = self.makeMove()
        
    def makeMove(self):
        print('Input your column!')
        col = int(input())
        
        if 0 <= col < self.width:
            row = self.levels[col]
        else:
            print('Invalid Move')
        if not 0 <= row < self.height:
            print('Invalid Move')
        else:
            self.levels[col] -= 1
            self.board[row][col] = self.whoseTurn()
            self.printBoard()
        return self.checkForWinner()
    
    def checkForWinner(self):
        for row in self.board:
            strRow = ''.join(row)
            if 'YYYY' in strRow or 'XXXX' in strRow:
                print('We have a winner row wise!')
                return True
        for col in range(self.width):
            strCol = ''
            for row in range(self.height):
                strCol += self.board[row][col]
            if 'YYYY' in strCol or 'XXXX' in strCol:
                print('We have a winner column wise!')
                return True
        return False
        
    def whoseTurn(self):
        if self.playerOneTurn:
            symbol = 'X'
        else:
            symbol ='Y'
        self.playerOneTurn = not self.playerOneTurn
        return symbol
        
    def printBoard(self):
        for row in self.board:
            print(row)
