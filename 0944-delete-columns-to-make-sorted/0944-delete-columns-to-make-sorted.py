class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        M = len(strs)
        N = len(strs[0])
        
        count = 0
        for col in range(N):
            for row in range(1, M):
                cur_char = strs[row][col]
                prev_char = strs[row - 1][col]
                if prev_char > cur_char:
                    count += 1
                    break
        
        return count