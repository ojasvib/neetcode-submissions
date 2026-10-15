class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) +1 )] for i in range(2) ]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[0][j] = 1 + dp[1][j + 1]
                else:
                    dp[0][j] = max(dp[0][j+1], dp[1][j])
            dp[1] = dp[0][:]

        return dp[0][0]