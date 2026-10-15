class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occ = [0] * 26
        for c in s:
            occ[ord(c) - ord('a')] += 1
        for c in t:
            occ[ord(c) - ord('a')] -= 1
        for n in occ:
            if n != 0:
                return False
        return True