class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        mono_inc_stack = []
        length = len(nums)
        for index, num in enumerate(nums):
            remaining = length - index
            while mono_inc_stack and num < mono_inc_stack[-1] and remaining > (k - len(mono_inc_stack)):
                mono_inc_stack.pop()
            mono_inc_stack.append(num)

        return mono_inc_stack[:k]