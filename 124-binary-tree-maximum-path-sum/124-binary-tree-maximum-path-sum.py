# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = [ root.val ]
        self.dfs(root, answer)
        return answer[0]
    
    def dfs(self, current, answer) -> int:
        if current == None:
            return -1001
        
        left_max_path_sum_so_far = self.dfs(current.left, answer)
        right_max_path_sum_so_far = self.dfs(current.right, answer)

        # Calculate the updated max path sum so far
        new_max_path_sum = max(left_max_path_sum_so_far + current.val,
                               right_max_path_sum_so_far + current.val,
                              current.val)
        
        # Update the answer
        answer[0] = max(answer[0], current.val,
                         new_max_path_sum,
                        current.val + left_max_path_sum_so_far + right_max_path_sum_so_far)
        
        return new_max_path_sum
