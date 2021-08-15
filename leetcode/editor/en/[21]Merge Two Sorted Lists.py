# Merge two sorted linked lists and return it as a sorted list. The list should 
# be made by splicing together the nodes of the first two lists. 
# 
#  
#  Example 1: 
# 
#  
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#  
# 
#  Example 2: 
# 
#  
# Input: l1 = [], l2 = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: l1 = [], l2 = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both lists is in the range [0, 50]. 
#  -100 <= Node.val <= 100 
#  Both l1 and l2 are sorted in non-decreasing order. 
#  
#  Related Topics Linked List Recursion 
#  👍 7790 👎 828

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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        result = ListNode()
        it = result
        while l1 or l2:
            if not l1:
                it.next = l2
                break
            if not l2:
                it.next = l1
                break
            if l1.val <= l2.val:
                it.next, l1 = l1, l1.next
            else:
                it.next, l2 = l2, l2.next
            it = it.next
        return result.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution: Solution = Solution()
