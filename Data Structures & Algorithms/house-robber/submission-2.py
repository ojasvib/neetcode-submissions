class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def robRec(index):
            if(index >= len(nums)):
                return 0
            if cache[index] != -1:
                return cache[index]
            cache[index] = max(nums[index] + robRec(index + 2), robRec(index + 1))    
            return cache[index]
        return robRec(0)
