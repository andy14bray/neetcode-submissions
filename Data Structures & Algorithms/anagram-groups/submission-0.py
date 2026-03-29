class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_anagrams = defaultdict(list)
        for string in strs:
            counts = [0] * 26
            for l in string:
                counts[ord(l) - ord('a')] += 1
            seen_anagrams[tuple(counts)].append(string)
        return list(seen_anagrams.values())