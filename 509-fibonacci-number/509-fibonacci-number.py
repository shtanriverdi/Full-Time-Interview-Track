class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * max(3, n + 1)
        return self.helper(n, memo)

    def helper(self, n, memo):
        if memo[n] != -1:
            return memo[n]
        if n == 0:
            return 0
        if n < 2:
            return 1
        
        l = self.helper(n - 1, memo)
        r = self.helper(n - 2, memo)
        
        memo[n] = l + r
        return l + r
