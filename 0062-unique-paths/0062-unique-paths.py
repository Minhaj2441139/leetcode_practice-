class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = number of ways to reach cell (i,j)
        dp = [[0]*n for _ in range(m)]
        
        # base cases: only one way along the top row and left column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # fill in the rest
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
