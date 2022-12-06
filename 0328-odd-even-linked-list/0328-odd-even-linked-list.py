# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def moveEvensToBack(self, start, end):
        cur = start.next
        while cur and cur != end:
            # Swap
            cur.val, end.val = end.val, cur.val
            cur = cur.next
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        slow = head.next
        fast = slow.next if slow else None
        
        while slow and fast:
            # Swap
            slow.val, fast.val = fast.val, slow.val
            # Preserve the ordering of evens
            self.moveEvensToBack(slow, fast)
            slow = slow.next
            fast = fast.next.next if fast.next else None
            
        return head