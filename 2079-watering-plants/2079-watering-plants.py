class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps_taken = 0
        cur_cap = capacity
        for index, need in enumerate(plants):
            if cur_cap >= need:
                cur_cap -= need
                steps_taken += 1
            else:
                cur_cap = capacity - need
                steps_taken += (2*(index + 1)) - 1
            
        return steps_taken