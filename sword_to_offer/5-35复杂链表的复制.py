"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:return None
        st = head 
        st2 = head2 = Node(st.val)
        while st.next is not None:
            st = st.next
            st2.next = Node(st.val)
            st2 = st2.next
        st = head 
        st2 = head2 
        while st is not None:
            if st.random is None:
                st2.random = None
            else:
                tmpnode = head
                tmpnode2 = head2
                while(tmpnode != st.random):
                    tmpnode = tmpnode.next
                    tmpnode2 = tmpnode2.next
                st2.random = tmpnode2 
            st = st.next 
            st2 = st2.next
        return head2

#参考答案：
class Solution2(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:return None
        cur=head
        while cur:
            tmp=cur.next
            new_node=Node(cur.val)
            cur.next=new_node
            new_node.next=tmp
            cur=tmp
        cur=head
        while cur:
            cur_rd=cur.random
            nn=cur.next
            if cur_rd:
                nn.random=cur_rd.next
            else:
                nn.random=None
            cur=nn.next
        pre=head
        newn=head.next
        while pre:
            cur=pre.next
            pre.next=cur.next
            pre=cur.next
            if pre:
                cur.next=pre.next
            else:
                cur.next=None
        return newn
