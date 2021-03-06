# Given the head of a linked list, return the list after sorting it in ascending
#  order. 
# 
#  Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.
# e. constant space)? 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 5 * 104]. 
#  -105 <= Node.val <= 105 
#  
#  Related Topics Linked List Two Pointers Divide and Conquer Sorting Merge Sort
#  
#  π 4821 π 187

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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ιε½εΊε£
        if not head or not head.next:
            return head
        # εΏ«ζ’ζιζΎε°δΈ­ι΄ηΉ
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None
        # ιε½
        left, right = self.sortList(head), self.sortList(mid)
        # εεΉΆιε½η»ζ
        cur = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                cur.next, left = left, left.next
            else:
                cur.next, right = right, right.next
            cur = cur.next
        cur.next = left if left else right
        # θΏειε½η»ζ
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
