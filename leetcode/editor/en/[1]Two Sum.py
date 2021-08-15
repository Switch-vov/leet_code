# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 104 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  Only one valid answer exists. 
#  
# 
#  
# Follow-up: Can you come up with an algorithm that is less than O(n2) time comp
# lexity? Related Topics Array Hash Table 
#  👍 23306 👎 776


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = defaultdict()
        for i in range(len(nums)):
            mapping[nums[i]] = i
        for i in range(len(nums)):
            sub = target - nums[i]
            sub_index = mapping.get(sub)
            if sub_index and sub_index != i:
                return [i, sub_index]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([-1, -5, 11, 15], -6))
    print(solution.twoSum([1, 2], 3))
    print(solution.twoSum([-1, -5, 10, 15], 9))
    print(solution.twoSum([2, 5, 5, 11], 10))
