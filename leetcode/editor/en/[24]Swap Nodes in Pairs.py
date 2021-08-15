# Given a linked list, swap every two adjacent nodes and return its head. You mu
# st solve the problem without modifying the values in the list's nodes (i.e., onl
# y nodes themselves may be changed.) 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 100]. 
#  0 <= Node.val <= 100 
#  
#  Related Topics Linked List Recursion 
#  👍 4230 👎 227

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
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        this = ListNode()
        pre, pre.next = this, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            a.next = b.next
            b.next = a
            pre.next = b
            pre = a
        return this.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
