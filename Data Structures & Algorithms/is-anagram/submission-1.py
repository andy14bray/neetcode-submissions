class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        for l in s:
            if l in s_counts:
                s_counts[l] += 1
            else:
                s_counts[l] = 1

        for l in t:
            if l in s_counts:
                s_counts[l] -= 1
            else:
                return False

        for k, v in s_counts.items():
            if v != 0:
                return False
        return True