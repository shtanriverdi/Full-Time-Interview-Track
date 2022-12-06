class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        edge_scores = defaultdict(int)
        for source, destination in enumerate(edges):
            edge_scores[destination] += source
            
        best_edge_score_node = -1
        best_edge_score = -1
        for ith_node, _ in enumerate(edges):
            if edge_scores[ith_node] > best_edge_score:
                best_edge_score = edge_scores[ith_node]
                best_edge_score_node = ith_node
            
        return best_edge_score_node