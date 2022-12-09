# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, cur, answer):
        # Leaf node
        if cur and cur.left == None and cur.right == None:
            return [ cur.val, cur.val ]
        
        min_value = cur.val
        max_value = cur.val
        
        if cur.left:
            left_min_val, left_max_val = self.helper(cur.left, answer)
            answer[0] = max(answer[0], abs(left_max_val - cur.val))
            answer[0] = max(answer[0], abs(left_min_val - cur.val))
            min_value = min(left_max_val, left_min_val, min_value)
            max_value = max(left_max_val, left_min_val, max_value)
        
        if cur.right:
            right_min_val, right_max_val = self.helper(cur.right, answer)
            answer[0] = max(answer[0], abs(right_max_val - cur.val))
            answer[0] = max(answer[0], abs(right_min_val - cur.val))
            min_value = min(right_max_val, right_min_val, min_value)
            max_value = max(right_max_val, right_min_val, max_value)
        
        return [ min_value, max_value ]
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        self.helper(root, answer)
        return answer[0]