import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        
        seconds = 0
        while amount[0] != 0:
            if amount[0] > 0:
                amount[0] -= 1
            if amount[1] > 0:
                amount[1] -= 1
            
            seconds += 1
            amount.sort(reverse=True)
        
        return seconds