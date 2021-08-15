# Given an integer array nums of unique elements, return all possible subsets (t
# he power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in a
# ny order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: [[],[0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  All the numbers of nums are unique. 
#  
#  Related Topics Array Backtracking Bit Manipulation 
#  👍 6734 👎 120


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(results, [], 0, nums)
        return results

    def dfs(self, results: List[List[int]], result: List[int], level: int, nums: List[int]):
        if level == len(nums):
            results.append(result.copy())
            return
        result.append(nums[level])
        self.dfs(results, result, level + 1, nums)
        result.pop()
        self.dfs(results, result, level + 1, nums)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.subsets([1, 2, 3]))
    print(solution.subsets([1, 2, 3, 4, 5, 6]))
    print(solution.subsets([0]))
