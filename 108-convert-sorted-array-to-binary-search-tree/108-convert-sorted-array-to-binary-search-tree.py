# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        return self.helper(0, length - 1, nums)
    
    def helper(self, left, right, nums):
        if right < left:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(left, mid - 1, nums)
        node.right = self.helper(mid + 1, right, nums)
        
        return node