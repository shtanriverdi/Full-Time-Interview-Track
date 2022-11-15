# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, cur_node, binary_route, route_index):
        if cur_node == None:
            return False
        
        if route_index == len(binary_route):
            return True
        
        # Go left
        if binary_route[route_index] == '0':
            return self.dfs(cur_node.left, binary_route, route_index + 1)
        
        # Go right
        else:
            return self.dfs(cur_node.right, binary_route, route_index + 1)
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        walk = root
        level_count = 0
        while walk and walk.left:
            level_count += 1
            walk = walk.left
            
        left = 0
        right = (2**level_count) - 1
        while left <= right:
            mid = (left + right) // 2
            binary = format(mid, 'b')
            necessary_zeros = level_count - len(binary)
            binary_route = ("0"*necessary_zeros) + binary
            hasLeafFound = self.dfs(root, binary_route, 0)
            if hasLeafFound:
                left = mid + 1
            else:
                right = mid - 1
        
        # Right pointer points to the leaf at the right most place in the last level
        total_node_count_except_last_level = 2**level_count - 1
        last_level_node_count = right + 1 if right >= 0 else 1
        
        return total_node_count_except_last_level + last_level_node_count
            