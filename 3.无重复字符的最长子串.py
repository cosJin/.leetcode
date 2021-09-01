#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:return 0
        i = 0
        j = 0
        res = 0
        for j in range(len(s)):
            if s[j] not in s[i:j]: 
                res = max(j-i+1,res)
            else:  
                while(s[i]!=s[j] and i<j):
                    i+=1
                i+=1
        return res
        
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        res = 0
        dic = {}
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]],i)
            dic[s[j]] = j
            res = max(res,j - i)
        return res
# @lc code=end

print(Solution().lengthOfLongestSubstring("tmmzuxt"))
