# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, current_node, wanted):
        if current_node == None:
            return 
        
        if wanted == current_node.val:
            return current_node
        
        if wanted > current_node.val:
            return self.helper(current_node.right, wanted)
        
        return self.helper(current_node.left, wanted)
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.helper(root, val)