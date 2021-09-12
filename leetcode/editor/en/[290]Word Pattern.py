# Given a pattern and a string s, find if s follows the same pattern. 
# 
#  Here follow means a full match, such that there is a bijection between a lett
# er in pattern and a non-empty word in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= pattern.length <= 300 
#  pattern contains only lower-case English letters. 
#  1 <= s.length <= 3000 
#  s contains only lower-case English letters and spaces ' '. 
#  s does not contain any leading or trailing spaces. 
#  All the words in s are separated by a single space. 
#  
#  Related Topics Hash Table String 
#  👍 2108 👎 241


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s, t = pattern, s.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.wordPattern(pattern="abba", s="dog cat cat dog"))
    print(solution.wordPattern(pattern="abba", s="dog cat cat fish"))
    print(solution.wordPattern(pattern="aaaa", s="dog dog dog dog"))
    print(solution.wordPattern(pattern="a", s="dog ads"))
    print(solution.wordPattern(pattern="aba", s="dog cat cat"))
