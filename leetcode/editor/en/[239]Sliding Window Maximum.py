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


class MonotonicQueue:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, num: int):
        while self.queue and self.queue[-1] < num:
            self.queue.pop()
        self.queue.append(num)

    def pop(self, num: int) -> int:
        if self.queue and self.queue[0] == num:
            return self.queue.popleft()

    def max(self) -> int:
        if self.queue:
            return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        mono_queue = MonotonicQueue()
        for i in range(len(nums)):
            if i < k - 1:
                mono_queue.push(nums[i])
            else:
                mono_queue.push(nums[i])
                results.append(mono_queue.max())
                mono_queue.pop(nums[i - k + 1])
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
