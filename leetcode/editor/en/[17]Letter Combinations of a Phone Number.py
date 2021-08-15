# Given a string containing digits from 2-9 inclusive, return all possible lette
# r combinations that the number could represent. Return the answer in any order. 
# 
# 
#  A mapping of digit to letters (just like on the telephone buttons) is given b
# elow. Note that 1 does not map to any letters. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  Example 2: 
# 
#  
# Input: digits = ""
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: digits = "2"
# Output: ["a","b","c"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] is a digit in the range ['2', '9']. 
#  
#  Related Topics Hash Table String Backtracking 
#  👍 7019 👎 560


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dial_pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        results = []
        self.dfs(results, '', 0, digits, dial_pad)
        return results

    def dfs(self, results: List[str], result: str, level: int, digits: str, dial_pad: dict):
        if level == len(digits):
            results.append(result)
            return
        digit = digits[level]
        letters = dial_pad.get(digit)
        for letter in letters:
            self.dfs(results, result + letter, level + 1, digits, dial_pad)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.letterCombinations(''))
    print(solution.letterCombinations('2'))
    print(solution.letterCombinations('23'))
