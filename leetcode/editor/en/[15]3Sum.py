# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k
# ]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics Array Two Pointers Sorting 
#  👍 12186 👎 1191


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if not nums or len(nums) < 3:
            return []
        results = set()
        for left in range(len(nums) - 2):
            if nums[left] > 0:
                break
            right = len(nums) - 1
            mid = left + 1
            while mid < right:
                sub = -(nums[left] + nums[right])
                if sub == nums[mid]:
                    results.add(f'{nums[left]},{nums[mid]},{nums[right]}')
                    mid += 1
                elif sub > nums[mid]:
                    mid += 1
                else:
                    right -= 1
        return [[int(n) for n in r.split(',')] for r in results]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([0]))
    print(solution.threeSum([]))
    print(solution.threeSum([1, 2]))
    print(solution.threeSum([1, 2, 3, -4]))
    print(solution.threeSum([-1, -2, -3, -4]))
    print(solution.threeSum([-1, -2, 3, -4]))
    print(solution.threeSum([0, 0, 0, 0]))
    print(solution.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
