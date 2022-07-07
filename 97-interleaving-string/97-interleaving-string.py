class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        k = len(s3)
        
        if m + n != k:
            return False
        
        memo = {}
        
        return self.helper(0, 0, 0, k, m, n, list(s1), list(s2), list(s3), memo)
        
    def helper(self, cur, i, j, k, m, n, s1, s2, s3, memo) -> bool:
        if (cur, i, j) in memo:
            return memo[(cur, i, j)]
        
        if cur == k and i == m and j == n:
            return True
        
        result = False
        
        if i < m and s3[cur] == s1[i]:
            result |= self.helper(cur + 1, i + 1, j, k, m, n, s1, s2, s3, memo)
                
        if not result and j < n and s3[cur] == s2[j]:
            result |= self.helper(cur+ 1, i, j + 1, k, m, n, s1, s2, s3, memo)
        
        memo[(cur, i, j)] = result
        return result