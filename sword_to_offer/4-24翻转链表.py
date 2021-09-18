# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None :
            return head
        n = head.next
        if head.next.next is None:
            n.next = head
            head.next = None
            return n
        nn = head.next.next
        n.next = head
        head.next = None 
        while nn.next is not None:
            head = n
            n = nn 
            nn = nn.next
            n.next = head  
        nn.next = n 
        return nn