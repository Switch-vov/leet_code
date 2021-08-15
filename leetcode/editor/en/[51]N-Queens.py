# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return all distinct solutions to the n-queens puzzle. You
#  may return the answer in any order. 
# 
#  Each solution contains a distinct board configuration of the n-queens' placem
# ent, where 'Q' and '.' both indicate a queen and an empty space, respectively. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as show
# n above
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [["Q"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics Array Backtracking 
#  👍 3867 👎 119


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        self.dfs(results, [], set(), set(), set(), n)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in result] for result in results]

    def dfs(self, results: List[List[int]], result: List[int], col: Set[int], pie: Set[int], na: Set[int], n: int):
        r = len(result)
        if r == n:
            results.append(result.copy())
            return
        for c in range(n):
            if c not in col and c + r not in pie and c - r not in na:
                result.append(c), col.add(c), pie.add(c + r), na.add(c - r)
                self.dfs(results, result, col, pie, na, n)
                result.pop(), col.remove(c), pie.remove(c + r), na.remove(c - r)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.solveNQueens(4))
    print(solution.solveNQueens(8))
