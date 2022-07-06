# Bottom Up DP O(N) Time & Space
class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * max(3, n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

    # Top Down with Recursion and Memoization O(N) Time & Space
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
    
# O(N) Time O(1) Space Iterative Solution
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
