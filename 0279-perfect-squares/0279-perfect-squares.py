class Solution:
    def numSquares(self, n: int) -> int:
        # Build sorted perfect squares
        sorted_perfect_squares = []
        for i in range(1, 101):
            perfect_square = i * i
            sorted_perfect_squares.append( perfect_square )
        
        # Find the left most perfect square number <= n
        upper_index = bisect.bisect_right(sorted_perfect_squares, n)
        
        todo = deque()
        for ps_num in reversed(range(upper_index)):
            todo.append([ sorted_perfect_squares[ps_num], 1 ])
        
        while todo:
            cur_ps_num, count = todo.popleft()
            if cur_ps_num == n:
                return count
            
            for ps_index in reversed(range(upper_index)):
                next_ps_num = sorted_perfect_squares[ps_index] + cur_ps_num
                if next_ps_num == n:
                    return count + 1
                    
                if next_ps_num < n:
                    todo.append( [next_ps_num, count + 1] )
        
        return 1453