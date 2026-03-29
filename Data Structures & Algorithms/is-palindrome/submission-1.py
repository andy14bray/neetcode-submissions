class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for l in s:
            if l.isalnum():
                new_s.append(l.lower())
        l = 0
        r = len(new_s) - 1
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True