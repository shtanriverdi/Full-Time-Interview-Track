from sortedcontainers import SortedSet
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], index_diff: int, k: int) -> bool:
        window_set = SortedSet()
        for index, b in enumerate(nums):
            if index > index_diff:
                window_set.discard(nums[index - index_diff - 1])
            # a - b <= k  -->  a <= b + k
            # a - b >= -k -->  a >= b - k
            # lower_value <= a <= upper_value
            lower_a = b - k
            lower_index = window_set.bisect_left(lower_a)
            
            upper_a = b + k
            upper_index = window_set.bisect_right(upper_a)
            if lower_index != upper_index:
                return True
            
            # Add the current number into set
            window_set.add(nums[index])

        return False