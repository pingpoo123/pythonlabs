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
            
        for i in range(3):
            n = 0
            for r in range(3):
                if self._board[r][i] == mark:
                    n +=1
            if n == 3:
                return True
        
        if self._board[0][0] == mark and self._board[1][1] == mark and self._board[2][2] == mark:
            return True
        elif self._board[0][2] == mark and self._board[1][1] == mark and self._board[2][0] == mark:
            return True
        
        return False


if __name__ == '__main__':
    x = TicTacToeBoard()
    x.place('X',0,0)
    x.place('X',0,1)
    x.place('X',0,2)
    print(x.is_winner('X'))
    x.print_board()
