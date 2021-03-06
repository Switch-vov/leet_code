# Given n non-negative integers a1, a2, ..., an , where each represents a point 
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
#  the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x
# -axis forms a container, such that the container contains the most water. 
# 
#  Notice that you may not slant the container. 
# 
#  
#  Example 1: 
# 
#  
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,
# 3,7]. In this case, the max area of water (blue section) the container can conta
# inย is 49.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [1,1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: height = [4,3,2,1,4]
# Output: 16
#  
# 
#  Example 4: 
# 
#  
# Input: height = [1,2,1]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  2 <= n <= 105 
#  0 <= height[i] <= 104 
#  
#  Related Topics Array Two Pointers Greedy 
#  ๐ 10985 ๐ 760


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_area = 0, len(height) - 1, 0
        while left < right:
            height_left = height[left]
            height_right = height[right]
            current_height = (right - left) * min(height_left, height_right)
            if current_height > max_area:
                max_area = current_height
            if height_left > height_right:
                right -= 1
            else:
                left += 1
        return max_area


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
