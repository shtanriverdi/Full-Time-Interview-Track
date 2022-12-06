# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        evenHead = head.next
        even = head.next
        odd = head
        
        while even and even.next:
            # Rewire the links
            odd.next = odd.next.next
            even.next = even.next.next
            # Move the pointers
            odd = odd.next
            even = even.next

        # Connect odd tail to even head
        odd.next = evenHead
        
        return head
        