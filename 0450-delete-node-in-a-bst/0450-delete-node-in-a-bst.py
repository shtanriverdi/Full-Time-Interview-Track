# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSuccessor(self, root):
        walk = root.right
        if walk == None:
            return None
        
        while walk.left:
            walk = walk.left
            
        return walk
            
    def findPredecessor(self, root):
        walk = root.left
        if walk == None:
            return None
        
        while walk.right:
            walk = walk.right
            
        return walk
    
    def findAndDeleteNodeHelper(self, current, key):
        if current == None:
            return None
        
        if key < current.val:
            current.left = self.findAndDeleteNodeHelper(current.left, key)
        elif key > current.val:
            current.right = self.findAndDeleteNodeHelper(current.right, key)
        else:
            successor = self.findSuccessor(current)
            predecessor = self.findPredecessor(current) # TODO - Optimize
            if successor:
                current.val = successor.val
                current.right = self.findAndDeleteNodeHelper(current.right, successor.val)
            elif predecessor:
                current.val = predecessor.val
                current.left = self.findAndDeleteNodeHelper(current.left, predecessor.val)
            else:
                return None
                
        return current
                
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.findAndDeleteNodeHelper(root, key)