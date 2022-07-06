class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        prev = 1
        prev2 = 0
        cur = 1
        
        for _ in range(2, n + 1):
            cur = prev + prev2
            prev2 = prev
            prev = cur
        
        return cur