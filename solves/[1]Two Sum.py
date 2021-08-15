from collections import defaultdict

from typing import List


class SolutionV1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = defaultdict()
        for index in range(len(nums)):
            mapping[nums[index]] = index
        for index in range(len(nums)):
            sub = target - nums[index]
            other_index = mapping.get(sub)
            if not other_index:
                continue
            if other_index != index:
                return [index, other_index]
