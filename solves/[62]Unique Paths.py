class SolutionV1:
    # 递推的时候初始化
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp.append([1])
                elif i == 0:
                    dp[i].append(1)
                elif j == 0:
                    dp.append([1])
                else:
                    dp[i].append(dp[i - 1][j] + dp[i][j - 1])
        return dp[m - 1][n - 1]


class SolutionV2:
    # 先生成dp数组，再递推
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


class SolutionV3:
    # 压缩dp数组
    # 先生成dp数组，再递推
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for j in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]


class SolutionV4:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for j in range(n)]
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]
