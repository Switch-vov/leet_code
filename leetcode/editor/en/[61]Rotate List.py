# Given the head of a linked list, rotate the list to the right by k places. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 500]. 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 109 
#  
#  Related Topics Linked List Two Pointers 
#  👍 2917 👎 1183

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        k_count = k % count
        if k_count == 0:
            return head
        count = count - k_count
        cur = head
        pre, pre.next = ListNode(), cur
        while count > 0:
            pre = cur
            cur = cur.next
            count -= 1
        h = pre.next
        pre.next = None
        while cur.next:
            cur = cur.next
        cur.next = head
        return h


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
