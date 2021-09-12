# You are given an array of integers nums, there is a sliding window of size k w
# hich is moving from the very left of the array to the very right. You can only s
# ee the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [9,11], k = 2
# Output: [11]
#  
# 
#  Example 5: 
# 
#  
# Input: nums = [4,-2], k = 2
# Output: [4]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  1 <= k <= nums.length 
#  
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Monotonic Que
# ue 
#  👍 6878 👎 256


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 定义一个双端队列
        deque, results = collections.deque(), []
        # 遍历列表
        for index in range(len(nums)):
            # 所有不在窗口范围内的全删除掉
            while deque and deque[0] < index - k + 1:
                deque.popleft()
            # 从后往前所有小于当前值的全干掉
            while deque and nums[deque[-1]] < nums[index]:
                deque.pop()
            # 将当前索引添加到双端队列
            deque.append(index)
            # 当当前索引大于等于k-1之后，才将双端队列第一个索引对应的值加入结果中
            if index >= k - 1:
                results.append(nums[deque[0]])
        # 返回结果
        return results


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(solution.maxSlidingWindow([1], 1))
    print(solution.maxSlidingWindow([1, -1], 1))
    print(solution.maxSlidingWindow([9, 11], 2))
    print(solution.maxSlidingWindow([9, 11, 13], 2))
    print(solution.maxSlidingWindow([4, -2], 2))
    print(solution.maxSlidingWindow([-7, -8, 7, 5, 7, 1, 6, 0], 4))
