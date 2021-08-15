# Given a non-empty array of decimal digits representing a non-negative integer,
#  increment one to the integer. 
# 
#  The digits are stored such that the most significant digit is at the head of 
# the list, and each element in the array contains a single digit. 
# 
#  You may assume the integer does not contain any leading zero, except the numb
# er 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#  
# 
#  Example 2: 
# 
#  
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#  
# 
#  Example 3: 
# 
#  
# Input: digits = [0]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  
#  Related Topics Array Math 
#  👍 2706 👎 3513


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for digit in digits:
            result = result * 10 + digit
        result += 1
        return [int(n) for n in str(result)]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.plusOne(
        [1, 2, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5, 6, 9, 1, 2,
         3, 4, 5, 6, 9, 1, 2, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5, 6, 9]))
