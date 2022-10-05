# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        newRoot = TreeNode(1453)
        newRoot.left = root
        self.dfs(newRoot, depth - 1, val)
        return newRoot.left
        
    def dfs(self, current, depth, val_to_add):
        if current == None:
            return
        
        if depth == 0:
            left_subtree = current.left
            right_subtree = current.right
            
            current.left = TreeNode(val_to_add)
            current.left.left = left_subtree
            
            current.right = TreeNode(val_to_add)
            current.right.right = right_subtree
            return
        
        self.dfs(current.left, depth - 1, val_to_add)
        self.dfs(current.right, depth - 1, val_to_add)