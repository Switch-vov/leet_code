# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can yo
# u climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics Math Dynamic Programming Memoization 
#  👍 7592 👎 230


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    cache = defaultdict()

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            self.cache[n] = n
            return n
        left = right = 0
        if self.cache.get(n - 1):
            left = self.cache.get(n - 1)
        else:
            self.cache[n - 1] = left = self.climbStairs(n - 1)
        if self.cache.get(n - 2):
            right = self.cache.get(n - 2)
        else:
            self.cache[n - 2] = right = self.climbStairs(n - 2)
        return left + right


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))
    print(solution.climbStairs(45))
