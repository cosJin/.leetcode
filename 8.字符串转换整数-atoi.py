#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        dir={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        bef={'-':-1,' ':0,'+':1}
        begin = 1
        res = 0
        tag = 1
        for t in s:
            if t in dir or t in bef:
                if t in bef:
                    if begin == 0:return res
                    elif bef[t] == -1 or bef[t] == 1: 
                        tag = bef[t]
                        begin=0
                    continue
                i = dir[t]
                if i != 0 or begin == 0:
                    res = res*10 + i
                    begin = 0
            else: return res
        return -2**31 if res*tag <= -2**31 else 2**31-1 if res*tag >= 2**31-1 else res*tag



# @lc code=end

print(Solution().myAtoi("   -12"))