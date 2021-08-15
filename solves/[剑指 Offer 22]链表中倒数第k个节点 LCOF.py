class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionV1:
    # 计算数量n，然后再找到第n-k+1个节点
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        count = 0
        dummy = cur = ListNode(0)
        dummy.next = head
        while cur:
            count += 1
            cur = cur.next
        target = count - k + 1
        cur = dummy
        while target > 1:
            cur = cur.next
            target -= 1
        return cur


class SolutionV2:
    # 双指针，得到相差值后，再一起遍历
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy, dummy.next = ListNode(0), head
        back = front = dummy
        while k > 0:
            front, k = front.next, k - 1
        while front:
            back, front = back.next, front.next
        return back
