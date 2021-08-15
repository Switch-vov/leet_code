# English description is not available for the problem. Please switch to Chinese
# . Related Topics 链表 双指针 
#  👍 220 👎 0

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy, dummy.next = ListNode(0), head
        back = front = dummy
        while k > 0:
            front, k = front.next, k - 1
        while front:
            back, front = back.next, front.next
        return back


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
