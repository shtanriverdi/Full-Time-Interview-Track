class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        
        alice = 0
        bob = n - 1
        
        alicesCan = capacityA
        bobsCan = capacityB
        
        answer = 0        
        while alice < bob:
            # Alice
            if alicesCan >= plants[alice]:
                alicesCan -= plants[alice]
            else:
                alicesCan = capacityA - plants[alice]
                answer += 1
            # Bob
            if bobsCan >= plants[bob]:
                bobsCan -= plants[bob]
            else:
                bobsCan = capacityB - plants[bob]
                answer += 1
            alice += 1
            bob -= 1
            
        if n % 2 == 1:
            # Alice
            if max(alicesCan, bobsCan) < plants[alice]:
                answer += 1
            
        return answer