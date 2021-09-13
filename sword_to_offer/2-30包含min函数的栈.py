class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minu = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minu:
            self.minu.append(x)
        else:
            if x<=self.minu[-1]:
                self.minu.append(x)


    def pop(self):
        """
        :rtype: None
        """
        tmp_pop = self.stack.pop()
        if tmp_pop == self.minu[-1]:
            self.minu.pop()
        return tmp_pop



    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:return -1
        else: return self.stack[-1]




    def min(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:return None
        else: return self.minu[-1]

