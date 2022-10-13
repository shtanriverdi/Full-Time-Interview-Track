# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, current_node, target):
        if current_node == None:
            return float("-inf")

        possible_found_left = self.helper(current_node.left, target)
        if possible_found_left > target:
            return possible_found_left

        if current_node.val > target:
            return current_node.val

        possible_found_right = self.helper(current_node.right, target)
        if possible_found_right > target:
            return possible_found_right
        
        return float("-inf")

    def solve(self, root, t):
        return self.helper(root, t)