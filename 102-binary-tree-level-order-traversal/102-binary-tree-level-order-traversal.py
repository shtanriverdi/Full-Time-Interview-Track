# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root == None:
            return result
        
        todo = deque([root])
        while todo:
            nodes_count_at_cur_level = len(todo)
            nodes_at_cur_level = []
            for _ in range(nodes_count_at_cur_level):
                cur = todo.popleft()
                nodes_at_cur_level.append(cur.val)
                if cur.left:
                    todo.append(cur.left)
                if cur.right:
                    todo.append(cur.right)
            result.append(nodes_at_cur_level)
            
        return result