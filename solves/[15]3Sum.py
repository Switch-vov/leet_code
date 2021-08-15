from typing import List


class SolutionV1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if not nums or len(nums) < 2:
            return []
        result = set()
        for left in range(len(nums) - 1):
            if nums[left] > 0:
                break
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                sub = -(nums[left] + nums[right])
                if nums[mid] == sub:
                    result.add(f'{nums[left]},{nums[mid]},{nums[right]}')
                if nums[mid] > sub:
                    right -= 1
                else:
                    mid += 1
        return [[int(num) for num in r.split(',')] for r in result]
