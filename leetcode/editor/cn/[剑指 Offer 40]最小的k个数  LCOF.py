# English description is not available for the problem. Please switch to Chinese
# . Related Topics 数组 分治 快速选择 排序 堆（优先队列） 
#  👍 281 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class Heap:
    def __init__(self):
        self.heap = []
        self.heap_length = 0

    def empty(self):
        return self.heap_length == 0

    def get_top(self) -> int:
        if self.empty():
            raise Exception("Empty heap")
        return self.heap[0]

    def pop_top(self) -> int:
        top = self.get_top()
        self.delete(0)
        return top

    def add(self, value: int):
        self.heap.append(value)
        self.heapify_up(self.heap_length)
        self.heap_length += 1

    def delete(self, index: int):
        if self.empty():
            raise Exception("Empty heap")
        self.heap_length -= 1
        self.heap[index] = self.heap[self.heap_length]
        del self.heap[self.heap_length]
        if not self.empty():
            self.heapify_down(index)

    def heapify_down(self, index: int):
        tmp = self.heap[index]
        while index < self.heap_length:
            min_child_index = self.min_child_index(index)
            if min_child_index >= self.heap_length or tmp < self.heap[min_child_index]:
                break
            self.heap[index] = self.heap[min_child_index]
            index = min_child_index
        self.heap[index] = tmp

    def heapify_up(self, index: int):
        tmp = self.heap[index]
        while index > 0:
            parent_index = self.parent_index(index)
            if tmp > self.heap[parent_index]:
                break
            self.heap[index] = self.heap[parent_index]
            index = parent_index
        self.heap[index] = tmp

    @staticmethod
    def parent_index(index):
        return int((index + 1) / 2) - 1

    def min_child_index(self, index) -> int:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if right_child_index >= self.heap_length:
            return left_child_index
        if self.heap[left_child_index] < self.heap[right_child_index]:
            return left_child_index
        return right_child_index


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # heap = Heap()
        # for a in arr:
        #     heap.add(a)
        heapq.heapify(arr)
        results = []
        for i in range(k):
            results.append(heapq.heappop(arr))
        return results


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
    heap = Heap()
    heap.add(1)
    heap.add(10)
    heap.add(1000)
    heap.add(7)
    heap.add(9)
    heap.add(2)
    heap.add(4)
    heap.add(2000)
    heap.add(4)
    heap.add(40)
    print(heap.pop_top())
    print(heap.pop_top())
    print(heap.pop_top())
    print(heap.pop_top())
    print(heap.pop_top())
    print(heap.pop_top())
    print(heap.pop_top())
    print(heap.pop_top())
    print(heap.pop_top())
    print(heap.pop_top())
