class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda b: -b[1])
        
        total_amount = 0
        for box, amount in boxTypes:
            if truckSize:
                boxes_to_take = min(truckSize, box)
                truckSize -= boxes_to_take
                total_amount += boxes_to_take * amount
            
        return total_amount