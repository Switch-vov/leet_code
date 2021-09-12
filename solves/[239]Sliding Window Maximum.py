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


class SolutionV1:
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


class SolutionV2:
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
