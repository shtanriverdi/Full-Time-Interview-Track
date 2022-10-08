class Solution:
    def dfs(self, n, patterns, real_n):
        if n == 0:
            return [""]

        if n == 1:
            return ["0", "1", "8"]

        prev_ups = self.dfs(n - 2, patterns, real_n)

        new_list = []
        j = 0
        if n == real_n: 
            j = 1

        for i in range(j, len(patterns)):
            start, end = patterns[i]
            for up in prev_ups:
                new_list.append(start + up + end)

        return new_list

    def solve(self, n):
        if n == 0:
            return []
        patterns = [ ("0","0"), ("1","1"), ("6","9"), ("8","8"), ("9","6") ]
        answer = self.dfs(n, patterns, n)
        return answer