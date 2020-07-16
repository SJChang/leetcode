class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        
        return self.isRowValid(board) and self.isColValid(board) and self.isThreeValid(board)
    
    def isRowValid(self, board):
        n = len(board)
        for r in range(n):
            row = [x for x in board[r] if x != '.']
            if len(set(row)) != len(row):
                return False
        return True
    
    def isColValid(self, board):
        n = len(board)
        for c in range(n):
            col = [board[r][c] for r in range(n) if board[r][c] != '.']
            if len(set(col)) != len(col):
                return False
        return True
    
    def isThreeValid(self, board):
        n = len(board)
        for r in range(0,n,3):
            for c in range(0,n,3):
                cell =[]
                for i in range(3):
                    for j in range(3):
                        num = board[r+i][c+j]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
                
        return True