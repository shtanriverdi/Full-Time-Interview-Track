# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = self.dfs(root)
        return answer[0]
    
    def dfs(self, current) -> int:
        if current == None:
            return [-inf, -inf]
        
        left_answer, left_max_path_sum_so_far = self.dfs(current.left)
        right_answer, right_max_path_sum_so_far = self.dfs(current.right)
        
        # Calculate the new updated answer
        new_answer = max(left_answer, current.val, right_answer,
                         current.val + left_max_path_sum_so_far,
                        current.val + right_max_path_sum_so_far,
                        current.val + left_max_path_sum_so_far + right_max_path_sum_so_far)
        
        # Calculate the updated max path sum so far
        new_max_path_sum = max(left_max_path_sum_so_far + current.val,
                               right_max_path_sum_so_far + current.val,
                              current.val)
        
        return [new_answer, new_max_path_sum]
