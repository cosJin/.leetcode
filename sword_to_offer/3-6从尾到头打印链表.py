# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        vallist = []
        while(head is not None):
            vallist.append(head.val)
            head = head.next
        return vallist[::-1]