class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = 1
        length = len(nums)
        while right_pointer < length:
            if nums[left_pointer] == nums[right_pointer]:
                right_pointer += 1
            else:
                nums[left_pointer + 1] = nums[right_pointer]
                left_pointer += 1
        
        return left_pointer + 1