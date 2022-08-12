class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = self.helper(x, abs(n))
        if n < 0:
            answer = 1 / answer
            
        return answer
        
    def helper(self, x, n):
        if n == 1:
            return x
        
        if n == 0:
            return 1
        
        half = self.helper(x, n // 2)
        # if n is even
        answer = half * half
        
        # if n is odd, also multiply by x
        if n % 2 != 0:
            answer = answer * x
            
        return answer