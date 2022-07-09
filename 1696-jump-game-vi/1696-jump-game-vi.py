from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        mono_dec_deque = deque([nums[0]])
        
        left = 0
        for right in range(1, n):
            # Update monothonic decreasing dequeue by sliding the window
            window_len = right - left
            if window_len > k:
                prev_max_todo = dp[left]
                left += 1
                if prev_max_todo == mono_dec_deque[0]:
                    mono_dec_deque.popleft()
            
            # Update the answer in dp array
            prev_max_score = mono_dec_deque[0]
            dp[right] = nums[right] + prev_max_score
            
            # Maintain monothonic decreasing dequeue
            while mono_dec_deque and dp[right] > mono_dec_deque[-1]:
                mono_dec_deque.pop()
            mono_dec_deque.append(dp[right])
            
        return dp[-1]