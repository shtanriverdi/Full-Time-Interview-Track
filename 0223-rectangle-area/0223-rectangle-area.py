class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area_1 = (C - A) * (D - B)
        area_2 = (G - E) * (H - F)
        total_area = area_1 + area_2
        
        if C <= E or B >= H or D <= F or A >= G:
            return total_area
        
        overlapping_area = (abs(max(A, E) - min(C, G))) * (abs(max(B, F) - min(D, H)))
        return total_area - overlapping_area