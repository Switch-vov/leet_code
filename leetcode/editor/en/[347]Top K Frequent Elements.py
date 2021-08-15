# Given an integer array nums and an integer k, return the k most frequent eleme
# nts. You may return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#  Example 2: 
#  Input: nums = [1], k = 1
# Output: [1]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  k is in the range [1, the number of unique elements in the array]. 
#  It is guaranteed that the answer is unique. 
#  
# 
#  
#  Follow up: Your algorithm's time complexity must be better than O(n log n), w
# here n is the array's size. 
#  Related Topics Array Hash Table Divide and Conquer Sorting Heap (Priority Que
# ue) Bucket Sort Counting Quickselect 
#  👍 5756 👎 286


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict()
        for num in nums:
            mapping[num] = (mapping[num] if mapping.get(num) else 0) + 1
        items = [(-count, num) for num, count in mapping.items()]
        heapq.heapify(items)
        results = []
        for i in range(k):
            results.append(heapq.heappop(items)[1])
        return results


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
