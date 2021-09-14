#
# @lc app=leetcode.cn id=10 lang=python
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[0 for _ in  range(len(p)+1) ] for _ in range(len(s)+1)]
        dp[0][0] = 1
        for i in range(len(s)+1):
            for j in range(len(p)+1)[1:]:
                if i==0:
                    # if dp[i][j-1]==1 and p[j-1] == '.': dp[i][j] = 1
                    if dp[i][j-1]==1 and p[j-1] == '*': dp[i][j] = 1
                    elif dp[i][j-2]==1 and p[j-1] == '*': dp[i][j] = 1
                else:
                    if s[i-1] == p[j-1] and dp[i-1][j-1] == 1: dp[i][j] = 1
                    elif p[j-1] == '.' and dp[i-1][j-1] == 1:dp[i][j] = 1
                    elif p[j-1] == '*' and dp[i-1][j-1] == 1 and s[i-1] == p[j-2]: dp[i][j] = 1
                    elif p[j-1] == '*' and dp[i][j-2] == 1: dp[i][j] = 1
                    elif p[j-1] == '*' and dp[i][j-1] == 1: dp[i][j] = 1
                    elif p[j-1] == '*' and dp[i-1][j] == 1 and s[i-1] == p[j-2]: dp[i][j] = 1
                    elif p[j-1] == '*' and p[j-2] == '.' and (dp[i-1][j-1] == 1  or dp[i][j-1] == 1 or dp[i-1][j]):dp[i][j] =1
        return True if dp[-1][-1] == 1 else False
# @lc code=end
print(Solution().isMatch('aaa','a*'))

# [1, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 1, 0, 1, 1, 1, 0, 1, 1],
# [0, 0, 0, 0, 1, 1, 0, 1, 1], 
# [0, 0, 0, 0, 0, 0, 1, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0]]