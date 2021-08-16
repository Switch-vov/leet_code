from typing import List


class SolutionV1:
    # 递推
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and dp[i][j - 1] == 0:
                    dp[i][j] = 0
                elif j == 0 and dp[i - 1][j] == 0:
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]


class SolutionV2:
    # 压缩dp数组
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0 for j in range(m)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif i == 0 and j == 0:
                    dp[j] = 1
                elif i == 0 and dp[j - 1] == 0:
                    dp[j] = 0
                elif j == 0 and dp[j] == 0:
                    dp[j] = 0
                elif i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[m - 1]
