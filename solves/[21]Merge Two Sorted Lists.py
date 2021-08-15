class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionV1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            tmp = l1
            l1 = l2
            l2 = tmp
        head = itr = l1
        l1 = l1.next
        while l1 or l2:
            if not l1:
                itr.next = l2
                break
            if not l2:
                itr.next = l1
                break
            l1_value = l1.val
            l2_value = l2.val
            if l2_value < l1_value:
                itr.next = l2
                l2 = l2.next
            else:
                itr.next = l1
                l1 = l1.next
            itr = itr.next
        return head
