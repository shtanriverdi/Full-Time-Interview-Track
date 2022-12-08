# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, current, leaves):
        if not current:
            return
        self.helper(current.left, leaves)
        self.helper(current.right, leaves)
        if not current.left and not current.right:
            leaves.append( current.val )
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_A = []
        leaves_B = []
        self.helper(root1, leaves_A)
        self.helper(root2, leaves_B)
        return leaves_A == leaves_B