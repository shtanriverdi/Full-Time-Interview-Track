class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = int(25*1e6)
        answer = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            valid_capacity = self.is_possible(mid, weights, days)
            if valid_capacity:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return answer
        
    def is_possible(self, capacity, weights, days):
        total_days = 1
        total_weight = 0
        for weight in weights:
            if weight > capacity:
                return False
            total_weight += weight
            if total_weight > capacity:
                total_weight = weight
                total_days += 1
            if total_days > days:
                return False
            
        return True