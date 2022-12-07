# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, cur, low, high, total_sum):
        if cur == None:
            return
        
        if low <= cur.val and cur.val <= high:
            total_sum[0] += cur.val
            self.helper(cur.right, low, high, total_sum)
            self.helper(cur.left, low, high, total_sum)
        
        # cur.val < low <= X <= high, go to right
        elif cur.val < low:
            self.helper(cur.right, low, high, total_sum)
            
        # low <= X <= high < cur.val, go to left
        elif high < cur.val:
            self.helper(cur.left, low, high, total_sum)
            
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total_sum = [0]
        self.helper(root, low, high, total_sum)
        return total_sum[0]