class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0
        size = len(blocks)
        answer = float("inf")
        
        for i in range(size):
            if blocks[i] == 'W':
                white_count += 1
                
            if (i - k) >= 0 and blocks[i - k] == 'W':
                white_count -= 1
                
            if (i + 1) >= k:
                answer = min(answer, white_count)
            
        return answer