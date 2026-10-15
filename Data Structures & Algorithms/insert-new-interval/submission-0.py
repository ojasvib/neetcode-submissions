class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        isInserted = False
        for x, y in intervals:
            if newInterval[0] <= x:
                ans.append(newInterval)
                isInserted = True
            ans.append([x,y])
        if not isInserted:
            ans.append(newInterval)

        merged = []

        for interval in ans:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged





