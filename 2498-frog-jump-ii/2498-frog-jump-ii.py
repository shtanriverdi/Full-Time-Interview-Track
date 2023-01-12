class Solution:
    def maxJump(self, stones: List[int]) -> int:
        size = len(stones)
        if size <= 3:
            return abs(stones[0] - stones[-1])
        
        answer = float("-inf")
        is_even = (size % 2 == 0)
        
        # Forward
        current_pos = 2
        while current_pos < size:
            answer = max(answer, abs(stones[current_pos - 2] - stones[current_pos]))
            current_pos += 2
            
        if is_even:
            answer = max(answer, abs(stones[-1] - stones[-2]))
            
        # Backward
        current_pos = (size - 3) if (is_even) else (size - 2)
        answer = max(answer, abs(stones[current_pos] - stones[-1]))
        
        current_pos -= 2
        while current_pos >= 0:
            answer = max(answer, abs(stones[current_pos] - stones[current_pos + 2]))
            current_pos -= 2
        
        answer = max(answer, abs(stones[0] - stones[2]))        
        
        return answer