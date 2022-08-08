# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode(1453)
        dummy.left = root
        
        self.dfs(dummy, 0, depth - 1, val)
        
        return dummy.left
        
    def dfs(self, current_node, current_dept, wanted_depth, val):
        if current_node == None:
            return
        
        if current_dept == wanted_depth:
            self.add_nodes_with_value(current_node, val)
            return
        
        self.dfs(current_node.left, current_dept + 1, wanted_depth, val)
        self.dfs(current_node.right, current_dept + 1, wanted_depth, val)
    
    def add_nodes_with_value(self, parent_node, val):
        left_subtree = parent_node.left
        right_subtree = parent_node.right
        
        parent_node.left = TreeNode(val)
        parent_node.right = TreeNode(val)
        
        parent_node.left.left = left_subtree
        parent_node.right.right = right_subtree