# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        self.dfs(root, 0, targetSum, [], paths)
        return paths
        
    def dfs(self, current, sum_so_far, targetSum, path, paths):
        if current == None:
            return
        
        path.append(current.val)
        sum_so_far += current.val
        
        if not current.left and not current.right and sum_so_far == targetSum:
            paths.append(path.copy())
        
        self.dfs(current.left, sum_so_far, targetSum, path, paths)
        self.dfs(current.right, sum_so_far, targetSum, path, paths)
        
        path.pop()