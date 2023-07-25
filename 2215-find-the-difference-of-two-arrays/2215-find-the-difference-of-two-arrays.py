class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        
        A = set(nums1)
        B = set(nums2)
        
        answer[0] = list(A.difference(B))
        answer[1] = list(B.difference(A))
        
        return answer