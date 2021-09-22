class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in s:
            if i == ' ':
                i = '%20'
            res += i
        return res 