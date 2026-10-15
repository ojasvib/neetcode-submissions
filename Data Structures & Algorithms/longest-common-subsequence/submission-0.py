import collections
import bisect

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. text2 ke har character ki saari positions ka map banayein
        # Yeh automatic sorted hota hai kyunki hum sequential loop chala rahe hain
        str2map = collections.defaultdict(list)
        for idx, char in enumerate(text2):
            str2map[char].append(idx)
            
        # Memoization table taaki repeat hone wale states dubara calculate na ho
        memo = {}

        # 2. Greedy recursive function jo best path chunega
        def match_greedy(i, j_bound):
            # Agar text1 khatam ho jaye, toh subsequence ki length 0 hogi
            if i == len(text1):
                return 0
                
            # Agar yeh state pehle se calculated hai, toh wahi return karein
            if (i, j_bound) in memo:
                return memo[(i, j_bound)]
                
            char = text1[i]
            
            # --- Option 1: Is character ko skip kar dein (Greedy Choice A) ---
            option_skip = match_greedy(i + 1, j_bound)
            
            # --- Option 2: Is character ko match karein (Greedy Choice B) ---
            option_match = 0
            if char in str2map:
                # Python ka lower_bound (bisect_right/left) use karke 
                # text2 mein j_bound ke baad ka sabse pehla index dhoondhein
                pos_list = str2map[char]
                idx = bisect.bisect_left(pos_list, j_bound)
                
                # Agar valid index mil jata hai text2 ke andar
                if idx < len(pos_list):
                    next_j_index = pos_list[idx]
                    # Subsequence ki length +1 karein aur agla match dhoondhein
                    option_match = 1 + match_greedy(i + 1, next_j_index + 1)
            
            # Dono greedy options mein se jo BEST (maximum) hai usse chunein
            memo[(i, j_bound)] = max(option_skip, option_match)
            return memo[(i, j_bound)]

        # j_bound = 0 ka matlab hum text2 ke shuruat se check kar rahe hain
        return match_greedy(0, 0)


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
