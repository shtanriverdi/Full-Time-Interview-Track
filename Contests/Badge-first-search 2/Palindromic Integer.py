class Solution:
    def solve(self, num):
        pal = str(num)

        n = len(pal)
        for i in range(n//2):
            if pal[i] != pal[n - i - 1]:
                return False
        return True