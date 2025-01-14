# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next      # mid
            fast = fast.next.next # last
        mid = slow.next
        slow.next = None

        left = self.sortList(head) # self.merge(left,right)
        right = self.sortList(mid) # self.merge(left,right)

        return self.merge(left,right)


    def merge(self, l1: Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy

        while l1 and l2:
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
                result = result.next
            else:
                result.next = l2
                l2 = l2.next
                result = result.next

        result.next = l1 if l1 else l2
        return dummy.next
