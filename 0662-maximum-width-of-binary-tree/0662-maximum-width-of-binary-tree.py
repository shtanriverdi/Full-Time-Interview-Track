# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, cur, level, nth, level_map):
        if cur == None:
            return
        
        if level not in level_map:
            level_map[level] = [float("inf"), float("-inf")]
        
        # Update min/left most node value
        level_map[level][0] = min(level_map[level][0], nth)
            
        # Update max/right most node value
        level_map[level][1] = max(level_map[level][1], nth)
    
        self.dfs(cur.left, level + 1, (nth * 2) - 1, level_map)
        self.dfs(cur.right, level + 1, nth * 2, level_map)
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level_map = dict()
        self.dfs(root, 0, 1, level_map)
        
        answer = 1
        for left, right in level_map.values():
            answer = max(answer, right - left + 1)
            
        return answer