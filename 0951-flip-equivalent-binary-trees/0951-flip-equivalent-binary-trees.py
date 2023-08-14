# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, cur_A, cur_B):
        if cur_A == None and cur_B == None:
            return True
        
        if cur_A == None or cur_B == None:
            return False
        
        if cur_A.val != cur_B.val:
            return False
        
        # No Flip
        if self.helper(cur_A.left, cur_B.left) and self.helper(cur_A.right, cur_B.right):
            return True
        
        # Flip
        if self.helper(cur_A.right, cur_B.left) and self.helper(cur_A.left, cur_B.right):
            return True
        
        return False
    
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.helper(root1, root2)