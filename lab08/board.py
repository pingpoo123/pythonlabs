class TicTacToeBoard:
    def __init__(self):
        self.restart()

    def get(self, col, row):
        return self._board[row][col]
    
    def is_empty(self, col, row):
        if self.get(col, row) == '-':
            return True
        else:
            return False
        
    def place(self, mark, col, row):
        self._board[row][col] = mark

    def print_board(self):
        for l in self._board:
            print(*l)
    
    def is_full(self):
        for l in self._board:
            if l.count('-') > 0:
                return False
        return True
    
    def restart(self):
        self._board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    
    def is_winner(self,mark):
        for row in self._board:
            if row.count(mark) == 3:
                return True
            
        for col in range(3):
            n = 0
            for row in range(3):
                if self._board[row][col] == mark:
                    n =+ 1
            if n == 3:
                return True
        
        n = 0
        for i in range(3):
            if self._board[i][i] == mark:
                n =+ 1
            if n == 3:
                return True
        print(n)

        return False

x = TicTacToeBoard()
x.place('X',0,0)
x.place('X',1,1)
x.place('X',2,2)
print(x.is_winner('X'))