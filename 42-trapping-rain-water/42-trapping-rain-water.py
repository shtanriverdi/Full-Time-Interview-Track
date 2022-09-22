class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)

        # Calculate right max
        right_max = [0] * n
        prev_right_max = -inf
        for index in range(n - 1, -1, -1):
            height = heights[index]
            if height > prev_right_max:
                prev_right_max = height
            right_max[index] = prev_right_max
        
        # Calculate left max
        left_max = []
        prev_left_max = -inf
        for height in heights:
            if height > prev_left_max:
                prev_left_max = height
            left_max.append(prev_left_max)
            
        # Calculate the total trapped water
        total_trapped_water = 0
        for i in range(n):
            left_max_bar = left_max[i]
            right_max_bar = right_max[i]
            total_trapped_water += min(left_max_bar, right_max_bar) - heights[i]
            
        return total_trapped_water