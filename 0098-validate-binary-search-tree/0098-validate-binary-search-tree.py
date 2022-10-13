# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidHelper(self, current, lower_bound, upper_bound):
        if current == None:
            return True
        
        if not (lower_bound < current.val < upper_bound):
            return False
        
        left_answer = self.isValidHelper(current.left, lower_bound, current.val)
        right_answer = self.isValidHelper(current.right, current.val, upper_bound)
        
        return left_answer and right_answer
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidHelper(root, float("-inf"), float("inf"))
        