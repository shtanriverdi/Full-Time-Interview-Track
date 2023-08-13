# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isCriticalPoint(self, prev, cur, nextt):
        if (cur.val < prev.val and cur.val < nextt.val) or (cur.val > prev.val and cur.val > nextt.val):
            return True
        return False
    
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        cur = head.next
        cur_index = 1

        left_most_cp_index = float("inf")
        right_most_cp_index = float("-inf")

        prev_cp_index = float("-inf")
        min_dist = float("inf")
        
        while cur.next:
            isCriticalPoint = self.isCriticalPoint(prev, cur, cur.next)
            # Critical point found
            if isCriticalPoint:
                left_most_cp_index = min(left_most_cp_index, cur_index)
                right_most_cp_index = max(right_most_cp_index, cur_index)
                min_dist = min(min_dist, cur_index - prev_cp_index)
                prev_cp_index = cur_index
                
            # Update pointers
            prev = cur
            cur = cur.next
            cur_index += 1
        
        # Calculate the longest distance
        max_dist = right_most_cp_index - left_most_cp_index
        
        # Edge case, if no cpoints or only one
        if min_dist == inf:
            return [-1, -1]
            
        return [min_dist, max_dist]