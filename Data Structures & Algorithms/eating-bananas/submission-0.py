class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lower_bound = 1
        def calTime(k):
            hrs = 0
            for num in piles:
                hrs += num // k     
                if num % k != 0:
                    hrs += 1
            return hrs
        ans = 10e9 + 1
        while lower_bound <= upper_bound:
            m = (lower_bound + upper_bound) // 2
            if calTime(m) > h:
                lower_bound  = m+1
            else:
                upper_bound = m - 1
                ans = min(m, ans)
        return ans
        