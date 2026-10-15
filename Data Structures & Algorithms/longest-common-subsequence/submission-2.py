import collections
import bisect

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. text2 ke har character ki positions ko REVERSE order mein store karein
        # Reverse order isliye taaki same character duplicate match na ho sake
        str2map = collections.defaultdict(list)
        for idx, char in enumerate(text2):
            str2map[char].append(idx)
            
        # 2. text1 ke characters ko unki text2 wali indices se map karein
        # Yeh list hume greedy track rakhne mein madad karegi
        mapped_indices = []
        for char in text1:
            if char in str2map:
                # Reverse order mein indices add karein
                mapped_indices.extend(reversed(str2map[char]))
                
        # 3. Mapped indices par Patience Sorting (Greedy LIS) lagayein
        # Yeh step pure greedy hai, har element apni sahi jagah lower_bound se dhoondta hai
        tails = []
        for index in mapped_indices:
            # Python's lower_bound (bisect_left)
            subseq_idx = bisect.bisect_left(tails, index)
            
            # Agar index list ke end mein fit hota hai, naya element add karein
            if subseq_idx == len(tails):
                tails.append(index)
            else:
                # Greedy choice: Choti value se replace karein taaki aage bade numbers aa sakein
                tails[subseq_idx] = index
                
        return len(tails)



# Input: text1 = "cat", text2 = "crabtt" 
# Input: text1 = "czzzzzatalexa", text2 = "crmmmmmmabtalexa" 
# cat
# map str1map<char, set<int>>;
# c->{0}
# a->{1}
# t->{2}
# map str2map<char, set<int>>;
# c->{0}
# r->{1}
# a->{2}
# b->{3}
# t->{4,5}
#             both equal?

# i=0, j =0,  y, len++
# i=1, j =1,  no
# option 1
#     i= fixed, j move to find char at i
#     j = str2map[str[i]].lower_bound(j)
#     j = 2
#     i=1,j=2, len = 2
#     i++, j++
# option 2
#     j = fixed, i move to find char at j
#         i = 3, exit the loop 

#             both equal?
# i=0, j =0,  y
# i=1, j =1,  no
# option 1
#     i= fixed, j move to find char at i
# option 2
#     j = fixed, i move to find char at j
