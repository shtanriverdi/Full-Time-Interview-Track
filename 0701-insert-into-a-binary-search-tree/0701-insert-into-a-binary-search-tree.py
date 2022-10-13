# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertHelper(self, current_node, val_to_insert):
        if current_node == None:
            return TreeNode(val_to_insert)
        
        if val_to_insert > current_node.val:
            current_node.right = self.insertHelper(current_node.right, val_to_insert)
        else:
            current_node.left = self.insertHelper(current_node.left, val_to_insert)
        
        return current_node
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.insertHelper(root, val)