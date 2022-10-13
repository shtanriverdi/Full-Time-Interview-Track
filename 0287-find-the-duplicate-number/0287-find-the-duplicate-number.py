class Solution:
    def findLessThanOrEqualToCount(self, nums, pivot_num):
        count = 0
        for num in nums:
            if num <= pivot_num:
                count += 1
        return count
    
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n
        
        while left < right:
            mid = (left + right) // 2
            real_count = mid
            count_found = self.findLessThanOrEqualToCount(nums, mid)
            if count_found <= real_count:
                left = mid + 1
            else:
                right = mid
                
        return right