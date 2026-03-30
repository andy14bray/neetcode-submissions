class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = collections.defaultdict(int)

        for s in s1:
            s1_counts[s] += 1

        s2_counts = collections.defaultdict(int)

        for r in range(len(s2)):
            if r < len(s1):
                s2_counts[s2[r]] += 1
            else:
                s2_counts[s2[r]] += 1
                s2_counts[s2[r - len(s1)]] -= 1
                if s2_counts[s2[r - len(s1)]] == 0:
                    del s2_counts[s2[r - len(s1)]]
            if s1_counts == s2_counts:
                return True
        return False
