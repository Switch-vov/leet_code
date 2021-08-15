# Given a non-negative integer x, compute and return the square root of x. 
# 
#  Since the return type is an integer, the decimal digits are truncated, and on
# ly the integer part of the result is returned. 
# 
#  Note: You are not allowed to use any built-in exponent function or operator, 
# such as pow(x, 0.5) or x ** 0.5. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is
#  truncated, 2 is returned. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= x <= 231 - 1 
#  
#  Related Topics Math Binary Search 
#  👍 2376 👎 2556


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, res = 1, x, 0
        while left <= right:
            mid = (left + right) // 2
            r = mid ** 2
            if r == x:
                return mid
            elif r > x:
                right = mid - 1
            else:
                res = mid
                left = mid + 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.mySqrt(2))
    print(solution.mySqrt(8))
    print(solution.mySqrt(17))
    print(solution.mySqrt(18))
    print(solution.mySqrt(26))
    print(solution.mySqrt(27))
    print(solution.mySqrt(33))
    print(solution.mySqrt(37))
