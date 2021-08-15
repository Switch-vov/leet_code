# Given a positive integer num, write a function which returns True if num is a 
# perfect square else False. 
# 
#  Follow up: Do not use any built-in library function such as sqrt. 
# 
#  
#  Example 1: 
#  Input: num = 16
# Output: true
#  Example 2: 
#  Input: num = 14
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= num <= 2^31 - 1 
#  
#  Related Topics Math Binary Search 
#  👍 1460 👎 200


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right, res = 1, num, -1
        while left <= right:
            mid = (left + right) // 2
            r = mid ** 2
            if r == num:
                return True
            elif r < num:
                left = mid + 1
            else:
                right = mid - 1

        if res == -1:
            return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
