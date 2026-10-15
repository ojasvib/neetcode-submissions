class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for str in strs:
            def encode():
                occ = [0] * 26
                for c in str:
                    occ[ord(c) - ord('a')] += 1
               
                return tuple(occ)
            encodedStr = encode()
            if encodedStr not in hashMap:
                hashMap[encodedStr] = []
            hashMap[encodedStr].append(str)       
        return list(hashMap.values())