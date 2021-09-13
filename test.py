# # a = [3,4,5]
# # # for n,i in enumerate(a):
# # # 	print(n,i)
# # print(a[:0])
# # s = {2:4,5:6}
# # for a in s.keys():
# # 	print(a)


# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         begin = 0
#         end = 0
#         dp=[_ for _ in range(len(s))]
#         for n,i in enumerate(s):
#             if (n==0) or ((n == 1) and (s[n] != s[n-1])):
#                 dp[n] = n
#             elif (dp[n] == 1) and (s[n] == s[n-1]):
#                 dp[n] = 0
#             elif i == s[dp[n-1]-1] and dp[n-1]!=0:
#                 dp[n] = dp[n-1]-1
#             elif dp[n-1]==0 and s[0:n] == i*(n):
#                 dp[n]=0
#             elif i == s[n-1] : 
#                 dp[n]=n-1
#         res = [0,0]
#         longest = 0
#         for n,i in enumerate(dp):
#             if n-i > longest:
#                 longest=n-i
#                 res = [i,n]
#         return s[res[0]:res[1]+1]
# class Solution1(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         max = 0
#         res = "" if s == "" else s[0]
#         dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
#         for i in range(len(s)):
#             dp[i][i] = 1   #表示从i - j 是回文串
#             max = max if max > 0 else 0
#             if s[i] == s[i-1] and i > 0:
#                 dp[i][i-1] = 1      #讲相邻字母相同的字符串标记好
#                 res = s[i-1:i+1]
#                 max = max if max > 1 else 1
#         for j in range(len(s)):
#             for i in range(j):
#                 if dp[i+1][j-1] == 1 and s[i] == s[j]:   #如s i处字母等于j处字母，且i+1到j-1为回文串，则i-j也为回文串。
#                     dp[i][j] = 1
#                     if (j - i) > max:
#                         max = j - i
#                         res = s[i:j+1]
#         return res
#print(Solution().longestPalindrome("aacabdkacaa"))
# print(Solution1().longestPalindrome("aaa"))



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





# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()