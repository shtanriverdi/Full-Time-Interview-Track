class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        if n < 4:
            return False

        memo = {}
        
        groups = [0] * 4
        group_sum = sum(matchsticks) // 4
        
        # To optimize recursion
        matchsticks.sort(reverse=True)
        
        return self.helper(0, n, matchsticks, groups, group_sum, memo)
    
    def helper(self, index, n, matchsticks, groups, group_sum, memo):
        if index == n and groups[0] == groups[1] and groups[1] == groups[2] and groups[2] == groups[3]:
            return True
        
        if (index, groups[0], groups[1], groups[2], groups[3]) in memo:
            return memo[(index, groups[0], groups[1], groups[2], groups[3])]
        
        answer = False
        for group_index in range(4):
            # Assign current matchstick to current group
            next_group_sum = groups[group_index] + matchsticks[index]
            if next_group_sum > group_sum:
                continue
            groups[group_index] = next_group_sum
            
            # Recursively call next step
            has_square_found = self.helper(index + 1, n, matchsticks, groups, group_sum, memo)
            
            # Reassign/Backtrack current matchstick from the recent group
            groups[group_index] -= matchsticks[index]
            
            # Early termination, no need to continue if we've already found the answer True
            if has_square_found:
                answer = True
                break
            
        memo[(index, groups[0], groups[1], groups[2], groups[3])] = answer
        return answer
    