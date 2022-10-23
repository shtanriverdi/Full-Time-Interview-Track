class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        counts = [0] * (n + 1)
        for num in nums:
            counts[num] += 1
        
        duplicate_number = -1
        missing_number = -1
        
        for num in range(1, n + 1):
            if counts[num] == 0:
                missing_number = num
            if counts[num] == 2:
                duplicate_number = num
            
        return [duplicate_number, missing_number]