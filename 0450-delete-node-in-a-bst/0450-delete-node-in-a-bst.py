# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBiggestNode(self, current_node):
        walk = current_node
        while walk.right:
            walk = walk.right
        return walk
    
    def searchNodeToBeDeleted(self, current_node, parent, key, came_from):
        if current_node == None:
            return [ None, None, 'N' ]
        
        if current_node.val == key:
            return [ parent, current_node, came_from ]
        
        if key > current_node.val:
            return self.searchNodeToBeDeleted(current_node.right, current_node, key, 'R')
    
        return self.searchNodeToBeDeleted(current_node.left, current_node, key, 'L')
        
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy_root = TreeNode(1453)
        dummy_root.right = root
        
        [ parent, node_to_be_deleted, came_from ] = self.searchNodeToBeDeleted(root, dummy_root, key, 'R')
        
        if node_to_be_deleted == None:
            return dummy_root.right
        
        left_subtree_after = node_to_be_deleted.left
        right_subtree_after = node_to_be_deleted.right
        
        if left_subtree_after:
            if came_from == 'R':
                parent.right = left_subtree_after
            else:
                parent.left = left_subtree_after
                
            node_at_lower_right_corner = self.findBiggestNode(left_subtree_after)
            if right_subtree_after:
                node_at_lower_right_corner.right = right_subtree_after
                
        else:
            if came_from == 'R':
                parent.right = right_subtree_after
            else:
                parent.left = right_subtree_after
            
        return dummy_root.right