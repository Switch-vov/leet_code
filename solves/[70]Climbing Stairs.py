from collections import defaultdict


class SolutionV1:
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


"""
变种问题:
1. 可以走1,2,3步
2. 不能连续走相同的步数
3. 求走到第n阶，有多少种走法
"""


class SolutionVX:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1
        dp = [[0, 0, 0] for i in range(n + 1)]
        for i in range(3):
            dp[0][i] = 0
            dp[3][i] = 1
        dp[1][0] = dp[2][1] = 1
        for i in range(4, n + 1):
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2]
            dp[i][1] = dp[i - 2][0] + dp[i - 2][2]
            dp[i][2] = dp[i - 3][0] + dp[i - 3][1]
        return dp[n][0] + dp[n][1] + dp[n][2]


if __name__ == '__main__':
    solution = SolutionVX()
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))
    print(solution.climbStairs(6))
    print(solution.climbStairs(7))
    print(solution.climbStairs(8))
    print(solution.climbStairs(9))
    print(solution.climbStairs(10))
    print(solution.climbStairs(15))
    print(solution.climbStairs(20))
    print(solution.climbStairs(45))
    print(solution.climbStairs(50))
