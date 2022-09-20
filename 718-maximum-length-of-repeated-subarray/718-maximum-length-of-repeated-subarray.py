class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1) + 1
        n = len(nums2) + 1
        dp = [ [0] * n for _ in range(m) ]

        answer = 0
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    answer = max(answer, dp[i][j])

        return answer