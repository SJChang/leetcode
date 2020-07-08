# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = new_head = ListNode(0)
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            pre.next = tmp
            pre = head
            head = head.next
        return new_head.next