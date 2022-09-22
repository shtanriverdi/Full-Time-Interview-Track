class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        
        prev_right_max = -inf
        prev_left_max = -inf
        
        left_index = 0
        right_index = n - 1
        
        total_trapped_water = 0

        while left_index < right_index:
            # Update the previous left and right max bars
            prev_right_max = max(prev_right_max, heights[right_index])
            prev_left_max = max(prev_left_max, heights[left_index])
            current_min_bar = min(prev_right_max, prev_left_max)
            
            # Calculate contribution for right bar
            right_bar = heights[right_index]
            possible_right_contribution = current_min_bar - right_bar
            if possible_right_contribution > 0:
                total_trapped_water += possible_right_contribution
            
            # Calculate contribution for left bar
            left_bar = heights[left_index]
            possible_left_contribution = current_min_bar - left_bar
            if possible_left_contribution > 0:
                total_trapped_water += possible_left_contribution
            
            # Update the pointers
            if right_bar <= left_bar:
                right_index -= 1
            else:
                left_index += 1
            
        return total_trapped_water