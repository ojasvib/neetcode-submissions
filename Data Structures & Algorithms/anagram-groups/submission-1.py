class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedToStrings = {}
        
        for word in strs:
            occ = [0]*26
            for c in word:
                occ[ord(c) - ord('a')] += 1
            occStr = ""
            for i in range(26):
                occStr += str(occ[i]) + "#"
            # If the key is missing, create an empty list first
            if occStr not in sortedToStrings:
                sortedToStrings[occStr] = []
            sortedToStrings[occStr].append(word)
        return list(sortedToStrings.values())
