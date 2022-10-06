class Solution:
    def solve(self, relations):
        follower_map = defaultdict(set)
        uniqs = set()
        for a, b in relations:
            if a in follower_map[b]:
                uniqs.add(a)
                uniqs.add(b)
            follower_map[a].add(b)

        answer = list(uniqs)
        answer.sort()
        return answer
