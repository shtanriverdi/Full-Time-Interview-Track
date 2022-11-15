# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node
        dummy_node = ListNode(1453)
        dummy_node.next = head
        
        # Place pointers
        cur = head
        prev = dummy_node
        
        # Find the node at index left - 1
        count = 1
        while cur and count < left:
            prev = cur
            cur = cur.next
            count += 1
            
        nextt = cur
        
        to_be_linked_to_reversed_head = prev
        to_be_linked_to_right_next = cur
            
        while left <= right and cur:
            # Update next
            nextt = nextt.next
            # Reverse
            cur.next = prev
            # Advance prev and cur
            prev = cur
            cur = nextt
            left += 1

        to_be_linked_to_right_next.next = nextt
        to_be_linked_to_reversed_head.next = prev
        
        return dummy_node.next