class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for each row and column
        for i in range(9):
            col_set = set()
            row_set = set()
            for j in range(9):
                if board[i][j] in row_set or board[j][i] in col_set:
                    return False
                if board[i][j] != '.':
                    row_set.add( board[i][j] )
                if board[j][i] != '.':
                    col_set.add( board[j][i] )
                
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                three_set = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] in three_set:
                            return False
                        if board[i][j] != '.':
                            three_set.add( board[i][j] )
        
        return True