class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        incoming_edge_count = defaultdict(int)
        
        for winner, loser in matches:
            incoming_edge_count[winner]
            incoming_edge_count[loser]
        
        for winner, loser in matches:
            incoming_edge_count[loser] += 1
        
        answer = [[], []]
        for node, count in incoming_edge_count.items():
            if count == 0:
                answer[0].append( node )
            if count == 1:
                answer[1].append( node )
        
        answer[0].sort()
        answer[1].sort()
        
        return answer