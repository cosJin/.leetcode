class CQueue(object):

    def __init__(self):
        self.tmp_in = []
        self.tmp_out = []
    

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.tmp_in.append(value)
    def deleteHead(self):
        """
        :rtype: int
        """
        if self.tmp_out != []:
            return self.tmp_out.pop()
        elif self.tmp_in == [] : return -1
        else:
            while self.tmp_in != []:
                self.tmp_out.append(self.tmp_in.pop())
            return self.tmp_out.pop()
