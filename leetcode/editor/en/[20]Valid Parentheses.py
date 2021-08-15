# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: s = "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: s = "{[]}"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 104 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 
#  👍 8448 👎 340


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        result = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                result.append(c)
                continue
            if not result:
                return False
            r_c = result.pop()
            if c == ')' and r_c != '(':
                return False
            if c == ']' and r_c != '[':
                return False
            if c == '}' and r_c != '{':
                return False
        return len(result) == 0


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.isValid('()[]{}'))
    print(solution.isValid('(]'))
    print(solution.isValid('([)]'))
    print(solution.isValid('{[]}'))
    print(solution.isValid('{[]}{}{}'))
    print(solution.isValid(''))
    print(solution.isValid('{'))
    print(solution.isValid(']'))
