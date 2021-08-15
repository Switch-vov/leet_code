class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionV1:
    def swapPairs(self, head: ListNode) -> ListNode:
        this = ListNode()
        pre, pre.next = this, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return this.next


class SolutionV2:
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
