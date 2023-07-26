class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        has_smaller_on_left = []
        prev_min = nums[0]
        for num in nums:
            if num > prev_min:
                has_smaller_on_left.append(num)
            prev_min = min(prev_min, num)
        
        # Check if any possible tuple chain found
        if not has_smaller_on_left:
            return False
        
        # Second pass for 3rd element of the increasing sequence
        prev_min = has_smaller_on_left[0]
        for num in has_smaller_on_left:
            if num > prev_min:
                return True
            prev_min = min(prev_min, num)
        
        return False