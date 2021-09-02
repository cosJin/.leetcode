#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#
# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 0
        res = "" if s == "" else s[0]
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1   #表示从i - j 是回文串
            max = max if max > 0 else 0
            if s[i] == s[i-1] and i > 0:
                dp[i][i-1] = 1      #讲相邻字母相同的字符串标记好
                res = s[i-1:i+1]
                max = max if max > 1 else 1
        for j in range(len(s)):
            for i in range(j):
                if dp[i+1][j-1] == 1 and s[i] == s[j]:   #如s i处字母等于j处字母，且i+1到j-1为回文串，则i-j也为回文串。
                    dp[i][j] = 1
                    if (j - i) > max:
                        max = j - i
                        res = s[i:j+1]
        return res
        #return res