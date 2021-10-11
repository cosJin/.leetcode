class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = {}
        for i in nums:
            if i not in tmp.keys():
                tmp[i] = 1
            else:
                return i
                
        dict = set()
        for i in nums:
            if i not in dict:
                dict.add(i)
            else:
                return i
