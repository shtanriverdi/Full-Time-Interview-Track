class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        changed = [False] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                changed[i] = True
                
        # print(candies)
        # print(changed)      
        
        for i in reversed(range(n - 1)):
            if (ratings[i] > ratings[i + 1] and changed[i] == False) or (ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]):
                candies[i] = candies[i + 1] + 1
                        
        # print(candies)
        # print(changed)
        
        return sum(candies)