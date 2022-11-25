class Solution:
    def isFeasible(self, i, j, digit, row_sets, col_sets, box_sets):
        if digit in row_sets[i] or digit in col_sets[j] or digit in box_sets[(i // 3, j // 3)]:
            return False
        return True
    
    def add(self, i, j, digit, row_sets, col_sets, box_sets):
        row_sets[i].add( digit )
        col_sets[j].add( digit )
        box_sets[(i // 3, j // 3)].add( digit )
        
    def pop(self, i, j, digit, row_sets, col_sets, box_sets):
        row_sets[i].remove( digit )
        col_sets[j].remove( digit )
        box_sets[(i // 3, j // 3)].remove( digit )
    
    def helper(self, cur_dot_index, dots_len, row_sets, col_sets, box_sets, dots, board):
        if cur_dot_index == dots_len:
            return True
        
        dot_i, dot_j = dots[cur_dot_index]
        for d in range(1, 10):
            digit = str(d)
            canBePut = self.isFeasible(dot_i, dot_j, digit, row_sets, col_sets, box_sets)
            if canBePut:
                board[dot_i][dot_j] = digit
                self.add(dot_i, dot_j, digit, row_sets, col_sets, box_sets)
                solved = self.helper(cur_dot_index + 1, dots_len, row_sets, col_sets, box_sets, dots, board)
                if solved:
                    return True
                self.pop(dot_i, dot_j, digit, row_sets, col_sets, box_sets)
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        box_sets = defaultdict(set)
        
        dots = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row_sets[i].add( board[i][j] )
                    col_sets[j].add( board[i][j] )
                    box_sets[(i // 3, j // 3)].add( board[i][j] )
                else:
                    dots.append( (i, j) )
        
        self.helper(0, len(dots), row_sets, col_sets, box_sets, dots, board)