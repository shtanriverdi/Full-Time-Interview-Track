# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for index, cur_list in enumerate(lists):
            if cur_list:
                heappush(min_heap, (cur_list.val, index, cur_list))
        
        new_list = ListNode(1453)
        walk = new_list
        while min_heap:
            min_val, index, cur_list = heappop(min_heap)
            walk.next = ListNode(min_val)
            walk = walk.next
            cur_list = cur_list.next
            if cur_list:
                heappush(min_heap, (cur_list.val, index, cur_list))
            
        return new_list.next