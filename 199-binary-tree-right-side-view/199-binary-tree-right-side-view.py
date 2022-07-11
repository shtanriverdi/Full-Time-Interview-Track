# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return result
        
        todo = deque([root])
        while todo:
            nodes_count_at_current_level = len(todo)
            last_processed_node = None
            for _ in range(nodes_count_at_current_level):
                cur = todo.popleft()
                last_processed_node = cur.val
                if cur.left:
                    todo.append(cur.left)
                if cur.right:
                    todo.append(cur.right)
                    
            if last_processed_node != None:
                result.append(last_processed_node)
        
        return result