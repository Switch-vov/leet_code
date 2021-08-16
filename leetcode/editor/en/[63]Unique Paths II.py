# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  Now consider if some obstacles are added to the grids. How many unique paths 
# would there be? 
# 
#  An obstacle and space is marked as 1 and 0 respectively in the grid. 
# 
#  
#  Example 1: 
# 
#  
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#  
# 
#  Example 2: 
# 
#  
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  m == obstacleGrid.length 
#  n == obstacleGrid[i].length 
#  1 <= m, n <= 100 
#  obstacleGrid[i][j] is 0 or 1. 
#  
#  Related Topics Array Dynamic Programming Matrix 
#  👍 3355 👎 312


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
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


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
