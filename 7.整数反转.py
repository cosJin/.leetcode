#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        neg = 1
        begin = 0
        if x < 0:
            x = -x 
            neg = -1
        tag = 10
        while x>0:
            tmp = x%10
            if  tmp != 0 or begin == 1:
                res = (res*10)+ tmp
                if begin == 0:begin=1
            x = int(x/10)
        return 0 if (res*neg<=-2**31 or res*neg>=(2**31)-1) else res*neg
# @lc code=end

print(-2**30 ,(2**30)-1)

print(Solution().reverse(123))