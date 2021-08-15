# Given n pairs of parentheses, write a function to generate all combinations of
#  well-formed parentheses. 
# 
#  
#  Example 1: 
#  Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#  Example 2: 
#  Input: n = 1
# Output: ["()"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics String Dynamic Programming Backtracking 
#  👍 9161 👎 362


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.backtrack(results, '', n, n)
        return results

    def backtrack(self, results: List[str], result: str, left: int, right: int):
        if not left and not right:
            results.append(result)
            return
        if left > right:
            return
        if left > 0:
            self.backtrack(results, result + '(', left - 1, right)
        if right > 0:
            self.backtrack(results, result + ')', left, right - 1)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.generateParenthesis(3))
