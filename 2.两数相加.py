#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = res = ListNode()
        # start = res
        jw = 0
        while ((l1 is not None) or (l2 is not None)):
            res.next = ListNode()
            res = res.next
            res.val = ((l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + jw) % 10
            jw = ((l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + jw) / 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if jw == 1:
            res.next = ListNode()
            res = res.next
            res.val = 1
        return start.next


# @lc code=end

