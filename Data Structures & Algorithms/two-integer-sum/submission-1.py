class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, n in enumerate(nums):
            visited[n] = i
        for i, n in enumerate(nums):
            if target - n in visited and visited[target - n] != i:
                return [i, visited[target - n]]
            