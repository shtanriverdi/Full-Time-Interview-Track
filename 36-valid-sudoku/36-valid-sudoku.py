class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set = set()
        col_set = set()
        
        for i in range(9):
            for j in range(9):
                cur_num_row = board[i][j]
                if cur_num_row != '.' and cur_num_row in row_set:
                    return False
                else:
                    row_set.add(cur_num_row)
                    
                cur_num_col = board[j][i]
                if cur_num_col != '.' and cur_num_col in col_set:
                    return False
                else:
                    col_set.add(cur_num_col)
            row_set.clear()
            col_set.clear()     
            
        three_set = set()
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(i, i + 3):
                    for m in range(j, j + 3):
                        cur = board[k][m]
                        if cur != '.' and cur in three_set:
                            return False
                        else:
                            three_set.add(cur)
                three_set.clear()
                
        return True