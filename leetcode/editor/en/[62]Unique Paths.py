# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  How many possible unique paths are there? 
# 
#  
#  Example 1: 
# 
#  
# Input: m = 3, n = 7
# Output: 28
#  
# 
#  Example 2: 
# 
#  
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-righ
# t corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#  
# 
#  Example 3: 
# 
#  
# Input: m = 7, n = 3
# Output: 28
#  
# 
#  Example 4: 
# 
#  
# Input: m = 3, n = 3
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 100 
#  It's guaranteed that the answer will be less than or equal to 2 * 109. 
#  
#  Related Topics Math Dynamic Programming Combinatorics 
#  👍 6040 👎 255


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for j in range(n)]
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.uniquePaths(3, 2))
