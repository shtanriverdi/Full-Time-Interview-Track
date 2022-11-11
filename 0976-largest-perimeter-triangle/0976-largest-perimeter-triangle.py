class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        a + b > c
        """
        nums.sort(reverse=True)
        length = len(nums)
        for i in range(2, length):
            if nums[i] + nums[i - 1] > nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]
        
        return 0