class Solution:
    def helper(self, A, A_idx, A_len, B, B_idx, B_len, memo):
        if A_idx == A_len or B_idx == B_len:
            return 0
        
        if (A_idx, B_idx) in memo:
            return memo[(A_idx, B_idx)]
        
        answer = 0
        if A[A_idx] == B[B_idx]:
            answer = 1 + self.helper(A, A_idx + 1, A_len, B, B_idx + 1, B_len, memo)
        else:
            option_1 = self.helper(A, A_idx + 1, A_len, B, B_idx, B_len, memo)
            option_2 = self.helper(A, A_idx, A_len, B, B_idx + 1, B_len, memo)
            answer = max(option_1, option_2)
            
        memo[(A_idx, B_idx)] = answer
        return answer
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = defaultdict(int)
        
        A_len = len(text1)
        B_len = len(text2)
        
        return self.helper(list(text1), 0, A_len, list(text2), 0, B_len, memo)