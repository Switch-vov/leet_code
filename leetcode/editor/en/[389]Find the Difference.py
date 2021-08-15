# You are given two strings s and t. 
# 
#  String t is generated by random shuffling string s and then add one more lett
# er at a random position. 
# 
#  Return the letter that was added to t. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "", t = "y"
# Output: "y"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a", t = "aa"
# Output: "a"
#  
# 
#  Example 4: 
# 
#  
# Input: s = "ae", t = "aea"
# Output: "a"
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 1000 
#  t.length == s.length + 1 
#  s and t consist of lower-case English letters. 
#  
#  Related Topics Hash Table String Bit Manipulation Sorting 
#  👍 1467 👎 325


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        mapping = defaultdict()
        for c in s:
            c_count = mapping.get(c)
            if not c_count:
                c_count = 0
            c_count += 1
            mapping[c] = c_count
        results = ''
        for c in t:
            c_count = mapping.get(c)
            if not c_count:
                results += c
                continue
            c_count -= 1
            mapping[c] = c_count
        return results


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.findTheDifference('abcd', 'abcde'))
    print(solution.findTheDifference('', 'y'))
    print(solution.findTheDifference('a', 'aa'))
    print(solution.findTheDifference('ae', 'aea'))
    print(solution.findTheDifference('', 'aeaasddsada'))
    print(solution.findTheDifference('aaabbbcc', 'aaaabbbbcccc'))
