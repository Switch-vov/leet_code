# An ugly number is a positive integer whose prime factors are limited to 2, 3, 
# and 5. 
# 
#  Given an integer n, return the nth ugly number. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 
# ugly numbers.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are li
# mited to 2, 3, and 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1690 
#  
#  Related Topics Hash Table Math Dynamic Programming Heap (Priority Queue) 
#  👍 2982 👎 175


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = set()
        h = []
        result = 1
        for i in range(1, n):
            r_two = result * 2
            r_three = result * 3
            r_five = result * 5
            if r_two not in s:
                s.add(r_two), heapq.heappush(h, r_two)
            if r_three not in s:
                s.add(r_three), heapq.heappush(h, r_three)
            if r_five not in s:
                s.add(r_five), heapq.heappush(h, r_five)
            result = heapq.heappop(h)
            s.remove(result)
        return result


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.nthUglyNumber(20))
