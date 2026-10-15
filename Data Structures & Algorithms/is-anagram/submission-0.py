class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occs = [0] * 26
        occt = [0] * 26
        
        for c in s:
            occs[ ord(c) - ord('a')] += 1
        for c in t:
            occt[ ord(c) - ord('a')] += 1

        for i in range(26):
            if occs[i] != occt[i]:
                return False
        return True 